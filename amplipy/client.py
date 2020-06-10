from amplipy.event import AmplipyEvent
from typing import List
from amplipy.utils import AMPLIPY_HTTPV2_URL, AMPLIPY_DEFAULT_HEADERS
import json
import requests


class AmplipyClient:
    api_key: str = None

    def __init__(self, api_key: str):
        self.api_key = api_key

    def log_event(self, event: AmplipyEvent) -> None:
        """
        Sends a request to Amplitude endpoint with encoded Event  
        Check docs for exceptions list
            :param event:AmplipyEvent: Event to send (not list!)
        """
        body_json = {"api_key": self.api_key, "events": [event.json()]}
        resp = requests.post(
            url=AMPLIPY_HTTPV2_URL, headers=AMPLIPY_DEFAULT_HEADERS, json=body_json
        )

        if resp.status_code == 200:
            pass
        elif resp.status_code == 400:
            error = json.loads(resp.text).get("error")
        elif resp.status_code == 413:
            error = json.loads(resp.text).get("error")
        elif resp.status_code == 429:
            error = json.loads(resp.text).get("error")
        elif (
            resp.status_code == 500
            or resp.status_code == 502
            or resp.status_code == 504
        ):
            pass
        elif resp.status_code == 503:
            pass

    def log_events(self, events: List[AmplipyEvent]):
        pass
