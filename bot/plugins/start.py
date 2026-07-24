from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

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

    await m.reply_photo(
        photo=tr.IMAGE,
        has_spoiler=True,
        caption=tr.START_MSG.format(m.from_user.first_name),
        parse_mode=ParseMode.HTML
)
