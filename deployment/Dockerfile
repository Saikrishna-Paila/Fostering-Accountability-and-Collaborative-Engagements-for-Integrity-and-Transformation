FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user first
RUN useradd -m -u 1000 streamlit

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip cache purge

# Verify Streamlit installation
RUN streamlit --version

# Create .streamlit directory and copy config
RUN mkdir -p /app/.streamlit
COPY config.toml /app/.streamlit/config.toml

# Copy application files
COPY . .

# Copy GCP credentials
COPY secrets/jurisai-gcp-translation-key.json /app/secrets/jurisai-gcp-translation-key.json
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/secrets/jurisai-gcp-translation-key.json"


# Set correct permissions
RUN chown -R streamlit:streamlit /app

# Switch to non-root user
USER streamlit

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
ENV STREAMLIT_SERVER_ENABLE_CORS=false
ENV STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_FILE_WATCHER_TYPE=none
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV PORT=8501

# Environment variables for API keys (to be set at runtime)
ENV GROQ_API_KEY=""
ENV OPENAI_API_KEY=""
ENV SIERRA_LEONE_PINECONE_API_KEY=""
ENV GHANA_PINECONE_API_KEY=""

# Expose the port
EXPOSE 8501

# Create a startup script with logging and checks
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
echo "=== Environment Information ==="\n\
echo "Current directory: $(pwd)"\n\
echo "Files in current directory:"\n\
ls -la\n\
echo "PORT: $PORT"\n\
echo "Python version:"\n\
python --version\n\
\n\
echo "=== Starting Streamlit ==="\n\
exec streamlit run app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false \
    --browser.serverAddress=0.0.0.0 \
    --theme.primaryColor="#c59d4f" \
    --theme.backgroundColor="#1a1f26" \
    --theme.secondaryBackgroundColor="#2b3240" \
    --theme.textColor="#e6e6ea" \
    --theme.font="serif" \
    --logger.level=info \
    --logger.messageFormat="%(asctime)s %(levelname)s %(message)s"' > /app/start.sh && \
    chmod +x /app/start.sh

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Use the startup script
CMD ["/app/start.sh"] 