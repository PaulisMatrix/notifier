import os

# LOAD env variables
from dotenv import load_dotenv

LOADED = False

if not LOADED:
    load_dotenv("./src/.env")
    LOADED = True

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
BROKER_URL = os.getenv("BROKER_URL")
