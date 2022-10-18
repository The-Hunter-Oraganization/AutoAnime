import os
import time
import subprocess
import requests, asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, Message
from Bot import ARCHIVE_CHANNEL, LOG, MAIN_CHANNEL, soheru 
from Bot.database.channels import custom_file, custom_thumb, custom_wall, find_channel
from Bot.database.client import check_resolution
from Bot.database.rss import check_pending, new
from Bot.plugins.api import AnimePahe
from Bot.plugins.font_change import text_replace
from Bot.utils.AnilistPython import anime_id_get, anime_thumb, animethumbnail, eng_name, jap_name
from Bot.utils.decorators import message_status, upload_file

def image_download(link, file):
    img_data = requests.get(link).content
    with open(file, 'wb') as handler:
        handler.write(img_data)
    return file    

def status(text, anime=None, episode=None, resolution=None, file_name=None):
    s = f"**{text}**\n\n"
    if anime is not None:
        s += f"**Anime Name:** {anime}\n"
    if episode is not None:
        s += f"**Episode Number:** {episode}\n"
    if resolution is not None:
        s += f"**Resolution:** {resolution}\n"
    if file_name is not None:
        s += f"**File Name:** {file_name}"    
    return text_replace(s)

def shorten_sub(title):
    if len(title) > 29:
        heading = title[0:29]
    else:
        heading = title
    return heading
working_list = []
id_get_anime = None          
  
async def process():
    for x in AnimePahe.get_latest():
        anime_title = x.get('anime_title') 
        disc = x.get('disc')
        if ":" in anime_title:
            id_get_anime = anime_title.split(":",1)[0]
        anime_id = anime_id_get(anime_title)
        
        if anime_id is None:
            anime_id = anime_id_get(id_get_anime)
            
        episode = x.get('episode')
        if len(str(episode)) == 1:
            episode = f'0{episode}'
        episode_session = x.get('session')
        checks = check_pending(anime_title, episode)
        if checks is False: 
            print(anime_title)
            if anime_title in working_list:
                LOG.warn(f'Bot-San : This Anime already in process {anime_title}')
                return
            episode_details = AnimePahe.get_episode_links(episode_session)
            files_downloaded = [] 
            resolutions = []
            sources = episode_details.get('sources') 
            file_title = custom_file(anime_id)
            if file_title is None: 
                file_title = shorten_sub(anime_title)  
            if disc == "DVD":
                pass
            elif disc == "BD":
                pass 
            else:
                if len(sources) < 3:
                    LOG.error(f'Senpai Skipping Due To Only 1 Few {anime_title} - {episode} Episodes Available Of this anime')
                    continue
            if anime_title not in working_list:
                working_list.append(anime_title)
            for y in sources:
                url = y.get('url')
                resolution = str(y.get('quality'))
                if y.get('audio') == "japanese".lower():
                    TYPE_SEND_CAPTION = f"**[Sub]**"
                    AUDIO = "Japanese"
                else:    
                    TYPE_SEND_CAPTION = f"**[Dub]**"
                    AUDIO = 'English'
                status_resolution = check_resolution(resolution)
                if status_resolution is True:
                    file_name = f"{episode} - {file_title} [{resolution}].mp4" #FILE_NAME
                    if resolution not in resolutions:
                        resolutions.append(resolution)
                    await message_status(text_replace(status("**Downloading**", anime_title, episode, resolution, file_name)))
                    if file_name not in files_downloaded:
                        files_downloaded.append((file_name, resolution))
                        proce = await asyncio.create_subprocess_shell(f"youtube-dl --add-header Referer:'https://kwik.cx/' {url} -o '{file_name}'", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
                        await proce.communicate() 
            await message_status(text_replace(status("**Downloaded Files**", anime_title, episode)))
            UPLOAD_CHANNEL = find_channel(anime_id)
            if UPLOAD_CHANNEL is None: 
                UPLOAD_CHANNEL = ARCHIVE_CHANNEL   
            #THUMB FILE    
            file_thumb = custom_thumb(anime_id)
            if file_thumb is None: 
                file_thumb = anime_thumb(anime_title)
            if file_thumb is None: 
                file_thumb = anime_thumb(id_get_anime)
            if file_thumb is None: 
                file_thumb = anime_thumb(shorten_sub(anime_title))
            thumb_file = image_download(file_thumb, f'{anime_id}.png')     
            #WALL    
            wall = custom_wall(anime_id)
            if wall is None:
                wall = animethumbnail(anime_title) 
            if wall is None: 
                wall = animethumbnail(id_get_anime)
            if wall is None: 
                wall = animethumbnail(shorten_sub(anime_title))
                
            #CAPTION    
            anime_engname = eng_name(anime_title)
            anime_japname = jap_name(anime_title)
            CAPTION = f"**{anime_engname}** | `{anime_japname}`\n\n"
            CAPTION += f"**‣ Episode :** `{episode}`\n"
            CAPTION += f"**‣ Audio :** `{AUDIO}`\n"
            CAPTION += f"**‣ Quality :** `{', '.join(resolutions)}`\n"
            
            if AUDIO == "Japanese":
                CAPTION += "**‣ Subtitles** : `English Subs`\n"
            else:
                CAPTION += "**‣ Subtitles** : `None`\n"
            #UPLOADING    
            await message_status(text_replace(status("**Uploading Start**", anime_title, episode)))
            LINKS = []       
            for x in files_downloaded:
                try:
                    await asyncio.sleep(14)
                    video = await upload_file(x[0], UPLOAD_CHANNEL, thumb=thumb_file, caption=TYPE_SEND_CAPTION)
                    LINKS.append(IKB(text_replace(f"✨{episode}-{x[1]}✨"), url=video.link))
                except Exception as e:
                    LOG.error(f'Senpai Error: {e}')
                    pass                           
                try:
                    os.remove(x[0])
                except Exception as e:
                    LOG.error(f'Senpai Error: {e}')
                    pass                
            try:
                os.remove(thumb_file)
            except Exception as e:
                LOG.error(f'Senpai Error: {e}')
                pass                    
            await soheru.send_photo(MAIN_CHANNEL, photo=wall, caption=CAPTION,reply_markup=IKM([LINKS]))
            await message_status("**‣ sᴛᴀᴛᴜs** : `ɪᴅʟᴇ`")    
            resolutions.clear()
            files_downloaded.clear()   
            LINKS.clear() 
            new(anime_title, episode, episode_session)   
             
scheduler = AsyncIOScheduler()
scheduler.add_job(process, "interval", seconds=60)
scheduler.start()        
        
                    
                    
                
               
           
            
           
           
           
           
           
           
            
        
    
    
                
        
