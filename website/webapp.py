import os
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .utils.compile_scss import convert_scss_to_css

app = FastAPI()

SERVER_ROOT = os.path.dirname(__file__)
STATIC_FOLDER = "static"


# compile scss files in /static/css folder to css files
convert_scss_to_css(
    [
        os.path.join(SERVER_ROOT, STATIC_FOLDER, "css", f)
        for f in os.listdir(os.path.join(SERVER_ROOT, STATIC_FOLDER, "css"))
        if f.endswith("scss")
    ]
)


app.mount(
    "/" + STATIC_FOLDER,
    StaticFiles(directory=os.path.join(SERVER_ROOT, STATIC_FOLDER)),
    name=STATIC_FOLDER,
)

templates = Jinja2Templates(directory=os.path.join(SERVER_ROOT, "templates"))


# option for routing `@app.X` where `X` is one of
# post: to create data.
# get: to read data.
# put: to update data.
# delete: to delete data.

# `127.0.0.1:8000/docs` endpoint will have autogenerated docs for the written code

# Test Driven Development --> https://fastapi.tiangolo.com/tutorial/testing/


@app.get("/")
def landing(request: Request) -> Response:
    convert_scss_to_css(
        [
            os.path.join(SERVER_ROOT, STATIC_FOLDER, "css", f)
            for f in os.listdir(os.path.join(SERVER_ROOT, STATIC_FOLDER, "css"))
            if f.endswith("scss")
        ]
    )
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/imprint")
def imprint(request: Request) -> Response:
    convert_scss_to_css(
        [
            os.path.join(SERVER_ROOT, STATIC_FOLDER, "css", f)
            for f in os.listdir(os.path.join(SERVER_ROOT, STATIC_FOLDER, "css"))
            if f.endswith("scss")
        ]
    )
    return templates.TemplateResponse("imprint.html", {"request": request})

@app.get("/privacy")
def imprint(request: Request) -> Response:
    convert_scss_to_css(
        [
            os.path.join(SERVER_ROOT, STATIC_FOLDER, "css", f)
            for f in os.listdir(os.path.join(SERVER_ROOT, STATIC_FOLDER, "css"))
            if f.endswith("scss")
        ]
    )
    return templates.TemplateResponse("privacy.html", {"request": request})

@app.get("/publications")
def imprint(request: Request) -> Response:
    convert_scss_to_css(
        [
            os.path.join(SERVER_ROOT, STATIC_FOLDER, "css", f)
            for f in os.listdir(os.path.join(SERVER_ROOT, STATIC_FOLDER, "css"))
            if f.endswith("scss")
        ]
    )
    return templates.TemplateResponse("publications.html", {"request": request})