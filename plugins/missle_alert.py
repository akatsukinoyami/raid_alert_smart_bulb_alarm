from os import getenv as env

from pyrogram import Client as app, filters

from lib.bulbs import Bulbs
from lib.colour import Colour


bulbs = Bulbs()
chat = filters.chat("air_alert_ua")
region = filters.regex(env("REGION"))


@app.on_message(chat & region & filters.regex("Повітряна тривога"))
async def on_missle_attack_message(app, msg):
    bulbs.flash(
        times=int(env("FLASH_TIMES")),
        sleep_time=float(env("SLEEP_TIME")),
        colour=Colour.RED)


@app.on_message(chat & region & filters.regex("Відбій тривоги"))
async def on_alert_cancel_message(app, msg):
    bulbs.flash(
        times=int(env("FLASH_TIMES")),
        sleep_time=float(env("SLEEP_TIME")),
        colour=Colour.GREEN)
