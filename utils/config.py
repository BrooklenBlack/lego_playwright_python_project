import os
from dotenv import load_dotenv

load_dotenv()

LEGO_BASE_URL = os.getenv("LEGO_BASE_URL")
LEGO_EMAIL = os.getenv("LEGO_EMAIL")
LEGO_PASSWORD = os.getenv("LEGO_PASSWORD")
LEGO_LOGIN_URL = os.getenv("LEGO_LOGIN_URL")