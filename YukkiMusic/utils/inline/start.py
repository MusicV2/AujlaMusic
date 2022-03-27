#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        

                [InlineKeyboardButton("💌𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨✍️", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "❤️𝗚𝗿𝗼𝘂𝗽❤️", url=f"https://t.me/Punjabi_ChatGroup"

                    ),

                    InlineKeyboardButton(

                        "❤️𝗢𝘄𝗻𝗲𝗿❤️", url=f"https://t.me/PB_65_Aujla"

                    ),

                ],
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [

                    InlineKeyboardButton(

                        "😍➕ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ➕😍",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("💌𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨✍️", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "❤️𝗚𝗿𝗼𝘂𝗽❤️", url=f"https://t.me/Punjabi_ChatGroup"

                    ),

                    InlineKeyboardButton(

                        "❤️𝗢𝘄𝗻𝗲𝗿❱❤️", url=f"https://t.me/PB_65_Aujla"

                    ),

                ],
        [InlineKeyboardButton("🇮🇳 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚 🇮🇳", callback_data="LG")],
    ]
  
    return buttons
