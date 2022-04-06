from flask_frozen import Freezer
import os, fnmatch
from shocksoc_app.app import app

freezer = Freezer(app)

@freezer.register_generator
def top_URLs_generator():
    listOfFiles = os.listdir("templates/pages")
    pattern = "*.html.jinja2"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            page = entry.replace(".html.jinja2","")
            print(page)
            yield "routes.render_top_page", {"page": page}


#@freezer.register_generator
def project_URLs_generator():
    listOfFiles = os.listdir("templates/pages/projects")
    pattern = "*.html.jinja2"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            page = entry.replace(".html.jinja2","")
            print(page)
            yield "routes.render_project_page", {"page": page}
