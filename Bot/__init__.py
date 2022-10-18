import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = environ.get('API_ID', 15849735)
API_HASH = environ.get('API_HASH', 'b8105dc4c17419dfd4165ecf1d0bc100')
BOT_TOKEN = environ.get('BOT_TOKEN', '5157922107:AAHFlGvnAh9acGgA8lvUERl4KLrD3FRj24Q')
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://soheru:roll@cluster0.7dyhvw6.mongodb.net/?retryWrites=true&w=majority')
OWNER_ID = int(environ.get('OWNER_ID', 953362604))
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1001591545511))
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1001894164463))
MESSAGE_ID = int(environ.get('MESSAGE_ID', 3)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
