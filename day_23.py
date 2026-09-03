from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/evaluate")

def query_endpoint(hours: int, projects: int):
    if hours >= 1000 and projects >= 5:
        return {"STATUS" : "SHORTLISTED",
                "logged_hours" : hours,
                "project_count" : projects}
    else:
        return {"STATUS" :"KEEP BUILDING"}

if __name__ == "__main__":
    uvicorn.run("day_23:app", host = "127.0.0.1", port = 8000, reload = True)
