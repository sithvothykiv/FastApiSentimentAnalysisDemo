from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import mlflow  

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

app = FastAPI()


# @app.post("/analyze-sentiment")
# async def analyze_sentiment(text_input: TextInput):
#     mlflow.start_run()
#     mlflow.set_tracking_uri("http://localhost:5001")
#     result = sentiment_pipeline(text_input.text)
#     mlflow.log_param("text", text_input.text)
#     mlflow.log_metric("sentiment", result[0]['label'])
#     mlflow.log_metric("confidence", result[0]['score'])
#     mlflow.end_run()
#     return {"sentiment": result[0]['label'], "confidence": result[0]['score']}

@app.post("/analyze-sentiment")
async def analyze_sentiment(text_input: TextInput):
    try:
        mlflow.set_tracking_uri("http://localhost:5001")
        
        with mlflow.start_run():
            result = sentiment_pipeline(text_input.text)
            
            # Log parameters and metrics
            mlflow.log_param("text", text_input.text)
            mlflow.log_param("model", "sentiment-analysis")
            
            # Convert sentiment label to numeric for MLflow metric logging
            sentiment_score = 1 if result[0]['label'] == 'POSITIVE' else 0
            mlflow.log_metric("sentiment_score", sentiment_score)
            mlflow.log_metric("confidence", result[0]['score'])
            
            # Log the actual sentiment as a tag instead of metric
            mlflow.set_tag("sentiment_label", result[0]['label'])
        
        return {"sentiment": result[0]['label'], "confidence": result[0]['score']}
    
    except Exception as e:
        # Return error details for debugging
        return {"error": str(e), "sentiment": "UNKNOWN", "confidence": 0.0}

@app.get("/")
async def root():
    return {"message": "Welcome to the Sentiment Analysis API. Use the /analyze-sentiment endpoint to analyze text."}
