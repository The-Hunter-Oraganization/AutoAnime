import sys, os
from Bot import soheru, OWNER_ID
from pyrogram import filters 
from pyrogram.types import  Message
from Bot.database.users import get_auth

@soheru.on_message(filters.user(OWNER_ID) & filters.command('restart', prefixes='/'))
async def restart_bot(client: soheru, message: Message): 
    if get_auth(message.from_user.id) is False:
        await message.reply('😞 You Are Not Authorized To Perform This Action Contact Admins')
        return
    msg = await message.reply("Restarting")
    os.execl(sys.executable, sys.executable, "-m", "Bot")  