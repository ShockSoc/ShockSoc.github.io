from flask import Blueprint, Response, render_template, url_for
import os
from os import path
from flask import Blueprint, Response, render_template, url_for
import jinja2
from jinja2 import FileSystemLoader

ROOT_DIR = path.abspath(path.join(path.dirname(__file__), '..'))
TEMPLATE_DIR = path.join(ROOT_DIR, "templates")

blueprint = Blueprint(
    "routes",
    __name__,
    static_folder=path.join(ROOT_DIR, "static"),
    static_url_path="/static/",
)


blueprint.jinja_loader = jinja2.ChoiceLoader(
    [
        FileSystemLoader(TEMPLATE_DIR),
        #CustomLoader(TEMPLATE_DIR, prefix_allow="*"),
    ]
)

@blueprint.route("/static/fonts.css")
def render_fonts_css():
    from shocksoc_app.app import get_fonts
    from flask import Response
    """Generate fonts CSS.
    Returns:
        str: CSS
    """
    css = render_template(f"fonts.css.jinja2", fonts = get_fonts("static/fonts/"))
    return Response(css, mimetype='text/css')

@blueprint.route("/<string:page>.html")
def render_top_page(page: str):
    """Renders a simple page.
    Serves `pages/foo.html.jinja2` at `/foo.html`
    Args:
        page (str): name of the page (with no extension)
    Returns:
        str: HTML
    """
    return render_template(f"pages/{page}.html.jinja2")

@blueprint.route("/projects/<string:page>.html")
def render_project_page(page: str):
    """Renders an event page.
    Serves `pages/events/foo.html.jinja2` at `/events/foo.html`
    Args:
        page (str): name of the page (with no extension)
    Returns:
        str: HTML
    """
    return render_template(f"pages/project.html.jinja2")


@blueprint.route("/")
def index():
    """Handles / serving index.html
    Returns:
        str: Full HTML page
    """
    return render_top_page("index")

@blueprint.route("/past_events_<int:page>.html")
def render_events():
    """Handles serving past events
    Returns:
        str: Full HTML page
    """
    return render_template(f"pages/past_events.html.jinja2")
