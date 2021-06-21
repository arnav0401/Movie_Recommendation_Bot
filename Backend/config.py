import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
FAUNA_KEY = os.getenv('FAUNA_KEY')