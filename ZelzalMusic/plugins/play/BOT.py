import asyncio
import random
from pyrogram import enums
from pyrogram import types
from ZelzalMusic.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from ZelzalMusic import app
from config import *

bot_name = {}

name = "فوكس"

@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

caesar_responses = [
    "اسمي {name} يصحبي 💘 ⋅",
    "يسطا قولتلك اسمي {name } ☺️",
    "ايه يا زميلي 😂♥️ ،",
    "قلب البوت 🥹💘 ⋅",
    "ثانية بشقط واحدة تانية 😂💘 ،",
    "يعم والله بحبك بس ناديلي بـ {name} 🙂",
    "ايه يا معلم مين مزعلك",
    "ايوه جاي 😂♥️ ،",
    "تًبا لك ماذا تريد من امي 🙂",
    "يسطا هوا عشان بحبك تصدعني؟",
    "تعرف بالله هحبك أكتر لو ناديتلي {name} 🥹💘",
    "اي ي معلم مين مزعلك؟",
    "متصلي على النبي كدا💘 ⋅",
    "مش فاضيلك نصايه وكلمني ☺ .",
    "انجز عايزني أشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا 😂♥ ,",
]

@app.on_message(filters.command(["بوت", "البوت"], ""), group=71135)
async def caesar_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(caesar_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك 🫣♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
    parse_mode=enums.ParseMode.MARKDOWN)
