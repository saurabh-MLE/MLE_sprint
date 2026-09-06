from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

class profile_validation_schema(BaseModel):
    name: str = Field(..., min_length = 3, max_length = 50,
                      description = "Candidate Ful Name")
    hours_logged: int = Field(..., ge = 1, le = 1000,
                             description = "Hours logged must be between 1 and 1000")
    projects_count: int = Field(..., ge = 1, le = 50,
                               description = "Projects count must be between 1 and 50")

@app.post("/validate-candidate")

def validate_candidate_endpoint(payload: profile_validation_schema):
    return {"status": "Payload Passed Deep Field Validation",
            "candidate": payload.name,
            "efficiency_ratio": round(payload.hours_logged / payload.projects_count, 2)}

if __name__ == "__main__":
    uvicorn.run("day_25:app", host = "127.0.0.1", port = 8000, reload = True)
