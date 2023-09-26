from pyrogram import Client

api_id = int(input("Write Telegram API_ID: "))
api_hash = str(input("Write Telegram API_HASH: "))

app = Client(":memory:", api_id=api_id, api_hash=api_hash, in_memory=True)

print("Session string: ", app.export_session_string())
