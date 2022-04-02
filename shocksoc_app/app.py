import flask
import json
from os import path
import shocksoc_app.routes

app = flask.Flask(__name__, static_folder=None, template_folder=None)
app.config["TEMPLATES_AUTO_RELOAD"] = True

from shocksoc_app.routes import blueprint, ROOT_DIR, TEMPLATE_DIR

app.register_blueprint(blueprint)

app.config["FREEZER_DESTINATION"] = path.join(ROOT_DIR, "build")
app.config.setdefault("FREEZER_BASE_URL", "http://www.shocksoc.org")
with open("events_list.json", 'r') as f:
    events_json_b = f.read()
    events = json.loads(events_json_b)

with open("links_list.json", 'r') as f:
    links_json_b = f.read()
    main_links = json.loads(links_json_b)

    

@app.context_processor
def inject_events():
    #print( dict(ev_dict = events["events"]))
    return dict(ev_dict = events["events"])

@app.context_processor
def inject_main_links():
    #print( dict(main_links_dict = main_links["links"]))
    return dict(main_links_dict = main_links["links"])
