import os
import requests
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.base import VectorStoreRetriever
from sklearn.metrics.pairwise import cosine_similarity
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from typing import List
import warnings
import time
from functools import wraps
from deep_translator import GoogleTranslator
warnings.filterwarnings("ignore", category=DeprecationWarning)
from openai import OpenAI
from google.cloud import translate_v2 as gtranslate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secrets/jurisai-gcp-translation-key.json"

# Load environment variables
load_dotenv(override=True)
ghana_api_key = os.getenv("GHANA_PINECONE_API_KEY")
sierra_api_key = os.getenv("SIERRA_LEONE_PINECONE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Shared OpenAI embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Rate limiting decorator

def rate_limited(max_calls_per_minute):
    interval = 60.0 / max_calls_per_minute
    def decorator(func):
        last_called = [0.0]
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait = interval - elapsed
            if wait > 0:
                time.sleep(wait)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Country configuration
country_configs = {
    "1": {
        "name": "Ghana",
        "flag": "🇬🇭",
        "pinecone_api_key": ghana_api_key,
        "index_name": "legalbot-ghana"
    },
    "2": {
        "name": "Sierra Leone",
        "flag": "🇸🇱",
        "pinecone_api_key": sierra_api_key,
        "index_name": "legalbot"
    }
}

# Handle greetings and basic queries
def handle_basic_queries(user_input: str) -> str:
    greetings = ["hello", "hi", "good morning", "good afternoon", "good evening"]
    basic_queries = {
        "how are you": "I'm just a bot, but I'm here to assist you with your legal questions!",
        "what is your name": "I am JurisAI, your legal assistant.",
        "who are you": "I am JurisAI, an AI developed to assist with legal information."
    }
    if user_input.lower() in greetings:
        return "Hello! How can I assist you with your legal questions today?"
    elif user_input.lower() in basic_queries:
        return basic_queries[user_input.lower()]
    return None

# Document retrieval using MMR and dynamic k
def retrieve_relevant_documents(query: str, vector_store: LangchainPinecone) -> List[str]:
    try:
        k = 3 if len(query.split()) > 15 else 2
        retriever: VectorStoreRetriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": k, "lambda_mult": 0.7}
        )
        return retriever.get_relevant_documents(query)
    except Exception as e:
        print(f"❌ Error during document retrieval: {e}")
        return []

# BLEU with smoothing
def evaluate_bleu(query, answer):
    try:
        reference = query.lower().split()
        candidate = answer.lower().split()
        smoothie = SmoothingFunction().method4
        return sentence_bleu([reference], candidate, smoothing_function=smoothie)
    except Exception as e:
        print(f"❌ BLEU score evaluation error: {e}")
        return 0.0

# Cosine similarity evaluation
def evaluate_cosine_similarity(query, documents):
    try:
        query_emb = embeddings.embed_query(query)
        scores = []
        for doc in documents:
            doc_emb = embeddings.embed_query(doc.page_content)
            sim = cosine_similarity([query_emb], [doc_emb])[0][0]
            scores.append(sim)
        return sum(scores) / len(scores) if scores else 0
    except Exception as e:
        print(f"❌ Cosine similarity evaluation error: {e}")
        return 0.0

# Build prompt with instructions for format
def build_prompt(context, question, country_name):
        return f"""
    You are **JurisAI**, a legal assistant for **{country_name}**. Your role is to provide **accurate, well-structured, and legally sound** guidance in a **clear, conversational, and human-like manner**.  

    You are **JurisAI**, a legal expert specializing in the **laws of Sierra Leone**. 

    ### **📌 Guidelines for Responses**
    - Use **simple, precise language** while maintaining legal accuracy.  
    - **Avoid unnecessary legal jargon** unless essential, and provide **brief explanations** where needed.  
    - **Base responses on the most recent laws, amendments, and case law** relevant to {country_name}.
    - Always **mention the applicable law, year of enactment, and date of the latest revision** when available.  
    - If **uncertainty exists**, provide **the best legal interpretation**, cite **relevant legal provisions**, and suggest **trusted verification sources** (e.g., government sources or legal professionals).  
    - 🚫 **Do not provide hyperlinks or clickable links in your response.**

    ### **🚨 Important Instructions for JurisAI**
    - **If the user asks about laws from another country**, politely clarify:  
    *"As a specialized legal assistant, my expertise is in {country_name}. I can provide guidance on legal matters specific to {country_name}. If you're looking for information on another country's laws, I recommend consulting an expert in that jurisdiction."*
    - **If the question is unrelated to law**, respond with:  
    *"My expertise is in legal matters. If you have any legal questions related to {country_name}, I'd be happy to assist!"*
    - **If I don't have sufficient legal information on a topic**, say:  
    *"Based on my available legal sources, I have limited details on this matter. However, I recommend referring to an official legal expert or government sources for further clarification."*

    🧾 **Legal Context:**
    {context}

    ❓ **User's Question:**
    {question}

    Respond in plain English, cite relevant laws, and avoid jargon unless explained.
    """.strip()


# Query Groq model
@rate_limited(60)  # Limit to 60 requests per minute
def query_groq_model(context, question, country_name):
    try:
        prompt = build_prompt(context, question, country_name)
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "system",
                    "content": f"You are JurisAI, a legal assistant for {country_name}.​For general inquiries or greetings, provide concise and relevant responses.​ For legal questions, offer detailed answers including:​Applicable legal references,Glossary of legal terms used, Relevant links, if available."
                },
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 600
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {groq_api_key}"
        }
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            print(f"❌ API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Exception during Groq query: {e}")
        return None

# Run chat loop for a selected country
def run_chat_for_country(config):
    print(f"\n🤖 JurisAI ({config['name']} {config['flag']}) is now active!")
    try:
        pc = Pinecone(api_key=config["pinecone_api_key"])
        index = pc.Index(config["index_name"])
        vector_store = LangchainPinecone(index=index, embedding=embeddings, text_key='text')
    except Exception as e:
        print(f"❌ Error initializing Pinecone or Vector Store: {e}")
        return

    while True:
        user_query = input("Ask your legal question (type 'bye' to return): ").strip()
        if user_query.lower() == 'bye':
            print("\nReturning to country selection...\n")
            break

        try:
            basic_response = handle_basic_queries(user_query)
            if basic_response:
                print(f"\n🧾 Answer:\n{basic_response}")
                continue

            docs = retrieve_relevant_documents(user_query, vector_store)
            context = "\n\n".join([doc.page_content for doc in docs])

            sources = []
            for doc in docs:
                source_url = doc.metadata.get('source')
                if source_url and source_url.startswith("http"):
                    sources.append(f"* [View Source]({source_url})")
            if sources:
                context += "\n\n🔗 Source links:\n" + "\n".join(sources)

            answer = query_groq_model(context, user_query, config["name"])

            if answer:
                print(f"\n🧾 Answer:\n{answer}")
                if sources:
                    print("\n🔗 Sources from JurisAI database:")
                    for link in sources:
                        print(link)
                bleu_score = evaluate_bleu(user_query, answer)
                sim_score = evaluate_cosine_similarity(user_query, docs)
                print(f"\n📊 Evaluation Metrics:\n   BLEU Score: {bleu_score:.2f}\n   Context Similarity (Cosine): {sim_score:.2f}")
            else:
                print("❌ No response from the model.")
        except Exception as e:
            print(f"❌ Unexpected error during chat loop: {e}")


# def akan_translation(text: str) -> str:
#     """
#     Translates English text to Akan using Deep Translator (Google Translate).
#     Returns the original text if translation fails.
#     """
#     try:
#         translated = GoogleTranslator(source='auto', target='ak').translate(text)
#         return translated
#     except Exception as e:
#         print(f"❌ Translation to Akan failed: {e}")
#         return text

# def krio_translation(text: str) -> str:
#     """
#     Translates English text to Krio using Deep Translator (Google Translate).
#     Returns the original if translation fails.
#     """
#     try:
#         return GoogleTranslator(source='auto', target='kri').translate(text)
#     except Exception as e:
#         print(f"❌ Translation to Krio failed: {e}")
#         return text


try:
    gtranslate_client = gtranslate.Client()
except Exception as e:
    print(f"⚠️ Google Translate API initialization failed: {e}")
    gtranslate_client = None


def translate_text(text: str, target: str, retries: int = 2) -> str:
    """
    Attempts to translate using Google API, falls back to Deep Translator on failure.
    """
    # Try Google Translate API
    if gtranslate_client:
        for attempt in range(retries):
            try:
                result = gtranslate_client.translate(text, target_language=target)
                return result["translatedText"]
            except Exception as e:
                print(f"⚠️ Google API translation to '{target}' failed (attempt {attempt+1}): {e}")
                time.sleep(1)

    # Fallback: Deep Translator
    for attempt in range(retries):
        try:
            return GoogleTranslator(source='auto', target=target).translate(text)
        except Exception as e:
            print(f"❌ Deep Translator failed for '{target}' (attempt {attempt+1}): {e}")
            time.sleep(1)

    # All attempts failed
    return text


def akan_translation(text: str) -> str:
    return translate_text(text, target='ak')


def krio_translation(text: str) -> str:
    return translate_text(text, target='kri')


client = OpenAI(api_key=openai_api_key)  # Make sure openai_api_key is already loaded

def summarize_response(text: str) -> str:
    try:
        prompt = ("The following is a detailed legal explanation in response to a user's question. "
            "Your job is to summarize it into 3–4 short, easy-to-understand sentences, as if you were explaining it to someone without a legal background. "
            "Keep it simple, clear, and conversational. Mention any important laws, requirements, or rights, but avoid heavy legal jargon.\n\n"
            f"Legal Text:\n{text}"
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            messages=[
                {"role": "system", "content": "You are a helpful assistant who explains legal answers in simple, human language."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Failed to generate summary: {str(e)}"


