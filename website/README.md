## Framework

[fastapi](https://fastapi.tiangolo.com/) is  [faster](https://medium.com/@ahmed.nafies/why-did-we-choose-fast-api-over-flask-and-django-for-our-restful-micro-services-77589534c036) than flask. However I found flask a bit more
 easy at first to use. I think what makes fastapi strong is the concurrency and
  asnychronuous capability. Its definition is similar to flask, making it easy to migrate from
   flask to fastapi if needed.


## Requirements

* python 3.6 or higher

## Getting started

1. Clone the repository locally
2. [Setup](https://oemof.readthedocs.io/en/latest/installation_and_setup.html#using-virtualenv-community-driven) a virtual environment.
3. Install the dependencies `pip install -r requirements.txt`
4. run the app locally with `. website/run_app.sh`, or `uvicorn website.webapp:app --reload --port 5001` you can visualize it in your browser under  `http://127.0.0.1:5001`
