import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["مستر ساد","ساد","عمك ساد","الهيبه ساد","مالك البوت","المطور","مطور"]))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/XovoX8",
        caption=f"""𝅄 𓏺 𝖭𝖺𝗆𝖾 : › 𓏺 Sad Planet .
𝅄 𓏺 𝖴𝗌𝖾𝗋 : › @XovoX8
𝅄 𓏺 𝖲𝗈𝗎𝗋𝖼𝖾 : › @lMySad
𝅄 𓏺 𝖡𝗂𝗈 : › His iraqelc.t.me are a world, and I am iraqolu.t.me in his lMySad.t.me place J_T_H.t.me , an Qraiin.t.me ٫ Ch iraqelu.t.me .HoT_FTer.t.me ؛R""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 الـمـطـور 𓆪", url=f"https://t.me/XovoX8"),
            ]
         ]
     )
  )
  
