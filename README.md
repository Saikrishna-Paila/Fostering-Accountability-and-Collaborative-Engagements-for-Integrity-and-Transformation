# JurisAI: Legal Assistant for Ghana and Sierra Leone 🇬🇭 🇸🇱

[![Documentation](https://img.shields.io/badge/docs-jupyter%20book-blue.svg)](https://worldbank.github.io/jurisai)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Mozilla-blue.svg)](LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jurisai.streamlit.app)
[![GitHub Actions](https://github.com/worldbank/jurisai/workflows/documentation/badge.svg)](https://github.com/worldbank/jurisai/actions)

## Overview

JurisAI is an intelligent legal assistant that provides accurate and accessible legal guidance for Ghana and Sierra Leone. The project aims to bridge the legal information gap by leveraging advanced AI technologies to make legal information more accessible to the public.

### Key Features
- **Multilingual Support**:
  - 🇬🇭 Ghana: English and Akan (Twi) with cultural context
  - 🇸🇱 Sierra Leone: English and Krio with local legal terminology
- **AI-powered Legal Analysis**:
  - Document summarization and key point extraction
  - Legal precedent matching
  - Contextual question answering
- **Real-time Translation**:
  - Bidirectional translation between supported languages
  - Legal terminology preservation
  - Cultural context awareness
- **User-friendly Interface**:
  - Intuitive web-based interface
  - Mobile-responsive design
  - Accessibility features

## 🚀 Getting Started

### Prerequisites

Before installing JurisAI, ensure you have:

1. **Python Environment**:
   - Python 3.9 or higher
   - pip (Python package installer)
   - Virtual environment management (venv or conda)

2. **Version Control**:
   - Git 2.x or higher
   - GitHub account for contributions

3. **API Keys**:
   - OpenAI API Key (for GPT-4 and GPT-3.5 models)
     - Required for: Legal analysis, document processing
     - [Get API Key](https://platform.openai.com/api-keys)
   - Google Cloud Translation API
     - Required for: Language translation
     - [Setup Instructions](https://cloud.google.com/translate/docs/setup)
   - Pinecone API Key
     - Required for: Vector similarity search
     - [Get API Key](https://www.pinecone.io/)

### Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/worldbank/jurisai.git
cd jurisai
```

2. **Set Up Python Environment**:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Unix/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Verify Python version
python --version  # Should be 3.9 or higher
```

3. **Install Dependencies**:
```bash
# For users (basic installation)
pip install -r requirements.txt

# For developers (includes testing and documentation tools)
pip install -e ".[dev,docs]"

# Verify installation
python -c "import jurisai; print(jurisai.__version__)"
```

4. **Configure Environment**:
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API credentials
# Required variables:
# - OPENAI_API_KEY
# - GOOGLE_CLOUD_API_KEY
# - PINECONE_API_KEY
# - PINECONE_ENVIRONMENT
```

For detailed setup instructions, see our [Installation Guide](docs/installation.md).

## 📖 Documentation

Our comprehensive documentation is built using Jupyter Book, providing both API references and usage guides.

### Building Documentation Locally

1. **Install Documentation Dependencies**:
```bash
pip install -e ".[docs]"
```

2. **Build the Documentation**:
```bash
# Generate HTML documentation
jupyter-book build . --config docs/_config.yml --toc docs/_toc.yml

# The built documentation will be in _build/html/
# Open _build/html/index.html in your browser
```

3. **Live Preview** (optional):
```bash
# Install live server
npm install -g live-server

# Start live preview
live-server _build/html
```

### Documentation Structure
- **User Guide**: Basic concepts and getting started
- **API Reference**: Detailed function and class documentation
- **Examples**: Jupyter notebooks with real-world examples
- **Contributing**: Guidelines for developers
- **Security**: Security best practices and guidelines

### Publishing Documentation

1. **Enable GitHub Actions**:
   - Navigate to repository Settings > Actions > General
   - Under "Workflow permissions", select "Read and write permissions"
   - Save the changes

2. **Enable GitHub Pages**:
   - Go to repository Settings > Pages
   - Under "Build and deployment":
     - Source: Deploy from a branch
     - Branch: gh-pages / root
   - Save the changes

The documentation will automatically build and deploy when:
- Changes are pushed to the main branch
- Pull requests are merged into main
- Manual workflow dispatch is triggered

## 🌟 Features

### Core Functionality

#### Legal Document Analysis
- **Document Processing**:
  - PDF, Word, and plain text support
  - OCR for scanned documents
  - Structure preservation
- **Analysis Capabilities**:
  - Key point extraction
  - Legal citation identification
  - Precedent matching
  - Summary generation

#### Multilingual Support
- **Ghana** 🇬🇭
  - English (Primary legal language)
  - Akan/Twi (Most widely spoken local language)
  - Context-aware translations
  - Legal terminology mapping
- **Sierra Leone** 🇸🇱
  - English (Official legal language)
  - Krio (Lingua franca)
  - Cultural context preservation
  - Legal concept mapping

#### Vector Search
- **Document Retrieval**:
  - Semantic similarity matching
  - Multilingual query support
  - Relevance ranking
- **Performance**:
  - Sub-second query time
  - High accuracy matching
  - Scalable to millions of documents

#### Real-time Translation
- **Features**:
  - Bidirectional translation
  - Legal terminology preservation
  - Cultural context awareness
- **Quality Assurance**:
  - Professional review process
  - Continuous improvement
  - User feedback integration

#### Interactive UI
- **Web Interface**:
  - Responsive design
  - Mobile-friendly
  - Accessibility compliant
- **Features**:
  - Document upload
  - Real-time translation
  - Interactive Q&A
  - Search functionality

### Technical Features

#### Backend Architecture
- **FastAPI Framework**:
  - Async request handling
  - OpenAPI documentation
  - Type checking
  - Request validation

#### Frontend Implementation
- **Streamlit**:
  - Interactive components
  - Real-time updates
  - Data visualization
  - File handling

#### AI Integration
- **LangChain**:
  - Document processing
  - LLM orchestration
  - Prompt management
  - Chain of thought reasoning

#### Vector Search
- **Pinecone**:
  - Vector similarity search
  - Real-time updates
  - Scalable storage
  - High availability

#### Translation Service
- **Google Cloud Translation**:
  - Neural machine translation
  - Language detection
  - Glossary support
  - Batch translation

## 📚 Project Structure

```
jurisai/
├── src/                 # Source code
│   └── jurisai/        # Main package
│       ├── __init__.py # Package initialization
│       ├── app.py      # Streamlit application
│       ├── api/        # FastAPI endpoints
│       ├── models/     # Data models
│       ├── services/   # Business logic
│       └── utils/      # Helper functions
├── docs/               # Documentation
│   ├── _config.yml    # Jupyter Book config
│   ├── _toc.yml       # Table of contents
│   ├── images/        # Documentation images
│   ├── api/           # API documentation
│   ├── guides/        # User guides
│   └── examples/      # Usage examples
├── notebooks/         # Jupyter notebooks
│   ├── api-examples.ipynb     # API usage examples
│   ├── translation-examples.ipynb  # Translation examples
│   └── analysis-examples.ipynb    # Analysis examples
├── tests/            # Test files
│   ├── unit/        # Unit tests
│   ├── integration/ # Integration tests
│   └── e2e/         # End-to-end tests
├── data/             # Data files (gitignored)
│   ├── raw/         # Raw data
│   ├── processed/   # Processed data
│   └── models/      # Model files
├── config/           # Configuration files
│   ├── app.yaml     # Application config
│   └── logging.yaml # Logging config
├── scripts/         # Utility scripts
├── pyproject.toml   # Python package config
├── requirements.txt # Direct dependencies
└── .env.example     # Template for environment variables
```

## 🤝 Contributing

We welcome contributions from developers, legal experts, and translators! Please follow these steps:

### Getting Started

1. **Review Documentation**:
   - [Contributing Guide](docs/contributing.md)
   - [Code of Conduct](docs/code-of-conduct.md)
   - [Development Setup](docs/development.md)

2. **Fork and Clone**:
   ```bash
   # Fork the repository on GitHub
   git clone https://github.com/YOUR-USERNAME/jurisai.git
   cd jurisai
   git remote add upstream https://github.com/worldbank/jurisai.git
   ```

3. **Create Feature Branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```

4. **Make Changes**:
   - Write clean, documented code
   - Follow our coding standards
   - Add tests for new features
   - Update documentation

5. **Test Your Changes**:
   ```bash
   # Run tests
   pytest
   
   # Check code style
   black .
   flake8
   
   # Run type checking
   mypy src/
   ```

6. **Submit Changes**:
   ```bash
   git commit -m "Add amazing feature"
   git push origin feature/AmazingFeature
   ```

7. **Open Pull Request**:
   - Use the PR template
   - Reference related issues
   - Provide clear description
   - Wait for review

### Development Guidelines

- Follow [PEP 8](https://pep8.org/) style guide
- Write [docstrings](https://peps.python.org/pep-0257/) for all functions
- Maintain test coverage above 80%
- Update documentation for new features
- Use type hints for better code quality

## 🔒 Security

### API Security

- **Authentication**:
  - API key validation
  - JWT token authentication
  - Rate limiting

- **Data Protection**:
  - Encryption at rest
  - Secure transmission (HTTPS)
  - Input sanitization

- **Best Practices**:
  - Environment variables for secrets
  - Regular security updates
  - Access control implementation
  - API endpoint protection

### Guidelines

1. **API Keys**:
   - Store in `.env` file
   - Never commit secrets
   - Rotate keys regularly

2. **Access Control**:
   - Implement role-based access
   - Validate all requests
   - Log security events

3. **Updates**:
   - Regular dependency updates
   - Security patch application
   - Vulnerability scanning

For detailed security guidelines, see [API Credentials Guide](docs/api-credentials.md).

## 📝 Citation

If you use JurisAI in your research, please cite:

```bibtex
@software{jurisai2024,
  title     = {JurisAI: Legal Assistant for Ghana and Sierra Leone},
  author    = {{JurisAI Team}},
  year      = {2024},
  url       = {https://github.com/worldbank/jurisai},
  version   = {1.0.0},
  abstract  = {An intelligent legal assistant providing multilingual legal guidance for Ghana and Sierra Leone.}
}
```

## 📄 License

This project is licensed under the Mozilla Public License - see the [LICENSE](LICENSE) file for details.

### License Terms

The Mozilla Public License (MPL) is a copyleft license that:
- **Permissions**:
  - Commercial use
  - Modification
  - Distribution
  - Private use
  
- **Requirements**:
  - Source code disclosure
  - License and copyright notice
  - Same license for modifications
  
- **Additional Terms**:
  - Patent rights included
  - Trademark protection
  - Liability limitations
  - No warranty provided

## 🙏 Acknowledgments

### Organizations
- **World Bank**
  - Legal document access
  - Project support and guidance
  - Infrastructure resources

- **Legal Institutions**
  - Ghana Legal Information Institute (GhaLII)
    - Legal resources and validation
    - Domain expertise
  - Sierra Leone Legal Information Institute (SierraLII)
    - Legal documentation
    - Local context expertise

### Technology Partners
- **Development Data Group**
  - Project template
  - Technical guidance
  - Maintenance support

- **Service Providers**
  - OpenAI for GPT models
  - Google Cloud for translation
  - Pinecone for vector search

### Community
- Contributors and maintainers
- Legal experts and reviewers
- Translation specialists
- User feedback providers

---

**Note**: Country borders or names do not necessarily reflect the World Bank Group's official position. All maps are for illustrative purposes and do not imply the expression of any opinion on the part of the World Bank.
