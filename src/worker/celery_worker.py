import json

from celery.utils.log import get_task_logger
from .celery_app import celery_app

from .processors import Processors

logger = get_task_logger(__name__)


@celery_app.task
def dummy_task(*args, **kwargs):
    event_payload = json.loads(kwargs.get("event_payload", {}))
    handlers = kwargs.get("handlers", [])
    if (event_payload is None) or len(handlers) == 0:
        logger.error(
            "critical data missing for handling a given taks. dropping the event..."
        )
        return

    # apply this async
    task_processor = Processors()
    for handler in handlers:
        try:
            getattr(task_processor, handler)(event_payload=event_payload)
        except:
            logger.error("exception in executing the task", exc_info=True)

    return
