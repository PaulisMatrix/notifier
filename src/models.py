from enum import Enum
from typing import Union, Optional

from pydantic import BaseModel


class Channel(str, Enum):
    ALL = "all"
    EMAIL = "email"
    WHATSAPP = "whatsapp"

    def __str__(self) -> str:
        return self.value


class Handlers(str, Enum):
    EMAILHANDLER = "EmailNotificationHandler"
    WHATSAPPHANDLER = "WhatsAPPNotificationHandler"
    SMSHANDLER = "SMSNotificationHandler"

    def __str__(self) -> str:
        return self.value


class OrderStatus(str, Enum):
    PLACED = "placed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return self.value


class PayloadMetadata(BaseModel):
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    channel: Channel = "all"


class UserData(BaseModel):
    user_id: str
    user_name: str
    user_emailid: str
    user_mobileno: str


class OrdersPayload(UserData, PayloadMetadata):
    order_id: str
    order_total: float
    order_status: OrderStatus
    expected_date: str
    delivery_address: str
    payment_mode: str
    tracking_id: Union[str, None] = None
    carrier_name: Union[str, None] = None


class ServerResponse(BaseModel):
    status_code: int
    status: str
    info: str
    responded_at: str
    respoded_updated_at: str
