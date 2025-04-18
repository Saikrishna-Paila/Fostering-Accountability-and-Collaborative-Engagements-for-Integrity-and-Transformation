# Usage Guide

## Starting the Application

1. Activate your virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Start the application:
   ```bash
   streamlit run src/jurisai/app.py
   ```

3. Open your browser and navigate to `http://localhost:8501`

## Using JurisAI

### Country Selection
1. Choose your country (Ghana or Sierra Leone)
2. Select your preferred language:
   - Ghana: English or Akan
   - Sierra Leone: English or Krio

### Legal Queries
1. Type your legal question in the text box
2. Click "Submit" to get a response
3. The system will:
   - Search relevant legal documents
   - Provide an answer in your chosen language
   - Include citations to legal sources

### Translation Features
- Toggle between languages using the language selector
- All responses are automatically translated
- Legal terms are preserved for accuracy

## API Usage

For API integration examples, see:
- [API Examples Notebook](../notebooks/api-examples.ipynb)
- [Translation Examples Notebook](../notebooks/translation-examples.ipynb) 