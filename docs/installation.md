# Installation Guide

## Prerequisites

Before installing JurisAI, ensure you have:

- Python 3.9 or higher
- pip (Python package installer)
- Git
- Docker (optional, for containerized deployment)

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Saikrishna-Paila/Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation.git
   cd Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your API credentials:
   - OpenAI API Key
   - Pinecone API Key
   - Google Cloud Translation API Key
   - Groq API Key (optional)

## API Credentials

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Create a new API key
5. Add to `.env`: `OPENAI_API_KEY=your_key_here`

### Pinecone API Key
1. Sign up at [Pinecone](https://www.pinecone.io/)
2. Create a new project
3. Get your API key and environment
4. Add to `.env`:
   ```
   PINECONE_API_KEY=your_key_here
   PINECONE_ENVIRONMENT=your_environment
   ```

### Google Cloud Translation API
1. Create a [Google Cloud Project](https://console.cloud.google.com/)
2. Enable Cloud Translation API
3. Create service account and download JSON key
4. Add to `.env`: `GOOGLE_APPLICATION_CREDENTIALS=path_to_json_key`

## Development Setup

1. Install pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Docker Installation (Optional)

For containerized deployment:

1. Build the Docker image:
   ```bash
   cd deployment
   docker-compose build
   ```

2. Start the container:
   ```bash
   docker-compose up -d
   ```

For more detailed deployment instructions, see [Deployment Guide](../deployment/README.md).

## Troubleshooting

If you encounter any issues during installation:

1. Ensure all prerequisites are installed and up to date
2. Check that all environment variables are properly set
3. Verify API credentials are valid
4. For Docker issues, ensure Docker daemon is running

For additional help, please [open an issue](https://github.com/Saikrishna-Paila/Fostering-Accountability-and-Collaborative-Engagements-for-Integrity-and-Transformation/issues) on our GitHub repository. 