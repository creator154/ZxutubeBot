import random

from pyrogram import filters as Filters
from pyrogram.types import Message

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
        has_spoiler=True,
        parse_mode="markdown",
        quote=True,
    )
