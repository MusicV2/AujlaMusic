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
        

                [InlineKeyboardButton("๐๐พ๐ค๐ข๐ข๐๐ฃ๐๐จโ๏ธ", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "๐งโ๐คโ๐ง๐พโ๐๐โ๐ญ", url=f"https://t.me/Punjabi_ChatGroup"

                    ),

                    InlineKeyboardButton(

                        "๐ฌ๐ข๐ฃ๐๐ฃ๐ค๐ข๐ฅ", url=f"https://t.me/Punjabi_Status_Mania"

                    ),

                ],
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [

                    InlineKeyboardButton(

                        "๐นโ เธdd ะผฮต ัฯ แงฯuั gัฯup โ๐พ",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("๐๐พ๐ค๐ข๐ข๐๐ฃ๐๐จโ๏ธ", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "๐งโ๐คโ๐ง๐พโ๐๐โ๐ญ", url=f"https://t.me/Punjabi_ChatGroup"

                    ),

                    InlineKeyboardButton(

                        "โค๏ธ๐๐ฆ๐๐๐กโค๏ธ", url=f"https://t.me/PB_65_Aujla"

                    ),

                ],
        [InlineKeyboardButton("๐ฎ๐ณ ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด ๐ฎ๐ณ", callback_data="LG")],
    ]
  
    return buttons
