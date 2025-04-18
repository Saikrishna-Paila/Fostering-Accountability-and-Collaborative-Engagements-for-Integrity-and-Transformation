import streamlit as st
import time
from be_pipe import (
    country_configs, handle_basic_queries,
    retrieve_relevant_documents, query_groq_model, embeddings, akan_translation, krio_translation, summarize_response
)
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as LangchainPinecone

# Set up the Streamlit page
st.set_page_config(page_title="JurisAI", layout="wide")

# 🟡 Akan Translation Dictionary
translations_akan = {
    "select_country": "Paw wo man",
    "about_jurisai": "Fa ho nsɛɛm afa JurisAI ho",
    "about_desc": "JurisAI yɛ wo mmaranimfoɔɛ boafoɔɛ a ɔwɔ nyansa, ɔde mmuaeɛɛ a ɛɛ ntɛm na wotumi de ho to so a AI na ɛma ahoɔden na ɛɛ wo man mmara nhyehyɛɛ ma.",
    "legal_resources": "Mmara Nnwuma",
    "ghalii": "[Ghana Mmara Nsɛm (GhaLII)](https://ghalii.org)",
    "sierralii": "[Sierra Leone Mmara Nsɛm (SierraLII)](https://sierralii.gov.sl)",
    "app_title": "JurisAI ⚖️ | Mmara Akwankyerɛ a Wogye Di a AI Efficiency wom",
    "chat_prompt": "Hyɛ wo mmara mu nsɛmmisa wɔ ha (Żw borɔfo kasa mu)...",
    "updated_till": "Wɔyɛɛ no ​​foforo nea etwa to: April 2025"
}

# 🔣 Krio Translation Dictionary
translations_krio = {
    "select_country": "Choos yu kontri",
    "about_jurisai": "Na bɔt JurisAI",
    "about_desc": "JurisAI na yu intɛligent ligal ɛstɛt, we de gi fast ɛn rilibul ansa dɛn we AI de pawa ɛn we dɛn tayla to yu kɔntri in ligal sistɛm.",
    "legal_resources": "Lɛlgal Risɔs Dem",
    "ghalii": "[Ghana Ligal Risos  (GhaLII)](https://ghalii.org)",
    "sierralii": "[Sierra Leone Ligal Risos  (SierraLII)](https://sierralii.gov.sl)",
    "app_title": "JurisAI ⚖️ | Trusted Ligal Gaydɛnɛs wit AI Efyushɔn",
    "chat_prompt": "Rayt yu lɛlgal kwɛwshɔn ya (insayd English)...",
    "updated_till": "Las ɔpdet: Epril 2025"
}



# Initialize session state
if "country_code" not in st.session_state:
    st.session_state.country_code = "1"

if "translate_to_akan" not in st.session_state:
    st.session_state.translate_to_akan = False

if "translate_to_krio" not in st.session_state:
    st.session_state.translate_to_krio = False
# Update country config
country_code = st.session_state.country_code



# ✅ 1. Determine current country config
country_config = country_configs[st.session_state.country_code]

# ✅ 2. Reset toggle values if country has changed
if "last_country_code" not in st.session_state:
    st.session_state.last_country_code = st.session_state.country_code

if st.session_state.country_code != st.session_state.last_country_code:
    st.session_state.translate_to_akan = False
    st.session_state.translate_to_krio = False
    st.session_state.last_country_code = st.session_state.country_code
    st.rerun()


# ✅ 3. Then show toggle button for the selected country
country_config = country_configs[st.session_state.country_code]

if country_config["name"] == "Ghana":
    col1, col2 = st.columns([6, 1])
    with col2:
        new_toggle_value = st.toggle(
            "Akan",
            value=st.session_state.translate_to_akan,
            help="Translate responses to Akan language",
            key="akan_toggle"
        )
        if new_toggle_value != st.session_state.translate_to_akan:
            st.session_state.translate_to_akan = new_toggle_value
            st.session_state.user_query = None
            st.session_state.full_response = ""
            st.session_state.response_shown = False
            st.session_state.summary_shown = False
            st.rerun()

elif country_config["name"] == "Sierra Leone":
    col1, col2 = st.columns([5, 1])
    with col2:
        new_toggle_value = st.toggle(
            "Krio",
            value=st.session_state.translate_to_krio,
            help="Translate responses to Krio language",
            key="krio_toggle"
        )
        if new_toggle_value != st.session_state.translate_to_krio:
            st.session_state.translate_to_krio = new_toggle_value
            st.session_state.user_query = None
            st.session_state.full_response = ""
            st.session_state.response_shown = False
            st.session_state.summary_shown = False
            st.rerun()


## 🧠 Sidebar 
with st.sidebar:
    st.image("logo.png")
    st.markdown('<hr style="margin-top: 2px; margin-bottom: 2px;">', unsafe_allow_html=True)

    # Determine translation dictionary
    use_translation = translations_krio if st.session_state.translate_to_krio else (
        translations_akan if st.session_state.translate_to_akan else None)

    label_select_country = use_translation["select_country"] if use_translation else "Select your country:"

    # ⛳ Country selector (this updates country_code in session)
    selected_country = st.selectbox(
        label_select_country,
        options=["1", "2"],
        index=["1", "2"].index(st.session_state.country_code),
        key="country_selector",
        format_func=lambda x: f"{country_configs[x]['name']} {country_configs[x]['flag']}"
    )

    # 🔁 Reset toggles when country changes
    if selected_country != st.session_state.country_code:
        st.session_state.country_code = selected_country

        # 🔄 Clear previous query and states
        st.session_state.user_query = None
        st.session_state.full_response = ""
        st.session_state.response_shown = False
        st.session_state.summary_shown = False

        st.session_state.translate_to_akan = False
        st.session_state.translate_to_krio = False
        st.rerun()

    # 🧠 About JurisAI
    label_about = use_translation["about_jurisai"] if use_translation else "About JurisAI"
    label_about_desc = use_translation["about_desc"] if use_translation else (
        "JurisAI is your intelligent legal assistant, offering fast and reliable answers powered by AI and tailored to your country’s legal system."
    )
    st.subheader(label_about)
    st.markdown(label_about_desc)

    # 📚 Legal Resources
    label_resources = use_translation["legal_resources"] if use_translation else "Legal Resources"
    ghalii = use_translation["ghalii"] if use_translation else "[Ghana Legal Info (GhaLII)](https://ghalii.org)"
    sierralii = use_translation["sierralii"] if use_translation else "[Sierra Leone Law (SierraLII)](https://sierralii.gov.sl)"
    updated_text = use_translation["updated_till"] if use_translation else "Last update: April 2025"

    st.subheader(label_resources)
    st.markdown(f"{ghalii}  \n{sierralii}")
    st.markdown(f"<small>{updated_text}</small><hr style='margin-top: 2px; margin-bottom: 2px'>", unsafe_allow_html=True)

    if use_translation == translations_akan:
        footer_caption = (
            "JurisAI v1.0 a ɛwɔ hɔ no |GWU Master’s Students na wɔyɛɛ no ​​maa Wiase Nyinaa Mmara kwan so Nkɔsoɔ"
        )
    elif use_translation == translations_krio:
        footer_caption = (
            "JurisAI v1.0 we de na di wɔl | Na GWU Masta Studɛnt dɛn mek am fɔ Globɛl Ligal Akses"
        )
    else:
        footer_caption = "JurisAI v1.0 | Created by GWU Master's Students for Global Legal Access"

    st.caption(footer_caption)


# Page Title and Chat Input
use_translation = translations_krio if st.session_state.translate_to_krio else (
    translations_akan if st.session_state.translate_to_akan else None)

title_text = use_translation["app_title"] if use_translation else "JurisAI ⚖️ | Trusted Legal Guidance with AI Efficiency"
chat_placeholder = use_translation["chat_prompt"] if use_translation else "Type your legal question..."

st.title(title_text)

# Initialize session states
if "user_query" not in st.session_state:
    st.session_state.user_query = None

if "response_shown" not in st.session_state:
    st.session_state.response_shown = False

if "summary_shown" not in st.session_state:
    st.session_state.summary_shown = False

# Accept input only if no question is active

user_query = st.chat_input(chat_placeholder)

if user_query:
    # New question asked → reset session
    st.session_state.user_query = user_query
    st.session_state.full_response = ""
    st.session_state.response_shown = False
    st.session_state.summary_shown = False
    st.rerun()
if user_query:
        st.session_state.user_query = user_query

# Show user question
if st.session_state.user_query:
    with st.chat_message("user",avatar="🙎"):
        st.markdown(f"**{st.session_state.user_query}**")

# Show assistant response if not already shown
if st.session_state.user_query and not st.session_state.response_shown:
    with st.chat_message("assistant",avatar="💬"):
        placeholder = st.empty()
        response = ""

        basic = handle_basic_queries(st.session_state.user_query)
        if basic:
            st.session_state.full_response = basic
        else:
            pc = Pinecone(api_key=country_config["pinecone_api_key"])
            index = pc.Index(country_config["index_name"])
            vector_store = LangchainPinecone(index=index, embedding=embeddings, text_key='text')
            docs = retrieve_relevant_documents(st.session_state.user_query, vector_store)
            context = "\n\n".join([doc.page_content for doc in docs])
            st.session_state.full_response = query_groq_model(context, st.session_state.user_query, country_config["name"]) or "⚠️ Sorry, couldn't find an answer."

        # Translate if needed
        final_response = st.session_state.full_response
        if st.session_state.translate_to_akan and country_config["name"] == "Ghana":
            final_response = akan_translation(final_response)
        elif st.session_state.translate_to_krio and country_config["name"] == "Sierra Leone":
            final_response = krio_translation(final_response)

        for char in final_response:
            response += char
            placeholder.markdown(response)
            time.sleep(0.01)

        st.session_state.response_shown = True

# Show summary button if response was shown
if st.session_state.response_shown and not st.session_state.summary_shown:
    # Set translated button and title
    if st.session_state.translate_to_akan:
        summarize_button_label = "🔁 Bobɔ mmuae no mua"
        summary_title = "Tɔfabɔ"
    elif st.session_state.translate_to_krio:
        summarize_button_label = "🔁 Sɔmariz di ansa"
        summary_title = "Ɛksplen"
    else:
        summarize_button_label = "🔁 Summarize the response"
        summary_title = "Summary"

    if st.button(summarize_button_label):
        summary = summarize_response(st.session_state.full_response)

        # Translate summary
        if st.session_state.translate_to_akan and country_config["name"] == "Ghana":
            summary = akan_translation(summary)
        elif st.session_state.translate_to_krio and country_config["name"] == "Sierra Leone":
            summary = krio_translation(summary)

        # Show summary below the original
        with st.chat_message("assistant",avatar="💬"):
            st.markdown(f"**{summary_title}:**")
            summary_placeholder = st.empty()
            summary_output = ""
            for char in summary:
                summary_output += char
                summary_placeholder.markdown(summary_output)
                time.sleep(0.01)

        st.session_state.summary_shown = True
