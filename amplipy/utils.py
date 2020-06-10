# list of Amplitude's reserved event types
AMPLIPY_HTTPV2_URL = "https://api.amplitude.com/2/httpapi"

AMPLIPY_DEFAULT_HEADERS = {"Content-Type": "application/json", "Accept": "*/*"}

AMPLIPY_EVENT_TYPE_BLACKLIST = [
    "[Amplitude] Start Session",
    "[Amplitude] End Session",
    "[Amplitude] Revenue",
    "[Amplitude] Revenue (Verified)",
    "[Amplitude] Revenue (Unverified)",
    "[Amplitude] Merged User",
]
