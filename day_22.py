from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/validate/{candidate_name}")

def validation_endpoint(candidate_name):
    return {"queried_profile" : candidate_name,
            "system_clearance" : "APPROVED",
            "assigned_track" : "MLE_SPRINT_ALPHA"}

if __name__ == "__main__":
    uvicorn.run("day_22:app", host = "127.0.0.1", port = 8000, reload = True)