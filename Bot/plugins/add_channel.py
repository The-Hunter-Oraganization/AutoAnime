from Bot import LOG, OWNER_ID, soheru as auto 
from pyrogram import filters 
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Bot.database.channels import add_new, find_channel, remove
from Bot.database.users import get_auth
from pyromod import listen
from Bot.utils.AnilistPython import anime_id_get, eng_name, jap_name
from Bot.utils.telegraph import telegraph_file_upload

@auto.on_message(filters.command('remove', prefixes='/'))
async def add_channels(client: auto, message: Message):
    if get_auth(message.from_user.id) is False:
        await message.reply('You Are Not Authorized To Perform This Action Contact Admins')
        return
    id_anime = message.text.split(" ", maxsplit=1)[1]
    if id_anime.isdigit() is False:
        anime_title = jap_name(id_anime)
        id_anime = anime_id_get(anime_title)
        if anime_title is None:
            anime_title = eng_name(id_anime)
            id_anime = anime_id_get(anime_title)
    elif id_anime.isdigit() is True:
        anime_title = jap_name(id_anime)
        if anime_title is None:
            anime_title = anime_id_get(id_anime)   
    output_status = remove(id_anime)
    await message.reply(f'**OwO Master** `{message.from_user.first_name}`\n,**I Removed** `{anime_title}`')

@auto.on_message(filters.command('add', prefixes='/'))
async def add_channels(client: auto, message: Message):
    if get_auth(message.from_user.id) is False:
        await message.reply('😞 You Are Not Authorized To Perform This Action Contact Admins')
        return
    if '|' in message.text:
        text = message.text.split(" ", maxsplit=1)[1]
        text = text.split('|')
        id_anime = text[0]
        if id_anime.isdigit() is False:
            anime_title = jap_name(id_anime)
            id_anime = anime_id_get(anime_title)
            if anime_title is None:
                anime_title = eng_name(id_anime)
                id_anime = anime_id_get(anime_title)
        elif id_anime.isdigit() is True:
            anime_title = jap_name(id_anime)
            if anime_title is None:
                anime_title = jap_name(id_anime)      
        anime_channel = text[1]
        thumbnail = text[2]
        if 'telegra.ph' not in thumbnail:
            thumbnail = None
        thumb = text[3]
        if 'telegra.ph' not in thumb:
            thumb = None
        file_name = text[4]
        if 'skip' in file_name:
            file_name = None
    else: 
        id_anime = await client.ask(message.chat.id, text="🙏 **Please Input Anime Name Or Anime ID**\n`To cancel process use` /cancel")
        id_anime = id_anime.text
        if 'cancel' in id_anime:
            await message.reply(f'🤷 Process Cancelled')
            return
        if id_anime.isdigit() is False:
            anime_title = jap_name(id_anime)
            id_anime = anime_id_get(anime_title)
            if anime_title is None:
                anime_title = eng_name(id_anime)
                id_anime = anime_id_get(anime_title)
        elif id_anime.isdigit() is True:
            anime_title = jap_name(id_anime)
            if anime_title is None:
                anime_title = eng_name(id_anime)
                      
        anime_channel = await client.ask(message.chat.id, text="🙏 **Please Input Channel ID**\n`To cancel process use` /cancel")
        anime_channel = anime_channel.text
        if 'cancel' in anime_channel:
            await message.reply(f'🤷 Process Cancelled')
            return
        if '-100' not in str(anime_channel):
            anime_channel = f"-100{str(anime_channel)}"
        #<----------THUMBNAIL---------->
        thumbnail = await client.ask(message.chat.id, text="🙏 **Please Send Anime Post Channel Image/Thumbnail**\n`To cancel process use` /cancel\n**Or**\n`To Use Default Anime Thumbnail Use` /skip")
        thumbnai = thumbnail
        thumbnail = thumbnail.text
        try:
            if 'cancel' in thumbnail:
                await message.reply(f'🤷 Process Cancelled')
                return   
        except Exception as e:
            LOG.error(f'Senpai Error: {e}')

        try:
            if thumbnai.photo:
               thumbnail_photo =  await thumbnai.download(f'thumbnail{message.from_user.id} + {message.id}.jpg')
               thumbnail = telegraph_file_upload(thumbnail_photo)
               await auto.send_message(message.chat.id, text='Uploaded Successfully', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Telegraph', url=thumbnail)]]))
        except Exception as e:
            LOG.error(f'Senpai Error: {e}')
            pass   
        try:
            if 'telegra.ph' not in thumbnail:
                thumbnail = None
        except Exception as e:
            LOG.error(f'Senpai Error: {e}')
            pass
            
        #<----------THUMB---------->    
        thumb = await client.ask(message.chat.id, text="🙏 **Please Send Anime File Thumb**\n`To cancel process use` /cancel\n**Or**\n`To Use Default Anime Thumb Use` /skip")
        thum = thumb
        thumb = thumb.text
        try:
            if 'cancel' in thumbnail:
                await message.reply(f'🤷 Process Cancelled')
                return   
        except Exception as e:
            LOG.error(f'Senpai Error: {e}')
            pass

        try:
            if thum.photo:
                thumb_photo = await thum.download(f'thumb{message.from_user.id} + {message.id}.jpg')
                thumb = telegraph_file_upload(thumb_photo)
                await auto.send_message(message.chat.id, text='Uploaded Successfully', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Telegraph', url=thumb)]]))
        except Exception as e:
            LOG.error(f'Senpai Error: {e}')
            pass
        try:
            if 'telegra.ph' not in thumb:
                thumb = None
        except Exception as e:
            LOG.error(f'Senpai Error: {e}')
            pass
        #<------------FILENAME-------------->             
        file_name = await client.ask(message.chat.id, text="🙏 **Please Input File Name**\n`To cancel process use` /cancel\n**Or**\n`To Use Default Anime Name Use` /skip")
        file_name = file_name.text
        if 'cancel' in file_name:
            await message.reply(f'🤷 Process Cancelled')
            return
        if 'skip' in file_name:
            file_name = None
        #<------------DATABASE ADD NOW----------->    
    try: 
        check_channel = find_channel(id_anime)
        if check_channel is None:
            add_new(anime_title, id_anime, anime_channel, file_name, thumb, thumbnail)
            text = f"Added \n**Anime Title** : {anime_title}\n**Anime ID**  :{id_anime}\n**Channel ID** : {anime_channel}"
        else:
            text = "Ayyo! This Anime Channel You Already Added. If you want to do any updates please remove old one. /remove anime name or id"
        await message.reply(text)
    except Exception as e:
        LOG.error(f'Senpai Error: {e}')   