# 🚀 Hugging Face Sentiment Analyzer

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-005571?logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?logo=kubernetes&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)

**Analyze text sentiment with the power of Transformers & Warp Speed!** 🌌✨

A sophisticated, containerized API service that leverages a fine-tuned **DistilBERT** model to determine if text is `POSITIVE` or `NEGATIVE`. Now featuring a **Star Trek** themed frontend implementation for that futuristic feel! 🖖

---

## ✨ Features

-   🤖 **Advanced NLP**: Powered by `distilbert-base-uncased-finetuned-sst-2-english`.
-   ⚡ **High Performance**: Built on **FastAPI** for asynchronous, lightning-fast responses.
-   🎨 **Engaging Frontend**: A custom **Star Trek (LCARS style)** dashboard interface for testing predictions.
-   🐳 **Dockerized**: Production-ready multi-stage Docker builds.
-   ☸️ **Kubernetes Ready**: Complete K8s manifests for scalable deployment.

---

## 🚀 Quick Start (Docker)

The fastest way to engage the engage engines!

### 1. Build the Image
```bash
docker build -t sentiment-analyzer .
```

### 2. Launch the Container
```bash
docker run -p 8080:8080 sentiment-analyzer
```

### 3. Access the App
-   **Frontend UI**: [http://localhost:8080](http://localhost:8080) 🖥️
-   **API**: [http://localhost:8080](http://localhost:8080) 📡

---

## 🖥️ Frontend Interface

Experience the future of sentiment analysis! The application serves a **Star Trek themed** UI at the root path.

1.  Navigate to `http://localhost:8080` (or `http://localhost:8000` for local dev).
2.  Enter your text log.
3.  Click **"PREDICT"** (or "ENGAGE").
4.  Receive immediate analysis from the ship's computer.

---

## ☸️ Kubernetes Deployment

Deploy to your cluster with ease. Full documentation is available in [kubernetes/README.md](./kubernetes/README.md).

### Quick Deploy:
```bash
# 1. Update image in deployment.yaml
# 2. Apply manifests
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

# 3. (Optional) Apply Ingress
kubectl apply -f kubernetes/ingress.yaml
```

**Port Forwarding (Testing):**
```bash
kubectl port-forward service/hf-sentiment-service 8080:8080 8000:8000
```
Then access at `http://localhost:8000`.

---

## 🛠️ Local Development

For those who prefer to work in the engineering bay:

1.  **Create Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Server**:
    ```bash
    uvicorn app:app --reload
    ```
    Access at `http://127.0.0.1:8000` (API & Frontend).

---

## 📡 API Usage

### Health Check ("Status Report")
`GET /health` or `GET /` (on port 8080)
```json
{"status": "ok", "model": "distilbert-base-uncased-finetuned-sst-2-english"}
```

### Predict Sentiment ("Analysis")
`POST /predict`

**Request:**
```bash
curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "The warp drive is functioning perfectly!"}'
```

**Response:**
```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```

---

_Live long and prosper._ 🖖
