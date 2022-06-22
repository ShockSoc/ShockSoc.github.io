import flask
import json
from datetime import datetime
from os import path
import os
import shocksoc_app.firebase
import shocksoc_app.routes
import shocksoc_app.markdown

app = flask.Flask(__name__, static_folder=None, template_folder=None)
app.config["TEMPLATES_AUTO_RELOAD"] = True

from shocksoc_app.routes import blueprint, ROOT_DIR, TEMPLATE_DIR

app.register_blueprint(blueprint)

app.config["FREEZER_DESTINATION"] = path.join(ROOT_DIR, "build")
app.config.setdefault("FREEZER_BASE_URL", "http://www.shocksoc.org")

with open("links_list.json", 'r') as f:
    links_json_b = f.read()
    main_links = json.loads(links_json_b)

@app.context_processor
def inject_date():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dict(date_time_now = dt_string)    

@app.context_processor
def inject_events():
    #print( dict(ev_dict = events["events"]))
    idToken = shocksoc_app.firebase.authenticate()
    events = shocksoc_app.firebase.get_events(idToken=idToken)
    return dict(ev_dict = events["events"])

@app.context_processor
def inject_main_links():
    #print( dict(main_links_dict = main_links["links"]))
    return dict(main_links_dict = main_links["links"])

@app.context_processor
def inject_about():
    try:
        markdown = shocksoc_app.markdown.render_markdown("markdown/home_about.md")
        home_html = markdown['html']
    except:
        home_html = ""
    try:
        markdown = shocksoc_app.markdown.render_markdown("markdown/about.md")
        about_html = markdown['html']
    except:
         about_html = "ShockSoc York.<br> <em>The</em> University Of York Engineering Society."
        
    return dict(about = about_html, home_about = home_html)

@app.context_processor
def inject_basic_about():
    try:
        markdown = shocksoc_app.markdown.render_markdown("markdown/about.md")
        html = markdown['html']
    except:
        html = "ShockSoc York.<br> <em>The</em> University Of York Engineering Society."
    return dict(about_us = html)

def get_fonts(dirname:str) -> list:
    fonts=[]
    for file in os.listdir(dirname):
        filename = os.fsdecode(file)
        if filename.endswith(".ttf") or filename.endswith(".otf"):
           fonts.append(dict(source = f"fonts/{filename}", name=filename.split(".")[0]))
    return fonts
