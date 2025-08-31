from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 Hᴇʏ, </b>{}\n 
<b>I'ᴍ ғᴀsᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴄᴏɴᴛᴇɴᴛ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ 😎</b>\n
<b>🧿 ᴘʟᴇᴀsᴇ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ɪɴ ʟɪᴍɪᴛ 😒</b>\n\n
<b><a href='https://yashyasag.github.io/hiddens_officials'>🔥𝗖𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗠𝘆 𝗙𝗿𝗲𝗲 𝗪𝗲𝗯𝘀𝗶𝘁𝗲𝘀 🥰</a></b>\n\n
<b>💝 @{}</b>\n"""

    HELP_TEXT = """
<b>𝗜 𝗮𝗺 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 𝗯𝗼𝘁 🔥</b>
<b>🔹 sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅᴏᴄᴜᴍᴇɴᴛ ᴏʀ ᴍᴇᴅɪᴀ</b>
<b>🔹 ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʟɪɴᴋ</b>\n
<b>🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.</b>\n
<i><b>‼️ ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴛᴏ <a href='https://telegram.me/HACKHEISTBOT'>𝗛𝗔𝗖𝗞𝗛𝗘𝗜𝗦𝗧</a></b></i>"""

    ABOUT_TEXT = """
<b>⚜ ᴍʏ ɴᴀᴍᴇ : {}</b>\n
<b>✦ ᴍᴀᴅᴇ ʙʏ  : ℍ𝔸ℂ𝕂ℍ𝔼𝕀𝕊𝕋</b>
<b>🔹 ᴡᴇʙsɪᴛᴇs ➪ <a href='https://yashyasag.github.io/hiddens_officials'>𝗙𝗥𝗘𝗘 𝗪𝗘𝗕𝗦 🔥</a></b>\n
"""

    STREAM_TEXT = """
<i><u>𝗟𝗲 𝗞𝗮𝗿𝗹𝗲 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 😒</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b><a href='https://yashyasag.github.io/hiddens_officials'>{}</a></b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🖥 Wᴀᴛᴄʜ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>𝗟𝗲 𝗞𝗮𝗿𝗹𝗲 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 😒</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b><a href='https://yashyasag.github.io/hiddens_officials'>{}</a></b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""


    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗛𝗔𝗖𝗞𝗛𝗘𝗜𝗦𝗧](tg://user?id={}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

class BUTTON(object):    
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
