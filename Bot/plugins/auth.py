from Bot import LOG, soheru as main
from pyrogram import filters 
from pyrogram.types import Message
from Bot.database.users import get_auth, new_user, update_user
from Bot.database.client import users as db

@main.on_message(filters.command(['auth', 'addsudo'], prefixes='!'))
async def auth_user(client:main, message:Message):
    if get_auth(message.from_user.id) is False:
        return 
    try:
        if message.reply_to_message: 
            user = message.reply_to_message.from_user.id 
    except: 
        pass
    if len(message.command) == 2:
        user = message.command[1]
    try:
        x = await main.get_users(user)
        user = x.id 
    except Exception as e:
        LOG.error(f'Senpai Error: {e}')
        await message.reply("No User Found")
        return 
    check = get_auth(user)
    if check is True:
        await message.reply(f"User Already Added in Authorized User List {x.mention()}")
        return
    new_user(user, True)                   
    await message.reply(f"Authorized User {x.mention()}")                        


@main.on_message(filters.command(['rmauth', 'unauth', 'rmsudo'], prefixes='!'))
async def unauthorize_user(client:main, message:Message):
    if get_auth(message.from_user.id) is False:
        return 
    try:
        if message.reply_to_message: 
            user = message.reply_to_message.from_user.id 
    except: 
        pass
    if len(message.command) == 2:
        user = message.command[1]
    try:
        x = await main.get_users(user)
        user = x.id
    except Exception as e:
        LOG.error(f'Senpai Error: {e}')
        await message.reply("No User Found")
        return 
    update_user(user, False)                 
    await message.reply(f"UnAuthorized User {x.mention()}")   