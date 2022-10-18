import os 
import random 
from Bot import LOG, soheru
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from Bot.database.client import check_resolution, currentformat, enable_resolution, update_format

from Bot.database.users import get_auth, is_reg, new_user
from Bot.plugins.font_change import text_replace 


LINK = [
    'https://telegra.ph/file/9e41b263e3a1fe8568427.jpg', 
    'https://telegra.ph/file/2f4928545aa5447d03af1.jpg', 
    'https://telegra.ph/file/2c5a59a07a9c9ebae64d6.jpg', 
    'https://telegra.ph/file/53ac0b5f9be1bd3067db0.jpg',
    'https://telegra.ph/file/a1226c66325921bd77a80.jpg',
    'https://telegra.ph/file/e27dcf346ae2d39d4919b.jpg',
]


BUTTONS_DEV = IKM(
    [
        [
            IKB('ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/sohailkhan_indianime'),
            IKB('ɢɪᴛʜᴜʙ', url = 'https://github.com/soheru')
        ],
        [
            IKB('ᴡᴇʙsɪᴛᴇ', url='https://soheru.in'),
            IKB('ᴄʜᴀɴɴᴇʟ', url='https://t.me/aboutmesk'),
        ],
        [
            IKB('ɪɴsᴛᴀɢʀᴀᴍ', url='https://instagram.com/soherusan'),
            IKB('ʜᴏᴍᴇ', 'call_start_or_go_back')
        ]
    ]
)

BUTTONSS = IKM(
    [
        [
            IKB(text_replace('Enable 360p'), 'function_enable_360p'),
            IKB(text_replace('Enable 720p'), 'function_enable_720p'),
            IKB(text_replace('Enable 1080p'), 'function_enable_1080p'),
        ], 
        [
            IKB(text_replace('Disable 360p'), 'function_disable_360p'),
            IKB(text_replace('Disable 720p'), 'function_disable_720p'),
            IKB(text_replace('Disable 1080p'), 'function_disable_1080p'),
        ], 
        [
            IKB(text_replace('Current_Settings'), 'function_current_settings'),
        ],
    ]
)

@soheru.on_callback_query(filters.regex('call'))
async def call_callback(client:soheru, callback_query):
    if 'about_dev' in callback_query.data:
        text = f'Hello `{callback_query.from_user.first_name}`,\n\n'
        text += "I'm Sohail\nTo connect with me, Check Below Buttons"
        await callback_query.message.edit(text_replace(text),reply_markup=BUTTONS_DEV)
        
    elif 'start_or_go_back' in callback_query.data:
        text = f"**Hi There {callback_query.message.from_user.first_name}**,\n\n"
        text += f"**Yup Waccha Lookin Here?**"
        await callback_query.message.edit(text_replace(text), reply_markup=BUTTONSS)    

@soheru.on_callback_query(filters.regex('function'))
async def call_callback(client:soheru, callback_query):
    if get_auth(callback_query.from_user.id) is False:
        await callback_query.answer(text_replace('You\'re not authorized'))
        return 
    
    if 'enable_360p' in callback_query.data:
        if check_resolution('360p') is False:
            enable_resolution('360p', True)
            await callback_query.answer(text_replace('Enabled 360p'))
        else:
            await callback_query.answer(text_replace('Already Enabled'))
    elif 'enable_720p' in callback_query.data:
        if check_resolution('720p') is False:
            enable_resolution('720p', True)
            await callback_query.answer(text_replace('Enabled 720p'))
        else:
            await callback_query.answer(text_replace('Already Enabled'))        
    elif 'enable_1080p' in callback_query.data:
        if check_resolution('1080p') is False:
            enable_resolution('1080p', True)
            await callback_query.answer(text_replace('Enabled 1080p'))
        else:
            await callback_query.answer(text_replace('Already Enabled'))        
    
    elif 'disable_360p' in callback_query.data:
        if check_resolution('360p') is True:
            enable_resolution('360p', False)
            await callback_query.answer(text_replace('Disable 360p'))
        else:
            await callback_query.answer(text_replace('Already Disabled'))
    elif 'disable_720p' in callback_query.data:
        if check_resolution('720p') is True:
            enable_resolution('720p', False)
            await callback_query.answer(text_replace('Disable 720p'))
        else:
            await callback_query.answer(text_replace('Already Disabled'))   
                 
    elif 'disable_1080p' in callback_query.data:
        if check_resolution('1080p') is True:
            enable_resolution('1080p', False)
            await callback_query.answer(text_replace('Disable 1080p'))
        else:
            await callback_query.answer(text_replace('Already Disabled'))    
            
    elif 'help' in callback_query.data:
        await callback_query.message.edit(text_replace('Checkout Plugins'), reply_markup=BUTTONSS)
                             
    elif 'current_settings' in callback_query.data:
        text = "\n\n**360p is enabled? : **" + str(check_resolution('360p'))
        text += "\n**720p is enabled? : **" + str(check_resolution('720p'))
        text += "\n**1080p is enabled? : **" + str(check_resolution('1080p'))
        await callback_query.message.edit(text_replace(text), reply_markup=BUTTONSS)
    
@soheru.on_message(filters.command('start', prefixes="!"))
async def start_bot(client:soheru, message:Message):
    if is_reg(message.from_user.id) is False:
        new_user(message.from_user.id, False)
    
    text = f"**Hi There {message.from_user.first_name}**,\n\n"
    text += f"**Yup Waccha Lookin Here?**"
    button = IKM(
        [
            [
                IKB(text_replace('help'), 'function_help'),
                IKB(text_replace('Developer'), 'call_about_dev')
            ]
        ]
    )
    try:
        await message.reply_photo(random.choice(LINK), caption=text, reply_markup=button)
    except Exception as e:
        LOG.warn(e)
    
    