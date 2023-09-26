from os import getenv as env

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

Client(
    "tuya_automatisation",
    session_string=env("TELEGRAM_SESSION_STRING"),
    plugins={"root": "plugins"}
).run()
