# Install Python FastApi
```bash
pip install fastapi uvicorn
```

# Pretrain Model
### Assuming you have a pretrained sentiment analysis model (e.g., using transformers library from Hugging Face):
## Install the transformers library:
```bash
pip install transformers
```

## Run the FastAPI app using Uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000.

Access API docs at http://127.0.0.1:8000/docs.

## Use the /analyze-sentiment endpoint to test the API by providing a JSON payload like:


```json
{
  "text": "I love using FastAPI!"
}
```

### Using curl:
```bash
curl -X POST "http://127.0.0.1:8000/analyze-sentiment" -H "Content-Type: application/json" -d '{"text": "I love using FastAPI!"}'
```

### Using Python requests:
```py
import requests

url = "http://127.0.0.1:8000/analyze-sentiment"
payload = {"text": "I love using FastAPI!"}
response = requests.post(url, json=payload)
print(response.json())

```