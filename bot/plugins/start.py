import random

from pyrogram import filters as Filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
    & Filters.user(Config.AUTH_USERS)
)
async def start(c: UtubeBot, m: Message):

    await m.reply_photo(
        photo=random.choice(tr.IMAGE_LIST),
        caption=tr.START_MSG.format(m.from_user.first_name),
        parse_mode=ParseMode.HTML,
        has_spoiler=True,
        quote=True
    )
