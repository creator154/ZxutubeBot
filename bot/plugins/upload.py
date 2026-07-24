import os
import time
import string
import random
import logging
import asyncio
import datetime
from typing import Union

from pyrogram import StopTransmission
from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from..translations import Messages as tr
from..helpers.downloader import Downloader
from..helpers.uploader import Uploader
from..config import Config
from..utubebot import UtubeBot

log = logging.getLogger(__name__)

@UtubeBot.on_message(Filters.private & Filters.incoming & Filters.command("upload") & Filters.user(Config.AUTH_USERS))
async def _upload(c: UtubeBot, m: Message):

    if not os.path.exists(Config.CRED_FILE): return await m.reply_text(tr.NOT_AUTHENTICATED_MSG)
    if not m.reply_to_message: return await m.reply_text(tr.NOT_A_REPLY_MSG)

    message = m.reply_to_message
    if not message.media: return await m.reply_text(tr.NOT_A_MEDIA_MSG)
    if not valid_media(message): return await m.reply_text(tr.NOT_A_VALID_MEDIA_MSG)

    snt = await m.reply_text("⏳ **ᴘʀᴏᴄᴇssɪɴɢ...**")
    c.counter += 1

    download_id = get_download_id(c.download_controller)
    c.download_controller[download_id] = True

    download = Downloader(m)
    status, file = await download.start(progress, snt, c, download_id)
    c.download_controller.pop(download_id, None)

    if not status:
        c.counter -= 1
        return await snt.edit_text(file)

    await snt.edit_text("📥 **ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇ**\n\n📤 **ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ʏᴏᴜᴛᴜʙᴇ...**")

    title = " ".join(m.command[1:]) or f"Uploaded_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    upload = Uploader(file, title)
    status, link = await upload.start(progress, snt)

    if os.path.exists(file): os.remove(file)

    if not status:
        c.counter -= 1
        return await snt.edit_text(f"❌ **ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ**\n\n`{link}`")

    # link me se url nikalna hai button ke liye
    youtube_url = link.split("Link: ")[1].split("\n")[0]

    await snt.edit_text(
        f"**✅ ᴜᴘʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇ**\n\n{link}",
        parse_mode="markdown",
        disable_web_page_preview=False,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("▶️ Watch on YouTube", url=youtube_url)]])
    )
    c.counter -= 1

def get_download_id(storage: dict) -> str:
    while True:
        download_id = "".join(random.choice(string.ascii_letters) for _ in range(3))
        if download_id not in storage: return download_id

def valid_media(media: Message) -> bool:
    return bool(media.video or media.video_note or media.animation or (media.document and "video" in media.document.mime_type))

def human_bytes(num: Union[int, float], split: bool = False):
    base, suffix = 1024.0, ["B","KB","MB","GB","TB"]
    for unit in suffix:
        if abs(num) < base: return (round(num,2), unit) if split else f"{round(num,2)} {unit}"
        num /= base

async def progress(cur, tot, start_time, status, snt, c, download_id):
    if not c.download_controller.get(download_id): raise StopTransmission
    try:
        diff = time.time() - start_time
        if diff < 1: diff = 1
        if int(time.time()) % 3 == 0 or cur == tot:
            await asyncio.sleep(0.5)
            speed, unit = human_bytes(cur / diff, True)
            text = f"**{status}**\n\nProgress: {round((cur*100)/tot,2)}%\n{human_bytes(cur)} / {human_bytes(tot)}\nSpeed: {speed} {unit}/s"
            await snt.edit_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", f"cncl+{download_id}")]]))
    except Exception: pass
