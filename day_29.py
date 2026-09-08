from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

class ModelInferenceRequest(BaseModel):
    feature_vector: list[float] = Field(..., min_length = 2, max_length = 5, description = "Input feature values")
    model_version: str = Field(..., min_length = 2, max_length = 10)

def verify_api_key(x_api_key: str = Header(..., description = "Internal system access token")):
    expected_token = "mle-secret-token-2026"

    if x_api_key != expected_token:
        raise HTTPException(status_code = 401, detail = "Unauthorized: Invalid API Key")

    return x_api_key

@app.post("/predict")

def run_prediction_endpoint(
    payload: ModelInferenceRequest,
    api_key: str = Depends(verify_api_key)
):
    mock_prediction = round(sum(payload.feature_vector) / len(payload.feature_vector), 4)

    return {"status": "Inference Executed",
            "authorized_by": api_key,
            "model_version": payload.model_version,
            "prediction_score": mock_prediction}

if __name__ == "__main__":
    uvicorn.run("day_29:app", host = "127.0.0.1", port = 8000, reload = True)
