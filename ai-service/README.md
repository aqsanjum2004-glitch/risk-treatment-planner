# AI Service — Risk Treatment Planner

## Overview
The AI microservice for the Risk Treatment Planner application. Built with Flask and powered by Groq LLaMA-3.3-70b model with ChromaDB RAG pipeline.

## Tech Stack
- Python 3.11
- Flask 3.x
- Groq API (LLaMA-3.3-70b-versatile)
- ChromaDB — Vector database
- Sentence Transformers — Text embeddings
- Flask-Limiter — Rate limiting

## Prerequisites
- Python 3.11+
- Groq API key (free at console.groq.com)

## Environment Variables
| Variable | Description | Required |
|---|---|---|
| GROQ_API_KEY | Your Groq API key | Yes |

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/tecsxpert/risk-treatment-planner.git
cd risk-treatment-planner/ai-service

### 2. Create .env file
GROQ_API_KEY=your_groq_api_key_here

### 3. Install dependencies
python -m pip install -r requirements.txt

### 4. Run the service
python app.py

### 5. Verify it's running
Visit http://localhost:5000/health

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| /health | GET | Service health check |
| /describe | POST | Generate risk description |
| /recommend | POST | Get 3 recommendations |
| /generate-report | POST | Generate full risk report |
| /query | POST | RAG question answering |
| /ingest | POST | Ingest document to ChromaDB |
| /analyse-document | POST | Analyse document for risks |
| /batch-process | POST | Process up to 20 risks |

## Developer
- Name: AQSA
- Role: AI Developer 1
- Sprint: 17 April - 18 May