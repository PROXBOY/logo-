import requests
from pyrogram import Client as Bot

from RiZNoBi.config import API_HASH
from RiZNoBi.config import API_ID
from RiZNoBi.config import BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="RiZNoBi.modules"),
)
