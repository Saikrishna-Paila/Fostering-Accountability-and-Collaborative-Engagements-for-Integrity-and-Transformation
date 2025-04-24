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

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technical Architecture](#technical-architecture)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

JurisAI is an intelligent legal assistant that provides accessible legal guidance for Ghana and Sierra Leone. Built with Streamlit and powered by advanced language models, it offers legal information in multiple languages to bridge the accessibility gap in legal services.

### Quick Links
- 🌐 [Live Demo](https://jurisai-1358123759.us-central1.run.app)
- 📚 [Documentation](docs/)
- 🤝 [Contributing Guidelines](CONTRIBUTING.md)
- 📜 [Code of Conduct](CODE_OF_CONDUCT.md)
- ⚖️ [License](LICENSE)

## Features

### Multilingual Support
- 🇬🇭 Ghana: English and Akan (Twi) translation
- 🇸🇱 Sierra Leone: English and Krio translation
- Real-time language switching
- Culturally appropriate translations

### AI-powered Legal Assistance
- Interactive legal question answering
- Context-aware responses using LangChain
- Legal document analysis and summarization
- Pinecone vector search for relevant legal documents

### User Interface
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

## Installation

### Prerequisites

1. **Python Environment**:
   - Python 3.9 or higher
   - pip (Python package installer)

2. **Required API Keys**:
   - OpenAI API Key (for GPT models)
   - Pinecone API Key (for vector search)
   - Google Cloud Translation API Key
   - Groq API Key (optional)

### Setup Steps

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
# Edit .env with your API keys
```

## Project Structure

```
.
├── src/
│   ├── jurisai/           # Main application package
│   ├── template/          # Template utilities
│   └── worldbank/         # World Bank specific modules
├── deployment/            # Deployment configurations
│   ├── config/           # Deployment config files
│   ├── Dockerfile        # Docker image definition
│   ├── docker-compose.yml # Docker Compose config
│   ├── deploy.sh         # Deployment script
│   └── README.md         # Deployment documentation
├── docs/                 # Documentation files
├── notebooks/            # Jupyter notebooks
├── tests/               # Test suite
├── config/              # Application configurations
├── data/               # Data files (gitignored)
├── secrets/            # Secret files (gitignored)
├── .github/            # GitHub workflows and templates
├── requirements.txt    # Python dependencies
├── pyproject.toml     # Project metadata and tools config
├── .pre-commit-config.yaml # Pre-commit hooks config
├── .env.example       # Example environment variables
├── LICENSE           # Mozilla Public License
├── CONTRIBUTING.md   # Contribution guidelines
├── CODE_OF_CONDUCT.md # Code of conduct
├── CITATION.cff      # Citation information
└── NOTICE           # Third-party notices
```

The project follows a modular structure with clear separation of concerns:
- `src/jurisai/`: Core application logic and components
- `src/template/`: Reusable template utilities
- `src/worldbank/`: World Bank specific implementations
- `deployment/`: All deployment-related configurations and scripts
- `docs/`: Project documentation and guides
- `notebooks/`: Example notebooks and data analysis
- `tests/`: Automated test suite
- `config/`: Application configuration files
- `data/`: Data storage (not tracked in git)
- `secrets/`: Sensitive configuration (not tracked in git)

## Dependencies

### Core Components
- **Frontend**:
  - `streamlit`: Web interface
  - `python-dotenv`: Environment management

### AI and ML
- `openai==1.66.2`: GPT model integration
- `langchain==0.3.20`: LLM framework
- `langchain-core==0.3.44`: Core functionality
- `langchain-community==0.3.19`: Community components
- `langchain-openai==0.3.8`: OpenAI integration
- `pinecone==5.4.2`: Vector database
- `groq==0.19.0`: Alternative LLM provider

### Translation
- `google-cloud-translate`: Primary translation
- `deep-translator==1.11.4`: Backup translation

### Data Processing
- `pandas`: Data manipulation
- `numpy`: Numerical operations
- `nltk`: Text processing
- `scikit-learn`: ML utilities
- `spacy`: NLP processing
- `tiktoken==0.9.0`: Token counting

## Deployment

### Quick Start
```bash
# Clone repository
git clone https://github.com/Saikrishna-Paila/Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation.git
cd Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation

# Setup environment
cp deployment/.env.example deployment/.env
cd deployment
docker-compose up --build -d
```

### Resource Requirements
- Memory: 2GB minimum
- CPU: 1 core minimum
- Storage: 1GB minimum
- Ports: 8501 (Streamlit)

### Container Management
```bash
./deploy.sh build    # Build image
./deploy.sh start    # Start container
./deploy.sh stop     # Stop container
./deploy.sh restart  # Restart container
./deploy.sh status   # Check status
```

For detailed deployment instructions, see [deployment/README.md](deployment/README.md).

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the Mozilla Public License - see the [LICENSE](LICENSE) file for details.

## Project Team

This project is a collaborative effort led by the World Bank and George Washington University (GWU) Master's students.

**Team Lead – World Bank Group**  
- **Tatsuya Iwasaki**

**Team Members – GWU**  
- **Saikrishna Paila**  
- **Aneri Patel**  
- **Phani Vishnu Addepalli**  
- **Pranideep Meka**

## Acknowledgments

- World Bank Group
- Ghana Legal Information Institute (GhaLII)
- Sierra Leone Legal Information Institute (SierraLII)
- GWU Master's Students

---

**Note**: This project is maintained by GWU Master's Students for Global Legal Access. Country borders or names do not necessarily reflect the World Bank Group's official position.
