import random

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    filters.private
    & filters.incoming
    & filters.command("start")
    & filters.user(Config.AUTH_USERS)
)
async def start(c: UtubeBot, m: Message):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔐 Login",
                    callback_data="login"
                ),
                InlineKeyboardButton(
                    "📖 Help",
                    callback_data="help"
                ),
            ]
        ]
    )

    await m.reply_photo(
        photo=random.choice(tr.IMAGE_LIST),
        caption=tr.START_MSG.format(
            m.from_user.mention
        ),
        has_spoiler=True,
        reply_markup=buttons,
    )
