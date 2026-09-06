from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class CandidatePayload(BaseModel):
    name: str
    hours_logged: int
    projects_count: int

@app.post("/submit-profile")

def create_profile_endpoint(payload: CandidatePayload):
    return {"msg": "Data Payload Ingested Successfully",
            "received_name": payload.name,
            "computed_score": payload.hours_logged * payload.projects_count}

if __name__ == "__main__":
    uvicorn.run("day_24:app", host = "127.0.0.1", port = 8000, reload = True)
