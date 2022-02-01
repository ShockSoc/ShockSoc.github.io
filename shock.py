import flaskim
from os import path
import shocksoc_app.routes

import flask
from os import path

app = flask.Flask(__name__, static_folder=None, template_folder=None)
app.config["TEMPLATES_AUTO_RELOAD"] = True

from shocksoc_app.routes import blueprint, ROOT_DIR

app.register_blueprint(blueprint)

app.config["FREEZER_DESTINATION"] = path.join(ROOT_DIR, "build")
app.config.setdefault("FREEZER_BASE_URL", "http://www.shocksoc.org")
