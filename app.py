# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


# --- 1. Define the Input/Output Schema ---
class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    score: float


# --- 2. Load Model Once (Optimization) ---
# This model is a fine-tuned DistilBERT for sentiment analysis
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

# Initialize the pipeline for text classification
# This will download the model and tokenizer upon startup
try:
    classifier = pipeline("sentiment-analysis", model=MODEL_NAME)
    print(f"Model {MODEL_NAME} loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    classifier = None


# --- 3. Initialize FastAPI App ---
app = FastAPI(
    title="Hugging Face Sentiment Analyzer",
    description="A service to classify text sentiment using DistilBERT.",
)

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    return FileResponse("static/index.html")


@app.get("/health")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "model": MODEL_NAME}


@app.post("/predict", response_model=PredictionOut)
async def predict_sentiment(item: TextIn):
    """
    Performs sentiment prediction on the input text.
    """
    if not classifier:
        raise Exception("Model failed to load.")

    # Get prediction results (usually returns a list of dictionaries)
    result = classifier(item.text)[0]

    # Return structured prediction data
    return PredictionOut(label=result["label"], score=result["score"])


# To run locally without Docker for testing:
# uvicorn app:app --reload
