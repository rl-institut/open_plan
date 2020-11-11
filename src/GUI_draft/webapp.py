import os
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

SERVER_ROOT = os.path.dirname(__file__)

app.mount(
    "/static", StaticFiles(directory=os.path.join(SERVER_ROOT, "static")), name="static"
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
def landing_page(request: Request) -> Response:
    return templates.TemplateResponse("landing_page.html", {"request": request})


@app.get("/menubar")
def menu_bar(request: Request) -> Response:
    return templates.TemplateResponse("menu_bar.html", {"request": request})


@app.get("/welcomepage")
def menu_bar(request: Request) -> Response:
    return templates.TemplateResponse("welcome_pop_up.html", {"request": request})

@app.get("/proj_params")
def proj_params(request: Request) -> Response:
    return templates.TemplateResponse("proj_params.html", {"request": request})

@app.get("/step1")
def step1(request: Request) -> Response:
    return templates.TemplateResponse("step1.html", {"request": request})


@app.get("/step2")
def step2(request: Request) -> Response:
    return templates.TemplateResponse("step2.html", {"request": request})


@app.get("/step3")
def step2(request: Request) -> Response:
    return templates.TemplateResponse("step3.html", {"request": request})


@app.get("/step4")
def step2(request: Request) -> Response:
    return templates.TemplateResponse("step4.html", {"request": request})


@app.get("/step5")
def step2(request: Request) -> Response:
    return templates.TemplateResponse("step5.html", {"request": request})


@app.get("/step6")
def step2(request: Request) -> Response:
    return templates.TemplateResponse("step6.html", {"request": request})
