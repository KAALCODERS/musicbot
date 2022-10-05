from telethon import events, Button, custom
from MissNaina.events import register
from MissNaina import telethn as tbot
HIMAWARI = "https://telegra.ph/file/9dfcdab5244a61b323210.jpg"
@register(pattern=("/alive"))
async def awake(event):
  STB = event.sender.first_name
  STB = "**I m Himawari** \n\n" + "**I'm Working Properly**\n\n"
  STB += "**Python Version : 3.9.7**\n\n"
  STB += "**python-Telegram-Bot : 13.7**\n\n"
  BUTTON = [[Button.url("Support", "https://t.me/{SUPPORT_CHAT}"), Button.url("Updates", "https://t.me/{UPDATES_CHANNEL}")]]
  await tbot.send_file(event.chat_id, HIMAWARI, caption=STB,  buttons=BUTTON)

  # thanks to stb the gay
