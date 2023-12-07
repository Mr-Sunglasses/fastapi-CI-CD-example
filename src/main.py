from fastapi import FastAPI

app = FastAPI(title="Demo CI App")

DUMMY_DATA = {
    "id": 1,
    "name": "Spider Man",
    "powers": [
        {"flying": "Yes"},
        {"SuperSoilder": "Yes"}

    ]
}


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return {"status": "running"}


@app.get("/power")
def power():
    return DUMMY_DATA
