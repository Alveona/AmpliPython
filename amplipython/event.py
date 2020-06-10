from pydantic import BaseModel, root_validator, validator
from amplipython.utils import AMPLIPY_EVENT_TYPE_BLACKLIST
from typing import Optional


class AmplipyEvent(BaseModel):
    user_id: Optional[str]
    device_id: Optional[str]
    event_type: str
    time: Optional[int]
    event_properties: Optional[dict]
    user_properties: Optional[dict]
    groups: Optional[dict]
    platform: Optional[str]
    os_name: Optional[str]
    os_version: Optional[str]
    device_brand: Optional[str]
    device_manufacturer: Optional[str]
    device_model: Optional[str]
    carrier: Optional[str]
    country: Optional[str]
    region: Optional[str]
    dma: Optional[str]
    language: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    revenue: Optional[float]
    productId: Optional[str]
    revenueType: Optional[str]
    location_lat: Optional[float]
    location_lng: Optional[float]
    ip: Optional[str]
    event_id: Optional[int]
    session_id: Optional[int]
    insert_id: Optional[int]

    @root_validator
    def check_user_id_or_device_id_exists(cls, values):
        user_id, device_id = values.get("user_id"), values.get("device_id")

        if user_id is None and device_id is None:
            raise ValueError("Either user_id or device_id should be specified in Event")
        return values

    @validator("event_type")
    def check_event_type_blacklist(cls, v):
        if v in AMPLIPY_EVENT_TYPE_BLACKLIST:
            raise ValueError(f"Can't use {v} event type, it is reserved by Amplitude")
        return v

    @validator("groups")
    def check_groups(cls, v):
        raise ValueError("Amplitude Enterprise features aren't supported yet")

    @validator("event_id", "session_id", "insert_id")
    def check_optionals(cls, v):
        raise ValueError(
            "event_id, session_id and insert_id parameters aren't supported yet"
        )
