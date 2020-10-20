## Framework

[fastapi](https://fastapi.tiangolo.com/)

## Requirements

* python 3.6 or higher

## Getting started

1. [Setup](https://oemof.readthedocs.io/en/latest/installation_and_setup.html#using-virtualenv-community-driven) a virtual environment
2. From the root of the repository, install the dependencies `pip install -r requirements/website.txt`
3. Run the app locally with`uvicorn src.GUI_draft.webapp:app --reload --port 5001` you can visualize it in your browser under `http://127.0.0.1:5001`
4. Edit the html files and refresh you browser to see the changes live