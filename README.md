AmpliPython
===========
[![PyPI version](https://badge.fury.io/py/AmpliPython.svg)](https://badge.fury.io/py/AmpliPython)
![GitHub stars](https://img.shields.io/github/stars/Alveona/AmpliPython?style=social)

![](https://camo.githubusercontent.com/3ed177a93b6b646e75176c2f9acdb52bfbe252ce/68747470733a2f2f7374617469632e616d706c69747564652e636f6d2f6c696768746e696e672f343663383562666439313930356465383034376631656536356337633933643666613965653665612f7374617469632f6d656469612f616d706c69747564652d6c6f676f2d776974682d746578742e34666239653436332e737667)


AmpliPython is a Python library which provides an easy method to log your events with Amplitude Analytics.  
Built with Pydantic.

Installing
----------

You can install this using pip.

````$ pip install AmpliPython````

Quick Start
----------

Usage is pretty easy, just pass all the params you want to `AmplipyEvent` and then log it with `AmplipyClient`

```python
from amplipython import AmplipyClient, AmplipyEvent

client = AmplipyClient(api_key="YOUR_API_KEY")

# Single event example, no additional data provided
event = AmplipyEvent(user_id="sample", event_type="amplipy-sample")
client.log_event(event)

# Multiple events example with event and user data
event_list = []
for i in range(5):
    event = AmplipyEvent(
        user_id="sample",
        event_type="amplipy-sample",
        event_properties={"iteration": i},
        user_properties={"sent_by": "amplipy"},
    )
    event_list.append(event)

# NOTE: Events order is dashboard is not specified!
client.log_events(event_list)

```

See all params you can pass to `AmplipyEvent` instance 

Exceptions
-------------

When trying to log event, following exceptions could be raised:

- `AmplipyInvalidRequestError`

- `AmplipyPayloadTooLargeError`

- `AmplipyTooManyRequestsForDeviceError`

- `AmplipyAmplitudeServerError`

- `AmplipyAmplitudeIsUnavaliable`

Event Params
-------------

All keys for AmplipyEvent initializer could be found in official Amplitude docs:  
https://developers.amplitude.com/docs/http-api-v2

-------------

PRs are pretty much welcomed and highly appreciated! 👻

