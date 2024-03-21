import json

from celery import Task
from celery.utils.log import get_task_logger
from worker.celery_app import celery_app
import asyncio
from worker import processors

logger = get_task_logger(__name__)


class BaseTask(Task):
    def __init__(self) -> None:
        super().__init__()


@celery_app.task(base=BaseTask, bind=True)
def dummy_task(self: BaseTask, *args, **kwargs):
    event_payload = json.loads(kwargs.get("event_payload", {}))
    handlers = kwargs.get("handlers", [])

    if (event_payload is None) or len(handlers) == 0:
        logger.error(
            "critical data missing for handling a given taks. dropping the event..."
        )
        return

    coroutine_handlers = []
    for class_name in handlers:
        # create payloads depending on the given channel.
        channel_class: processors.NotificationHandler = getattr(processors, class_name)
        channel_instance: processors.NotificationHandler = channel_class()

        # create a bunch of awaitable coroutines
        coroutine_handlers.append(
            channel_instance.send_notification(event_payload=event_payload)
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(make_request(coroutine_handlers=coroutine_handlers))

    return


async def make_request(
    coroutine_handlers: list,
):
    # run all the coroutines concurrently
    try:
        _ = await asyncio.gather(*coroutine_handlers, return_exceptions=True)
    except Exception:
        logger.warning("Error while sending notifications", exc_info=True)
