from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

class CandidateApplicationIn(BaseModel):
    full_name: str = Field(..., min_length = 2, max_length = 50)
    raw_score: float = Field(..., ge = 0.0, le = 100.0,
                             description = "Raw interview/model score")
    expected_salary: int = Field(..., ge = 300000,
                                 description = "Inetrnal candidate salary expectation")

class CandidateApplicationOut(BaseModel):
    full_name: str
    normalized_score: float = Field(..., description = "Score normalized to scale 0.0 to 1.0")
    status: str

@app.post("/evaluate-application", response_model = CandidateApplicationOut)
def evaluate_application(payload: CandidateApplicationIn):
    norm_score = round(payload.raw_score/100.0, 2)

    return {"full_name": payload.full_name,
            "normalized_score": norm_score,
            "status": "Shortlisted" if norm_score >= 0.7 else "Under Review",
            "expected_salary": payload.expected_salary}

if __name__ == "__main__":
    uvicorn.run("day_28:app", host = "127.0.0.1", port = 8000, reload = True)
