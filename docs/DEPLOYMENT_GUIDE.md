# World Bank Project Deployment Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Setup](#local-setup)
3. [Docker Setup](#docker-setup)
4. [Google Cloud Setup](#google-cloud-setup)
5. [Building and Deploying](#building-and-deploying)
6. [Monitoring and Maintenance](#monitoring-and-maintenance)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

1. **Install Required Tools**
```bash
# Install Google Cloud SDK
brew install google-cloud-sdk  # For macOS
# OR visit https://cloud.google.com/sdk/docs/install for other OS

# Install Docker Desktop
# Download from https://www.docker.com/products/docker-desktop
```

2. **Required API Keys**
```bash
# Add these to your .env file
OPENAI_API_KEY="your-openai-key"
GROQ_API_KEY="your-groq-key"
GHANA_PINECONE_API_KEY="your-ghana-pinecone-key"
SIERRA_LEONE_PINECONE_API_KEY="your-sierra-leone-pinecone-key"
```

## Local Setup

1. **Clone and Setup Project**
```bash
# Clone repository
git clone <repository-url>
cd World_Bank_Project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Unix/macOS
# OR
.\venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt
```

2. **Test Locally**
```bash
# Run Streamlit app
streamlit run app.py
```

## Docker Setup

1. **Build Docker Image Locally**
```bash
# For testing locally
docker build -t worldbank-app .

# Test the container locally
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=${OPENAI_API_KEY} \
  -e GROQ_API_KEY=${GROQ_API_KEY} \
  -e GHANA_PINECONE_API_KEY=${GHANA_PINECONE_API_KEY} \
  -e SIERRA_LEONE_PINECONE_API_KEY=${SIERRA_LEONE_PINECONE_API_KEY} \
  worldbank-app
```

## Google Cloud Setup

1. **Initialize Google Cloud**
```bash
# Login to Google Cloud
gcloud auth login

# Set project
gcloud config set project <your-project-id>

# Enable required APIs
gcloud services enable \
  cloudbuild.googleapis.com \
  run.googleapis.com \
  containerregistry.googleapis.com \
  cloudmonitoring.googleapis.com
```

2. **Setup Billing**
```bash
# List billing accounts
gcloud billing accounts list

# Link billing account
gcloud billing projects link <your-project-id> \
  --billing-account=<your-billing-account>

# Create budget alert
gcloud billing budgets create \
  --billing-account=<your-billing-account> \
  --display-name="WorldBank App Budget" \
  --budget-amount=50USD \
  --threshold-rule=percent=0.5 \
  --threshold-rule=percent=0.75 \
  --threshold-rule=percent=0.9 \
  --threshold-rule=percent=1.0
```

## Building and Deploying

1. **Build for Cloud Run**
```bash
# Configure Docker for GCP
gcloud auth configure-docker

# Build AMD64 image for Cloud Run
docker build --platform linux/amd64 \
  -t gcr.io/<your-project-id>/worldbank-app .

# Push to Google Container Registry
docker push gcr.io/<your-project-id>/worldbank-app
```

2. **Deploy to Cloud Run**
```bash
# Deploy with environment variables
gcloud run deploy worldbank-app \
  --image gcr.io/<your-project-id>/worldbank-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory=1Gi \
  --cpu=1 \
  --max-instances=10 \
  --concurrency=100 \
  --set-env-vars="OPENAI_API_KEY=${OPENAI_API_KEY},GROQ_API_KEY=${GROQ_API_KEY},GHANA_PINECONE_API_KEY=${GHANA_PINECONE_API_KEY},SIERRA_LEONE_PINECONE_API_KEY=${SIERRA_LEONE_PINECONE_API_KEY}"
```

## Monitoring and Maintenance

1. **View Service Status**
```bash
# Get service URL
gcloud run services describe worldbank-app \
  --region us-central1 \
  --format="get(status.url)"

# Check service health
gcloud run services describe worldbank-app \
  --region us-central1 \
  --format="table(status.conditions[].type,status.conditions[].status)"
```

2. **Monitor Resources**
```bash
# View logs
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=worldbank-app" --limit=10

# View metrics
# Visit Cloud Run service metrics in Google Cloud Console
```

3. **Update Service**
```bash
# Update resources
gcloud run services update worldbank-app \
  --region us-central1 \
  --memory=1Gi \
  --cpu=1 \
  --max-instances=10 \
  --concurrency=100

# Update environment variables
gcloud run services update worldbank-app \
  --region us-central1 \
  --set-env-vars="NEW_VAR=value"
```

## Troubleshooting

1. **Common Issues**

- **Image Build Fails**:
  ```bash
  # Check Docker logs
  docker logs $(docker ps -lq)
  ```

- **Deployment Fails**:
  ```bash
  # Check service logs
  gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=worldbank-app" --limit=10
  ```

- **Service Unavailable**:
  ```bash
  # Check service status
  gcloud run services describe worldbank-app --region us-central1
  ```

2. **Resource Management**

- **View Current Usage**:
  ```bash
  # Check resource utilization
  gcloud monitoring metrics list | grep "cloud_run"
  ```

- **Cost Management**:
  ```bash
  # View current budget
  gcloud billing budgets list --billing-account=<your-billing-account>
  ```

## Important URLs

1. **Service URL**: Visit your deployed Cloud Run service URL
2. **Monitoring Dashboard**: Access through Google Cloud Console
3. **Logs**: Access through Google Cloud Console
4. **Billing**: Access through Google Cloud Console

## Security Notes

1. Never commit `.env` file
2. Rotate API keys regularly
3. Monitor usage and set up alerts
4. Use secure methods for sharing credentials
5. Keep Docker and dependencies updated
6. Use environment variables for all sensitive information
7. Implement proper access controls and IAM policies

## Maintenance Schedule

1. **Daily**:
   - Check service health
   - Monitor logs for errors
   - Review request patterns

2. **Weekly**:
   - Review performance metrics
   - Check resource utilization
   - Update documentation if needed

3. **Monthly**:
   - Review and optimize costs
   - Rotate API keys
   - Update dependencies
   - Review security settings 