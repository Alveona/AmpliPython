from amplipython.event import AmplipyEvent
from typing import List
from amplipython.utils import AMPLIPY_HTTPV2_URL, AMPLIPY_DEFAULT_HEADERS
import json
import requests
from amplipython.exceptions import *


class AmplipyClient:
    api_key: str = None

    def __init__(self, api_key: str):
        self.api_key = api_key

    def log_event(self, event: AmplipyEvent) -> None:
        """
        Forms a JSON body for sending to Amplitude server with single event
        Check docs for exceptions list
            :param event:AmplipyEvent: Event to send (not list!)
        """
        body_json = {
            "api_key": self.api_key,
            "events": [json.loads(event.json(exclude_unset=True, exclude_none=True))],
        }
        self._send_request_to_amplitude(body_json=body_json)

    def log_events(self, events: List[AmplipyEvent]):
        """
        Forms a JSON body for sending to Amplitude server with multiple events
        Check docs for exceptions list
            :param event:AmplipyEvent: Event to send (not list!)
        """
        body_json = {
            "api_key": self.api_key,
            "events": [
                json.loads(event.json(exclude_unset=True, exclude_none=True))
                for event in events
            ],
        }
        self._send_request_to_amplitude(body_json=body_json)

    def _send_request_to_amplitude(self, body_json: dict):
        """
        Sends a request to Amplitude endpoint with provided json
        Check docs for exceptions list
            :param event:AmplipyEvent: Event to send (not list!)
        """

        # makes no sense to handler ConnectionError here, just raise it
        resp = requests.post(
            url=AMPLIPY_HTTPV2_URL, headers=AMPLIPY_DEFAULT_HEADERS, json=body_json,
        )

        if resp.status_code == 200:
            pass
        elif resp.status_code == 400:
            error = json.loads(resp.text).get("error")
            raise AmplipyInvalidRequestError(
                f"Bad request occured, server says: {error}"
            )
        elif resp.status_code == 413:
            error = json.loads(resp.text).get("error")
            raise AmplipyPayloadTooLargeError(
                f"Payload is too big, server says: {error}"
            )
        elif resp.status_code == 429:
            error = json.loads(resp.text).get("error")
            raise AmplipyTooManyRequestsForDeviceError(
                f"Payload is too big, server says: {error}"
            )
        elif resp.status_code in [500, 502, 504]:
            raise AmplipyAmplitudeServerError(
                "Amplitude Server Error occured, check dashboard to avoid creating duplicates"
            )
        elif resp.status_code == 503:
            raise AmplipyAmplitudeIsUnavaliable(
                "Amplitude is currently unavaliable, you can safely repeat event, no duplicates will be created"
            )
