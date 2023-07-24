from pyrogram.filters import command

from data import config
from loader import APP


@APP.on_message(filters=command("version"))
async def cmd_version(client, message_text):
    await APP.send_message(chat_id=message_text.from_user.id, text=config.VERSION)
