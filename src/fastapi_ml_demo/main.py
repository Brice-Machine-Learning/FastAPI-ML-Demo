from fastapi import FastAPI

from fastapi_ml_demo.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)
from fastapi_ml_demo.core.inference import predict

app = FastAPI(title="ML Inference API")


@app.post("/predict", response_model=PredictionResponse)
def predict_endpoint(payload: PredictionRequest):
    value = predict(payload.features)
    return {
        "prediction": value,
        "units": "hundreds of thousands USD",
    }
