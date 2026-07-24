import random

from pyrogram import filters as Filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)

from ..translations import Messages as tr
from ..auth_store import auth_filter, add_broadcast_user
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
    & auth_filter
)
async def _start(c: UtubeBot, m: Message):
    add_broadcast_user(m.from_user.id)

    await m.reply_chat_action("typing")

    caption = f"""
<b>Hi there {m.from_user.mention} 🇮🇳.</b>

I'm <b>YouTube Uploader Bot</b>. Made with ❤️ by @SumitTripathi.

You can use me to upload any Telegram video to YouTube once you authorise me.

📖 You can know more from /help.
🔐 Or use /login to get started.
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔐 Login", callback_data="login"),
                InlineKeyboardButton("📖 Help", callback_data="help")
            ],
            [
                InlineKeyboardButton(
                    "👨‍💻 Developer",
                    url="https://t.me/HeySumit"
                )
            ]
        ]
    )

    await m.reply_photo(
        photo=random.choice(tr.IMAGE_LIST),
        caption=caption,
        reply_markup=buttons,
        quote=True
    )
