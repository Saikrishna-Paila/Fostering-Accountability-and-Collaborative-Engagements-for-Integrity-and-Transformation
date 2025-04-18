# JurisAI: Legal Assistant for Ghana and Sierra Leone 🇬🇭 🇸🇱

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Mozilla-blue.svg)](LICENSE)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jurisai.streamlit.app)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-blue)](https://www.pinecone.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.20-orange)](https://python.langchain.com/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Saikrishna-Paila/Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation/graphs/commit-activity)
[![GitHub last commit](https://img.shields.io/github/last-commit/Saikrishna-Paila/Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation)](https://github.com/Saikrishna-Paila/Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation/commits/main)

## Overview

JurisAI is an intelligent legal assistant that provides accessible legal guidance for Ghana and Sierra Leone. Built with Streamlit and powered by advanced language models, it offers legal information in multiple languages to bridge the accessibility gap in legal services.

### Key Features

- **Multilingual Support**:
  - 🇬🇭 Ghana: English and Akan (Twi) translation
  - 🇸🇱 Sierra Leone: English and Krio translation
  - Real-time language switching
  - Culturally appropriate translations

- **AI-powered Legal Assistance**:
  - Interactive legal question answering
  - Context-aware responses using LangChain
  - Legal document analysis and summarization
  - Pinecone vector search for relevant legal documents

- **User-friendly Interface**:
  - Clean and intuitive Streamlit chat interface
  - Easy language toggle buttons
  - Mobile-responsive design
  - Real-time response generation

## Technical Architecture

### Backend Components
- **LangChain Integration**:
  - Document processing and chunking
  - Vector embeddings management
  - Prompt templates and chains
  - Context-aware response generation

- **Vector Search**:
  - Pinecone for document similarity search
  - Efficient retrieval of relevant legal information
  - Semantic search capabilities

- **Translation Services**:
  - Google Cloud Translation API integration
  - Deep-translator for backup translations
  - Custom translation dictionaries for legal terms

### Frontend Components
- **Streamlit UI**:
  - Chat-based interface
  - Language selection toggles
  - Progress indicators
  - Response formatting
  - Error handling

## Getting Started

### Prerequisites

1. **Python Environment**:
   - Python 3.9 or higher
   - pip (Python package installer)

2. **Required API Keys**:
   - OpenAI API Key (for GPT models)
   - Pinecone API Key (for vector search)
   - Google Cloud Translation API Key
   - Groq API Key (optional)

### Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/Saikrishna-Paila/Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation.git
cd Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation
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

4. **Configure Environment Variables**:
```bash
cp .env.example .env
# Edit .env with your API keys:
# - OPENAI_API_KEY
# - PINECONE_API_KEY
# - PINECONE_ENVIRONMENT
# - GOOGLE_CLOUD_API_KEY
# - GROQ_API_KEY (optional)
```

## Project Structure

```
jurisai/
├── src/
│   └── jurisai/
│       ├── __init__.py
│       ├── app.py          # Streamlit application
│       └── be_pipe.py      # Backend processing pipeline
├── docs/                   # Documentation
├── notebooks/             # Example notebooks
│   ├── api-examples.ipynb
│   └── translation-examples.ipynb
├── tests/                # Test files
├── config/               # Configuration files
├── data/                # Data files (gitignored)
└── requirements.txt     # Project dependencies
```

## Core Dependencies

- **Frontend**:
  - `streamlit`: Web interface
  - `python-dotenv`: Environment management

- **AI/ML**:
  - `openai==1.66.2`: GPT model integration
  - `langchain==0.3.20`: LLM framework
  - `langchain-core==0.3.44`: Core LangChain functionality
  - `langchain-community==0.3.19`: Community components
  - `langchain-openai==0.3.8`: OpenAI integration
  - `pinecone==5.4.2`: Vector database
  - `groq==0.19.0`: Alternative LLM provider

- **Translation**:
  - `google-cloud-translate`: Primary translation service
  - `deep-translator==1.11.4`: Backup translation

- **Data Processing**:
  - `pandas`: Data manipulation
  - `numpy`: Numerical operations
  - `nltk`: Text processing
  - `scikit-learn`: Machine learning utilities
  - `spacy`: NLP processing
  - `tiktoken==0.9.0`: Token counting

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

## Deployment

### Docker Deployment

The application can be deployed using Docker and Docker Compose. All deployment configurations are located in the `deployment` directory.

```bash
# Clone the repository
git clone https://github.com/Saikrishna-Paila/Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation.git
cd Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation

# Setup environment variables
cp deployment/.env.example deployment/.env
# Edit deployment/.env with your API keys

# Build and start the application
cd deployment
docker-compose up --build -d
```

### Resource Requirements

- Memory: 2GB minimum
- CPU: 1 core minimum
- Storage: 1GB minimum
- Ports: 8501 (Streamlit)

### Deployment Structure

```
deployment/
├── config/
│   └── deployment.yaml    # Deployment configuration
├── Dockerfile            # Docker image definition
├── docker-compose.yml    # Docker Compose configuration
├── deploy.sh            # Deployment script
├── .env.example         # Environment variables template
└── README.md           # Deployment documentation
```

### Health Checks

The application includes built-in health checks:
- Endpoint: `/_stcore/health`
- Interval: 30 seconds
- Timeout: 10 seconds
- Retries: 3

### Container Management

Use the deployment script for common operations:

```bash
cd deployment
./deploy.sh build    # Build the Docker image
./deploy.sh start    # Start the container
./deploy.sh stop     # Stop the container
./deploy.sh restart  # Restart the container
./deploy.sh status   # Check container status
```

For more detailed deployment instructions, see [deployment/README.md](deployment/README.md).
