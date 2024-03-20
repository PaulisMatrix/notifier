## Broker settings.
broker_url = "redis://127.0.0.1:6379/0"

# List of modules to import when the Celery worker starts.
imports = ("worker.celery_worker",)
