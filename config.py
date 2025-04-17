import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.hudl.com")
HUDL_USERNAME = os.getenv("HUDL_USERNAME")
HUDL_PASSWORD = os.getenv("HUDL_PASSWORD")
