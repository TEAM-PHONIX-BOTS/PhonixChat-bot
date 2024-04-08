import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from phonix import BOT_NAME, VENOM
from phonix.database.chats import add_served_chat
from phonix.database.users import add_served_user
from phonix.modules.helpers import PNG_BTN


@VENOM.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɢɢɢɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"ʜᴇʏ sʜᴏɴᴀ💞!!\n{BOT_NAME} ᴢɪɴᴅᴀ ʜᴀɪ ᴀᴜʀ ᴀᴄʜᴇ sᴇ ᴡᴏʀᴋ ᴋᴀʀ ʀᴀʜᴀ ʜᴀɪ\n➥ `{ms}` ms\n\n<b>|| ᴍᴀᴅᴇ ʙʏ [ᴏᴡɴᴇʀ](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
