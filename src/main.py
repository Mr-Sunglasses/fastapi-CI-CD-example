from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]


def configure_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app() -> FastAPI:
    app = FastAPI(title="Demo CI App")
    configure_cors(app=app)

    return app


app = create_app()

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
