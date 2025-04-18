# Deployment

This directory contains all deployment-related files and configurations for the JurisAI application.

## Directory Structure

```
deployment/
├── config/
│   └── deployment.yaml    # Deployment configuration
├── Dockerfile            # Docker image definition
├── docker-compose.yml    # Docker Compose configuration
├── deploy.sh            # Deployment script
├── .env.example         # Environment variables template
└── README.md           # This file
```

## Quick Start

1. Copy the environment template:
```bash
cp .env.example .env
# Edit .env with your API keys and configurations
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build -d
```

3. Check the application:
```bash
docker-compose ps
curl http://localhost:8501/_stcore/health
```

## Configuration

- `config/deployment.yaml`: Contains deployment settings
- `docker-compose.yml`: Defines the application stack
- `.env`: Environment variables (copy from .env.example)

## Deployment Script

The `deploy.sh` script provides commands for:
- Building the Docker image
- Running the container
- Managing deployments
- Health checks

Usage:
```bash
./deploy.sh [build|start|stop|restart|status]
```

## Resource Requirements

- Memory: 2GB minimum
- CPU: 1 core minimum
- Storage: 1GB minimum
- Ports: 8501 (Streamlit) 