from amplipy import AmplipyClient, AmplipyEvent

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

# NOTE: Events order is dashboard is not consistent!
client.log_events(event_list)
