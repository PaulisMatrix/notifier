import json
import pytz
from datetime import datetime

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

from worker.celery_app import celery_app
from models import ServerResponse, OrdersPayload, Handlers

app = FastAPI(title="notifier")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# for any data validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = exc.errors()
    modified_details = []
    # Replace 'msg' with 'message' for each error
    for error in details:
        modified_details.append(
            {
                "loc": error["loc"],
                "message": error["msg"],
                "type": error["type"],
            }
        )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": modified_details}),
    )


@app.post("/send-notif", status_code=status.HTTP_200_OK)
def dispatch_notification(data: OrdersPayload):
    # serialize the JSON and add
    event_payload = json.dumps(jsonable_encoder(data))
    task_name = "worker.celery_worker.dummy_task"

    # Register your functions here to which channel you want to send the notif
    # Can add selectively based on the "channel" param sent by the services as well
    handlers = [Handlers.SENDEMAIL]
    _ = celery_app.send_task(
        task_name, kwargs={"event_payload": event_payload, "handlers": handlers}
    )

    asia_time = datetime.now(pytz.timezone("Asia/Kolkata"))
    cur_time = asia_time.strftime("%H:%M:%S")
    resp = ServerResponse(
        status_code=status.HTTP_200_OK,
        status="success",
        info="sent notification to the respective channel",
        responded_at=cur_time,
        respoded_updated_at=cur_time,
    )

    return JSONResponse(content=jsonable_encoder(resp))


# Dummmy handler for testing
@app.post("/email-handler", status_code=status.HTTP_200_OK)
def email_handler(data: OrdersPayload):
    print("got event data: ", json.dumps(jsonable_encoder(data)))
    asia_time = datetime.now(pytz.timezone("Asia/Kolkata"))
    cur_time = asia_time.strftime("%H:%M:%S")

    resp = ServerResponse(
        status_code=status.HTTP_200_OK,
        status="success",
        info="sent notification to the users email address",
        responded_at=cur_time,
        respoded_updated_at=cur_time,
    )

    return JSONResponse(content=jsonable_encoder(resp))


# @app.on_event("startup")
# async def startup():
#   pass


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=3001)
