import random

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from ..translations import Messages as tr
from ..utubebot import UtubeBot


@UtubeBot.on_message(filters.private & filters.command("start"))
async def start(_, m: Message):
    caption = f"""
<b>Hi there {m.from_user.mention} 👋</b>

🎬 <b>Welcome to YouTube Uploader Bot</b>

This bot can upload your Telegram videos directly to YouTube.

📌 Commands:
/login - Login with Google
/help - Help
/cancel - Cancel current task
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔐 Login", callback_data="login"),
                InlineKeyboardButton("📖 Help", callback_data="help")
            ],
            [
                InlineKeyboardButton(
                    "🌐 Source",
                    url="https://github.com/creator154/ZxutubeBot"
                )
            ]
        ]
    )

    await m.reply_photo(
        photo=random.choice(tr.IMAGE_LIST),
        caption=caption,
        reply_markup=buttons
    )
