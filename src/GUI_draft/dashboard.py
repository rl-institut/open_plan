from flask.helpers import get_root_path
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html


def register_dashapp(server, base_pathname, title, layout):
    """Create Dash app."""

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    dash_app = Dash(
        server=server,
        routes_pathname_prefix=f"/{base_pathname}/",
        requests_pathname_prefix=f"/dash/{base_pathname}/",
        assets_folder=get_root_path(__name__) + "/static/",
        meta_tags=[meta_viewport],
    )
    # with server.app_context():
    dash_app.title = title
    dash_app.layout = layout

    return dash_app


dashboard_layout = html.Div(id="dash-container", children="dash app")
