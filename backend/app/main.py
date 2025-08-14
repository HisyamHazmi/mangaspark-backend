from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/generate")
def generate(scene: str):
    # Placeholder AI generation logic
    return {"panels": ["https://placekitten.com/300/300", "https://placekitten.com/301/300"]}
