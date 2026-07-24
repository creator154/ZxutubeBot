import random

from pyrogram import filters as Filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)

from ..translations import Messages as tr
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
)
async def start(c: UtubeBot, m: Message):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔐 Login", callback_data="login"),
                InlineKeyboardButton("📖 Help", callback_data="help"),
            ]
        ]
    )

    await m.reply_chat_action("upload_photo")

    await m.reply_photo(
        photo=random.choice(tr.IMAGE_LIST),
        caption=tr.START_MSG.format(m.from_user.first_name),
        reply_markup=buttons,
        quote=True,
    )
