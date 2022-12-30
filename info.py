import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8081")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 4165961
API_HASH = "38ba6396e513b86e9ed7ea534023a9cc"
BOT_TOKEN = "5871118086:AAEaWqv0yDR2vLXEcxkTuN8nZipYsznD93M"

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://te.legra.ph/file/7b87785a8b6686370f6bf.jpg https://te.legra.ph/file/a1879771e29a7f63320e8.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1315317652').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001555811375').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = -1001555811375
AUTH_GROUPS = -1001833989877

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://9860tushar:9860tushar@cluster0.y0smsth.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'TG_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '<b>Hello {} 👋🏻\n\nMy Name is {bot}, I Can Provide Movies & Series Just Add Me To Your Group And Enjoy 😍</b>')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ Hey {query}! That's Not For You. Please Request Your Own.")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '<b> JOIN OUR UPDATES CHANNEL @M2LINKS TO USE THIS BOT</b>')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "https://telegra.ph/file/19eeb26fa2ce58765917a.jpg")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "Hey {user}\nwelcome to {chat}")
PMFILTER = bool(environ.get("PMFILTER", True))
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = bool(environ.get("BUTTON_LOCK", True))

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001555811375))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'M2linksCommunity')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>Fɪʟᴇ Nᴀᴍᴇ 📁 : </b><code>{file_name}</code>\n\n<b>JOIN 💎 : @OTSeries\n\nPOWERED BY ❤️  @M2LINKS</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b>Fɪʟᴇ Nᴀᴍᴇ 📁 : </b><code>{file_name}</code>\n\n<b>JOIN 💎 : @OTSeries\n\nPOWERED BY ❤️  @M2LINKS</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query:</b> {query}\n‌\n🏷 Title: <a href={url}>{title}</a>\n🎭 <b>Genres:</b> {genres}\n📆 <b>Year:</b> <ahref={url}/releaseinfo>{year}</a>\n🌟 <b>Rating:</b> <a href={url}/ratings>{rating}</a>\n☀️ <b>Languages :</b><code>{languages}</code>\n👨‍💼 <b>Dɪʀᴇᴄᴛᴏʀ:</b> {director}\n👨🏻‍🦱 <b>Pʀᴏᴅᴜᴄᴇʀ:</b> {producer}\n📑 <b>wʀɪᴛᴇʀ:</b> {writer}\n📀 <b>RunTime:</b> {runtime} Minutes\n📆 <b>Release Info :</b> {release_date}\n\n🍀Requested by🍀 : {message.from_user.mention}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

#log srt
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


