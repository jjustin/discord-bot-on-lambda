from os import environ

import requests

APP_ID = environ.get("APP_ID")
SERVER_ID = environ.get("SERVER_ID")
BOT_TOKEN = environ.get("BOT_TOKEN")

# global commands are cached and only update every hour
# url = f'https://discord.com/api/v10/applications/{APP_ID}/commands'

# while server commands update instantly
# they're much better for testing
url = f"https://discord.com/api/v10/applications/{APP_ID}/guilds/{SERVER_ID}/commands"

json = [{"name": "bleb", "description": "Test command.", "options": []}]

response = requests.put(url, headers={"Authorization": f"Bot {BOT_TOKEN}"}, json=json)

print(response.json())
