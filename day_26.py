from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
import uvicorn

app = FastAPI()

class ProjectRecord(BaseModel):
    title: str = Field(..., min_length = 2, max_length = 100,
                       description = "Project Title")
    technologies_used: int = Field(..., ge = 1, le = 20,
                                   description = "Count of tools/tech utilized")

class CandidateBatchPayload(BaseModel):
    candidate_name: str = Field(..., min_length = 3, max_length = 50)
    projects: List[ProjectRecord] = Field(..., min_length = 1,
                                          description = "List of submitted projects")

@app.post("/ingested-candidate-portfolio")

def ingest_candiadte_portfoilo_endpoint(payload: CandidateBatchPayload):
    total_tech = sum(item.technologies_used for item in payload.projects)

    return {"status": "Nested Portfolio Successfully Validated",
            "candidate": payload.candidate_name,
            "projects_analyzed": len(payload.projects),
            "total_technologies_tracked": total_tech,}

if __name__ == "__main__":
    uvicorn.run("day_26:app", host = "127.0.0.1", port = 8000, reload = True)