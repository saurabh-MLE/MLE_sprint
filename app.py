import torch
import torch.nn as nn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Production PyTorch Inference Gateway",
    description="Low-latency model serving engine",
    version="1.0.0"
)

class SimpleMLEModel(nn.Module):
    def __init__(self):
        super(SimpleMLEModel, self).__init__()
        self.linear = nn.Linear(in_features=2, out_features=1)

    def forward(self, x):
        return self.linear(x)

model = SimpleMLEModel()
model.load_state_dict(torch.load("model_weights.pth"))
model.eval()

class InferenceInput(BaseModel):
    feature_1: float
    feature_2: float

@app.post("/predict")
def predict(payload: InferenceInput):
    tensor_data = torch.tensor([[payload.feature_1, payload.feature_2]], dtype=torch.float32)
    
    with torch.no_grad():
        output = model(tensor_data)
        
    return {
        "status": "success",
        "prediction": output.item()
    }

@app.get("/health")
def healthcheck():
    return {"status": "healthy", "model_loaded": True}