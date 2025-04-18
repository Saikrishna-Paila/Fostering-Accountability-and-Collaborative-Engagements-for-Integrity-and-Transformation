#!/bin/bash

# Exit on error
set -e

echo "=== World Bank Project Deployment Script ==="
echo "This script will help you deploy the application to Google Cloud Run"

# Check prerequisites
command -v gcloud >/dev/null 2>&1 || { echo "Google Cloud SDK is required but not installed. Aborting." >&2; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "Docker is required but not installed. Aborting." >&2; exit 1; }

# Configuration
PROJECT_ID="world-bank-project-1745007891"
REGION="us-central1"
SERVICE_NAME="worldbank-app"
IMAGE_NAME="gcr.io/${PROJECT_ID}/${SERVICE_NAME}"

echo "=== Checking Google Cloud Authentication ==="
gcloud auth list

echo "=== Setting up Google Cloud Project ==="
gcloud config set project ${PROJECT_ID}

echo "=== Enabling Required APIs ==="
gcloud services enable \
  cloudbuild.googleapis.com \
  run.googleapis.com \
  containerregistry.googleapis.com \
  cloudmonitoring.googleapis.com

echo "=== Building Docker Image ==="
docker build --platform linux/amd64 -t ${IMAGE_NAME} .

echo "=== Pushing to Google Container Registry ==="
gcloud auth configure-docker
docker push ${IMAGE_NAME}

echo "=== Deploying to Cloud Run ==="
gcloud run deploy ${SERVICE_NAME} \
  --image ${IMAGE_NAME} \
  --platform managed \
  --region ${REGION} \
  --allow-unauthenticated \
  --memory=1Gi \
  --cpu=1 \
  --max-instances=10 \
  --concurrency=100 \
  --set-env-vars="OPENAI_API_KEY=${OPENAI_API_KEY},GROQ_API_KEY=${GROQ_API_KEY},GHANA_PINECONE_API_KEY=${GHANA_PINECONE_API_KEY},SIERRA_LEONE_PINECONE_API_KEY=${SIERRA_LEONE_PINECONE_API_KEY}"

echo "=== Deployment Complete ==="
echo "Getting service URL..."
gcloud run services describe ${SERVICE_NAME} \
  --region ${REGION} \
  --format="get(status.url)"

echo "=== Setting up Monitoring ==="
echo "Visit: https://console.cloud.google.com/run/detail/${REGION}/${SERVICE_NAME}/metrics" 