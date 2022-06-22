import os
import requests
import json


def authenticate() -> str:
    '''Authenticates on the Firebase API with the provided (environment variables) email and password.'''
    API_KEY = os.getenv("FIREBASE_API_KEY")
    EMAIL = os.getenv("FIREBASE_EMAIL")
    PWD = os.getenv("FIREBASE_PWD")
    request_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}".format(
        API_KEY)
    data = {}
    data["email"] = EMAIL
    data["password"] = PWD
    data["returnSecureToken"] = True

    auth_request = requests.post(url=request_url, json=data)
    return(auth_request.json()["idToken"])


def get_events(idToken: str) -> str:
    '''Retrieves scheduled events from the database.'''
    database_url = "https://eventsplannerapp-16769-default-rtdb.europe-west1.firebasedatabase.app/events.json?auth={}".format(idToken)

    events_request = requests.get(url=database_url)
    events_response = events_request.json()

    # Remove placeholder event
    del events_response["0"]

    events = {
        "events": []
    }
    for event in events_response:
        events["events"].append({
            "name": events_response[event]["title"],
            "description": events_response[event]["description"],
            "date": ("Every " if events_response[event]["recurring"] else "") + events_response[event]["date"],
            "start_time": events_response[event]["start"],
            "end_time": events_response[event]["end"],
            "location": events_response[event]["room"],
            "image": events_response[event].get("imageURL", ""),
            "form": events_response[event].get("formURL", "")
        })

    return events