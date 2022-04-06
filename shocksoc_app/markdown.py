import markdown
import datetime
import os

md_dirs=["markdown/events/", "markdown/projects"]

#Used in sorting
def get_md_date(md:dict):
    #Get the datetime for the event
    try:
        print(md['meta']['date'][0])
        date = datetime.datetime.strptime(md['meta']['date'][0], "%d/%m/%Y").date()
    except:
        date = datetime.date.today() + datetime.timedelta(days=1)
    print(date)
    return date

def render_markdown(file_str:str) -> dict:
    with open(file_str,'r') as md_f:
        md_s = md_f.read()
        md = markdown.Markdown(extensions=['meta'])
        return dict(html = md.convert(md_s), meta = md.Meta)

def render_dir(dirname:str) -> list:
    md_lst=[]
    for file in os.listdir(dirname):
        filename = os.fsdecode(file)
        if filename.endswith(".md"):
           md_lst.append(render_markdown(os.path.join(dirname, filename)))
    return md_lst

events = render_dir("markdown/events")
try:
    events = render_dir("markdown/events")
except:
    print("Error rendering events dir")

future_events = [ev for ev in events if get_md_date(ev) >= datetime.date.today()]
past_events = [ev for ev in events if get_md_date(ev) < datetime.date.today()]

future_events = sorted(future_events, key=lambda event: get_md_date(event))
past_events = sorted(past_events, reverse=True, key=lambda event: get_md_date(event))

print("future: ")
print(future_events)
print("past: ")
print(past_events)

try:
    projects = render_dir(md_dirs[1])
except:
    print("Error rendering projects dir")

sorted_projects = sorted(projects, key=lambda project: get_md_date(project))
