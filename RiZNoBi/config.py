from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
OWNER_ID = getenv("OWNER_ID")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
