from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re
import os
import ssl
from urllib.request import urlopen
import json
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


def convert_to_dict(info_list):
    # Joining the list elements into a single string
    info_string = ', '.join(info_list)

    # Using regex to extract values
    pattern = re.compile(r"(\w+)='([^']+)'")
    matches = pattern.findall(info_string)

    # Creating a dictionary from the matches
    info_dict = dict(matches)

    return info_dict


SYSTEM_INFO = convert_to_dict(str(os.uname()).split(","))

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


@app.get("/info", description="Get the server info")
def info():
    return SYSTEM_INFO


@app.get("/city/{ip_address}", description="To find geolocation based on an IP address")
def get_city_name(ip_address):
    ssl._create_default_https_context = ssl._create_unverified_context

    with urlopen(f"https://geoip.samagra.io/city/{ip_address}") as response:
        body = response.read()
    result_dict = json.loads(body.decode('utf-8'))
    print(result_dict)
    return result_dict
