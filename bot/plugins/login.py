from pyrogram import filters as Filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from ..youtube import GoogleAuth
from ..config import Config
from ..utubebot import UtubeBot

auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
AUTH_URL = auth.GetAuthUrl()


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("login")
    & Filters.user(Config.AUTH_USERS)
)
async def login(_, m: Message):
    await m.reply_text(
        "You want to login.\n\n"
        "Click the button below to authorize your Google account.\n\n"
        "After allowing access, copy the code and send:\n\n"
        "`/authorise YOUR_CODE`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔑 Authentication URL",
                        url=AUTH_URL
                    )
                ]
            ]
        )
    )
