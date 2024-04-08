import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from phonix import BOT_NAME, VENOM, VENOM
from phonix.database.chats import add_served_chat
from phonix.database.users import add_served_user
from phonix.modules.helpers import (
    CLOSE_BTN,
    VENOM_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@VENOM.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("ʙᴏᴏᴛɪɴɢ....")
        await asyncio.sleep(0.2)
        await accha.edit("ʙᴏᴏᴛɪɴɢ..")
        await asyncio.sleep(0.2)
        await accha.edit("ʙᴏᴏᴛɪɴɢ....")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**ʜᴇʏ ɪ'ᴍ {BOT_NAME}**\n**ᴄᴀɴ ɪ ʜᴇʟᴘ ʏᴏᴜ ᴀᴄᴛɪᴠᴀᴛᴇ ᴛʜᴇ ɢʀᴏᴜᴘ?.\n.\nɪ ᴄᴀɴ ᴡᴏʀᴋ 𝟸𝟺/𝟽.\nᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴄʜᴀᴛ-ʙᴏᴛ.\nᴀᴅᴅ-ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙᴇ.**\n**──────────────**\n****\n**──────────────**\n**ᴜsᴇ /chatbot [on/off]**\n<b>||ғᴏʀ /help ||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@VENOM.on_message(filters.command(["help"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def help(client: VENOM, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ\n ᴘʟs ᴜsᴇ ᴍᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ ғᴏʀ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@VENOM.on_message(filters.command("repo") & ~filters.bot)
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@VENOM.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
