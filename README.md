# Hugging Face Sentiment Analyzer

A simple, containerized API service that uses a fine-tuned DistilBERT model to classify text sentiment. Built with FastAPI and Hugging Face Transformers.

## Features

-   **Sentiment Analysis**: Classifies text as "POSITIVE" or "NEGATIVE" with a confidence score.
-   **Model**: Uses `distilbert-base-uncased-finetuned-sst-2-english` (optimized implementation).
-   **API**: Fast and asynchronous endpoints using FastAPI.
-   **Dockerized**: Ready for deployment with a multi-stage Dockerfile.

## Prerequisites

-   Docker
-   Python 3.10+ (for local development)

## Installation

### Method 1: Docker (Recommended)

1.  **Build the Docker image:**

    ```bash
    docker build -t sentiment-analyzer .
    ```

2.  **Run the container:**

    ```bash
    docker run -p 8080:8080 sentiment-analyzer
    ```

    The API will be available at `http://localhost:8080`.

### Method 2: Local Setup

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**

    ```bash
    uvicorn app:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

## API Usage

### Health Check

**Endpoint:** `GET /`

```bash
curl http://localhost:8080/
```

**Response:**
```json
{"status": "ok", "model": "distilbert-base-uncased-finetuned-sst-2-english"}
```

### Predict Sentiment

**Endpoint:** `POST /predict`

**Request Body:**

```json
{
  "text": "I love using this new tool! It's fantastic."
}
```

**Example:**

```bash
curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love using this new tool! It is fantastic."}'
```

**Response:**

```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```
