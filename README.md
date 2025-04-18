# JurisAI: Legal Assistant for Ghana and Sierra Leone 🇬🇭 🇸🇱

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Mozilla-blue.svg)](LICENSE)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jurisai.streamlit.app)

## Overview

JurisAI is an intelligent legal assistant that provides accessible legal guidance for Ghana and Sierra Leone. Built with Streamlit and powered by advanced language models, it offers legal information in multiple languages to bridge the accessibility gap in legal services.

### Key Features

- **Multilingual Support**:
  - 🇬🇭 Ghana: English and Akan (Twi)
  - 🇸🇱 Sierra Leone: English and Krio
- **AI-powered Legal Assistance**:
  - Legal question answering
  - Document analysis
  - Context-aware responses
- **User-friendly Interface**:
  - Simple chat interface
  - Easy language switching
  - Mobile-responsive design

## Getting Started

### Prerequisites

1. **Python Environment**:
   - Python 3.9 or higher
   - pip (Python package installer)

2. **API Keys**:
   - OpenAI API Key
   - Pinecone API Key
   - Google Cloud Translation API Key

### Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/worldbank/jurisai.git
cd jurisai
```

2. **Set Up Python Environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

4. **Configure Environment**:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Project Structure

```
jurisai/
├── src/
│   └── jurisai/
│       ├── __init__.py
│       ├── app.py          # Streamlit application
│       └── be_pipe.py      # Backend processing
├── docs/                   # Documentation
├── notebooks/             # Example notebooks
├── tests/                # Test files
├── config/               # Configuration files
├── data/                # Data files (gitignored)
└── requirements.txt     # Project dependencies
```

## Core Dependencies

- **Frontend**: Streamlit
- **AI/ML**:
  - OpenAI
  - LangChain
  - Pinecone
  - Groq
- **Translation**:
  - Google Cloud Translate
  - deep-translator

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the Mozilla Public License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- World Bank Group
- Ghana Legal Information Institute (GhaLII)
- Sierra Leone Legal Information Institute (SierraLII)
- GWU Master's Students

---

**Note**: This project is maintained by GWU Master's Students for Global Legal Access. Country borders or names do not necessarily reflect the World Bank Group's official position.
