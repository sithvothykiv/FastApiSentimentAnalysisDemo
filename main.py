from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Define the request body schema
class TextInput(BaseModel):
    text: str

app = FastAPI()

# Define the sentiment analysis endpoint
@app.post("/analyze-sentiment")
async def analyze_sentiment(text_input: TextInput):
    result = sentiment_pipeline(text_input.text)
    return {"sentiment": result[0]['label'], "confidence": result[0]['score']}

@app.get("/")
async def root():
    return {"message": "Welcome to the Sentiment Analysis API. Use the /analyze-sentiment endpoint to analyze text."}
