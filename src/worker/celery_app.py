# Celery worker to send the notifications to the relevant channel.

from celery import Celery


celery_app = Celery(
    "notifier-bg",
    broker="redis://127.0.0.1:6379/0",
)

celery_app.config_from_object("worker.celeryconfig")
