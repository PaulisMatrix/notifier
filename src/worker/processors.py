import asyncio
import aiohttp
from abc import ABC, abstractmethod


class NotificationHandler(ABC):
    @abstractmethod
    def _prepare_payload(self, event_payload: dict) -> dict:
        pass

    @abstractmethod
    async def send_notification(self, event_payload: dict):
        pass


class EmailNotificationHandler(NotificationHandler):
    def _prepare_payload(self, event_payload: dict) -> dict:
        return super()._prepare_payload(event_payload)

    async def send_notification(self, event_payload: dict):
        print("got event payload in email class : ", event_payload)
        return


class WhatsAPPNotificationHandler(NotificationHandler):
    def _prepare_payload(self, event_payload: dict) -> dict:
        return super()._prepare_payload(event_payload)

    async def send_notification(self, event_payload: dict):
        print("got event payload in whatsapp class : ", event_payload)
        return


class SMSNotificationHandler(NotificationHandler):
    def _prepare_payload(self, event_payload: dict) -> dict:
        return super()._prepare_payload(event_payload)

    async def send_notification(self, event_payload: dict):
        pass
