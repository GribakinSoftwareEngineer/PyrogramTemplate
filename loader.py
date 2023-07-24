import os

from pyrogram import Client

from data import config


APP = Client(config.SESSION_NAME, api_id=config.API_ID, api_hash=config.API_HASH, app_version=config.VERSION, workdir=os.path.join(os.getcwd(), "sys"))
