from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home_endpoint():
    return {"status": "ONLINE", "engineer": "Saurabh", "target": "25_LPA_PLUS"}

if __name__ == "__main__":
    uvicorn.run("day_21:app", host="127.0.0.1", port=8000, reload=True)
