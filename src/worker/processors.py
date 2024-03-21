from abc import ABC, abstractmethod
import logging
from typing import Tuple

import yagmail

from worker.utils import get_html_content


class NotificationHandler(ABC):
    logger = None
    session = None

    def __init__(self) -> None:
        super().__init__()

        # if NotificationHandler.session is None:
        #    NotificationHandler.session = aiohttp.ClientSession()

        if NotificationHandler.logger is None:
            NotificationHandler.logger = logging.getLogger(__name__)

    @abstractmethod
    def _prepare_payload(self, event_payload: dict) -> Tuple[str, str]:
        pass

    @abstractmethod
    async def send_notification(self, event_payload: dict):
        pass


class EmailNotificationHandler(NotificationHandler):
    def __init__(self) -> None:
        super().__init__()
        self.receiver = "sirius8.612ly@gmail.com"
        self.sender = "1999.yadwade@gmail.com"
        self.gmail_creds_filepath = "worker/notifier.json"

    def _prepare_payload(self, event_payload: dict) -> Tuple[str, str]:
        # Any kind of filtering/updating the payload before send the mail
        filtered_payload = dict()
        filtered_payload["user_name"] = event_payload.get("user_name", "")
        filtered_payload["user_emailid"] = self.receiver
        filtered_payload["order_id"] = event_payload.get("order_id", "")
        filtered_payload["order_subtotal"] = event_payload.get("order_subtotal", 0)
        filtered_payload["shipping_charges"] = event_payload.get("shipping_charges", 0)
        filtered_payload["discount_applied"] = event_payload.get(
            "discount_applied", False
        )
        filtered_payload["total_discount"] = event_payload.get("total_discount", 0)
        filtered_payload["currency"] = event_payload.get("currency", "")
        filtered_payload["num_items"] = event_payload.get("num_items", 0)
        filtered_payload["order_status"] = event_payload.get("order_status", "")
        filtered_payload["expected_date"] = event_payload.get("expected_date", "")
        filtered_payload["delivery_address"] = event_payload.get("delivery_address", "")
        filtered_payload["payment_mode"] = event_payload.get("payment_mode", "")
        filtered_payload["tracking_id"] = event_payload.get("tracking_id", "")
        filtered_payload["carrier_name"] = event_payload.get("carrier_name", "")

        payload, subject = get_html_content(info=filtered_payload)
        return payload, subject

    async def send_notification(self, event_payload: dict):
        content, subject = self._prepare_payload(event_payload=event_payload)

        # TODO: Find an async email sender. aioyagmail doesn't work!!!
        yag = yagmail.SMTP(user=self.sender, oauth2_file=self.gmail_creds_filepath)
        yag.send(
            to=self.receiver,
            subject=subject,
            contents=content,
        )
        self.logger.info("done sending the notification to the email channel")


class WhatsAPPNotificationHandler(NotificationHandler):
    def __init__(self) -> None:
        super().__init__()

    def _prepare_payload(self, event_payload: dict) -> Tuple[str, str]:
        pass

    async def send_notification(self, event_payload: dict):
        pass


class SMSNotificationHandler(NotificationHandler):
    def __init__(self) -> None:
        super().__init__()

    def _prepare_payload(self, event_payload: dict) -> Tuple[str, str]:
        pass

    async def send_notification(self, event_payload: dict):
        pass
