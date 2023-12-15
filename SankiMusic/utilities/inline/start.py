from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ 🥀 ",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇꜱ 🎊", url=f"https://t.me/GJ516_DISCUSS_GROUP"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘ 📈",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ 🥀", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇꜱ 🎊", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Oᴡɴᴇʀ ⛵", url="https://t.me/lippsxd"
            )
        ]
     ]
    return buttons
