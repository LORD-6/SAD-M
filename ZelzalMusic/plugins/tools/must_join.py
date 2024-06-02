from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/lMySad":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("lMySad", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/lMySad".isalpha():
                link = "https://t.me/lMySad"
            else:
                chat_info = await bot.get_chat("lMySad")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\n⌯︙قناة البوت: @lMySad .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("𝚜𝚘𝚞𝚛𝚌𝚎 𝚛𝚎𝚍", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @lMySad !")