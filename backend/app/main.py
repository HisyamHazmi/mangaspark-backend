from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
CORSMiddleware,
allow_origins=['*'], # or list your exact domains
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*'],
)


@app.get('/health')
def health():
return {"status": "ok"}


@app.get('/generate')
def generate(scene: str):
return {"panels": [
"https://placekitten.com/300/300",
"https://placekitten.com/301/300"
]}
