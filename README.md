# FastApi Sentiment Analysis Demo with MLFlow


## Install Python FastApi
```bash
pip install fastapi uvicorn
```

## Pretrain Model
Assuming you have a pretrained sentiment analysis model (e.g., using transformers library from Hugging Face):
### Install the transformers library:
```bash
pip install transformers
pip install "numpy<2.0.0" --force-reinstall

```

### Run the FastAPI app using Uvicorn:
```bash
uvicorn main:app --reload
```

- The API will be available at http://127.0.0.1:8000.
- Access API docs at http://127.0.0.1:8000/docs.
- Use the /analyze-sentiment endpoint to test the API by providing a JSON payload like:


```json
{
  "text": "I love using FastAPI!"
}
```

### Testing Using curl:
```bash
curl -X POST "http://127.0.0.1:8000/analyze-sentiment" -H "Content-Type: application/json" -d '{"text": "I love using FastAPI!"}'

curl -X GET "http://127.0.0.1:8000" -H "Content-Type: application/json"
```

# Using Mac M Chip:
## Issue
https://stackoverflow.com/questions/70723757/arch-x86-64-and-arm64e-is-available-but-python3-is-saying-incompatible-architect


```bash
arch -arm64 pip install fastapi uvicorn
arch -arm64 pip install fastapi uvicorn

# Create a new virtual environment using the system Python
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Clear pip cache to avoid cached incompatible packages
pip cache purge

# Upgrade pip
pip install --upgrade pip

# Install packages one by one to catch any issues
arch -arm64 pip install --no-cache-dir fastapi
arch -arm64 pip install --no-cache-dir uvicorn
arch -arm64 pip install --no-cache-dir pydantic
arch -arm64 pip install --no-cache-dir transformers
arch -arm64 pip install --no-cache-dir torch
arch -arm64 pip install --no-cache-dir numpy
arch -arm64 pip install --no-cache-dir mlflow

# Run app
arch -arm64 uvicorn main:app --reload

```