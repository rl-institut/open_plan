import os
import uvicorn
from starlette.responses import RedirectResponse
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
def landing_page(request: Request, project: int = None) -> Response:
    params = {"request": request}
    if project is not None:
        params["project"] = project
    return templates.TemplateResponse("landing_page.html", params)


@app.get("/project_created")
def project_created(request: Request) -> Response:
    return landing_page(request, project=1)


@app.get("/menubar")
def menu_bar(request: Request) -> Response:
    return templates.TemplateResponse("menu_bar.html", {"request": request})


@app.get("/create_project")
def create_project(request: Request) -> Response:
    return templates.TemplateResponse("create_project.html", {"request": request})


@app.get("/project_list")
def create_project(request: Request) -> Response:
    return templates.TemplateResponse("project_list.html", {"request": request})


@app.get("/proj_params")
def proj_params(request: Request) -> Response:
    return templates.TemplateResponse("proj_params.html", {"request": request})


@app.get("/load_proj_params")
def load_proj_params(request: Request) -> Response:
    return templates.TemplateResponse(
        "load_project_parameters.html", {"request": request}
    )


@app.get("/proj_location")
def proj_location(request: Request) -> Response:
    return templates.TemplateResponse("proj_location.html", {"request": request})


@app.get("/welcomepage")
def menu_bar(request: Request) -> Response:
    return templates.TemplateResponse("welcome_pop_up.html", {"request": request})


@app.get("/project_overview")
def project_overview(request: Request) -> Response:
    return templates.TemplateResponse("project_overview.html", {"request": request})


@app.get("/create_scenario")
def create_scenario(request: Request) -> Response:
    url = request.url_for("progression", step_id=1)
    return RedirectResponse(url=url)


@app.get("/load_scenario")
def load_scenario(request: Request) -> Response:
    return templates.TemplateResponse("load_scenarío.html", {"request": request})


@app.get("/step/{step_id}")
def progression(request: Request, step_id: int = 1) -> Response:
    return templates.TemplateResponse(
        f"step{step_id}.html", {"request": request, "step_id": step_id}
    )


@app.get("/progression_bar")
def progression_bar_vc(request: Request) -> Response:
    return templates.TemplateResponse("progression_bar_vc.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
