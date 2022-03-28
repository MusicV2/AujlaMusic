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

                        "🧑‍🤝‍🧑𝔾ℝ𝕆𝕌ℙ👭", url=f"https://t.me/Punjabi_ChatGroup"

                    ),

                    InlineKeyboardButton(

                        "❤️🅢🅣🅐🅣🅤🅢❤️", url=f"https://t.me/Punjabi_Status_Mania"

                    ),

                ],
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [

                    InlineKeyboardButton(

                        "🌹➕ คdd мε тσ ყσuя gяσup ➕🌾",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("💌𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨✍️", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "🧑‍🤝‍🧑𝔾ℝ𝕆𝕌ℙ👭", url=f"https://t.me/Punjabi_ChatGroup"

                    ),

                    InlineKeyboardButton(

                        "❤️🅞🅦🅝🅔🅡❤️", url=f"https://t.me/PB_65_Aujla"

                    ),

                ],
        [InlineKeyboardButton("🇮🇳 🄻🄰🄽🄶🅄🄰🄶🄴 🇮🇳", callback_data="LG")],
    ]
  
    return buttons
