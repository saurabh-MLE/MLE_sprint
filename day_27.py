from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import uvicorn

app = FastAPI()

class CandidateSubmission(BaseModel):
    full_name: str = Field(..., min_length = 2, max_length = 50)
    email: str = Field(..., description = "Candidate contact email")
    github_profile: str = Field(..., description = "URL pointing to candidate GitHUb")

    @field_validator("email")
    @classmethod
    def sanitize_email(cls, value: str) -> str:
        clean_value = value.strip().lower()

        if "@" not in clean_value:
            raise ValueError("Invalid email: missing '@' symbol")

        return clean_value

    @field_validator("github_profile")
    @classmethod
    def validate_github(cls, value: str) -> str:
        if not value.startswith("https://github.com/"):
            raise ValueError("Profile URL must begin with 'https://github.com/'")
        return value

@app.post("/register-candidate")
def register_candidate_endpoint(payload: CandidateSubmission):
    return {"status": "Candidate Validated & Sanitized",
            "clean_email": payload.email,
            "verified_github": payload.github_profile,
            "raw_name": payload.full_name,}

if __name__ == "__main__":
    uvicorn.run("day_27:app", host = "127.0.0.1", port = 8000, reload = True)