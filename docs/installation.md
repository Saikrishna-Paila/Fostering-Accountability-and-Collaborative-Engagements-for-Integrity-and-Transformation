# Installation Guide

## Prerequisites

Before installing JurisAI, ensure you have:

- Python 3.9 or higher
- pip (Python package installer)
- Git

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/jurisai.git
   cd jurisai
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package and dependencies:
   ```bash
   pip install -e ".[docs]"
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your API credentials.

## API Credentials Setup

For detailed API setup instructions, see [API Credentials Guide](api-credentials.md).

## Development Setup

1. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

2. Install documentation dependencies:
   ```bash
   pip install -e ".[docs]"
   ``` 