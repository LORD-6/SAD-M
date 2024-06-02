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
    command(["مستر لورد","لورد","المطور لورد"]))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/M_R_C2",
        caption=f"""𝅄 𓏺 𝖭𝖺𝗆𝖾 : › 𝖬𝖱 𝖫𝖮𝖱𝖣
𝅄 𓏺 𝖴𝗌𝖾𝗋 : › @M_R_C2
𝅄 𓏺 𝖲𝗈𝗎𝗋𝖼𝖾 : › @M_R_ZC
𝅄 𓏺 𝖡𝗂𝗈 : › 𝖬𝗒 𝖡𝗋𝗈 : › « @MR_1X0 » 𓏺 « @P_O_C » 𓏺 « @M_Lr1 » ᯾ 𝖬𝗒 𝖶𝗈𝗋𝗅𝖽 : › « @OOOJ30 »""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩👨‍💻︙مطور الـسـورس 𓆪", url=f"https://t.me/M_R_C2"),
            ]
         ]
     )
  )
  
