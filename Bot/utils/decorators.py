from Bot import LOG, MAIN_CHANNEL, soheru, MESSAGE_ID
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

from Bot.plugins.font_change import text_replace
async def upload_file(file, chat, thumb=None, caption=None):
    try:
       files =  await soheru.send_document(int(chat), document=file, thumb=thumb, caption=caption)
    except:
       files =  await soheru.send_document(int(chat), document=file, caption=caption)
    return files  

async def message_status(text):
    try:
        await soheru.edit_message_text(MAIN_CHANNEL, message_id=MESSAGE_ID, text=text, reply_markup=IKM([[IKB(text_replace('Dev'), url='https://t.me/AboutMeSk/168'), IKB(text_replace('Files'), url=f"https://t.me/Auto_Airing_Animes")]]))
    except Exception as e:
        LOG.error(f'Senpai Error :{e}')
        pass      
    return None