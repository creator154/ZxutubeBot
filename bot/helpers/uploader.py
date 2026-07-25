import os
import random
import asyncio
import logging
from typing import Optional, Tuple

from ..youtube import GoogleAuth, YouTube
from ..config import Config

log = logging.getLogger(__name__)


class Uploader:
    def __init__(self, file: str, title: Optional[str] = None):
        self.file = file
        self.title = title

        self.video_category = {
            1: "Film & Animation",
            2: "Autos & Vehicles",
            10: "Music",
            15: "Pets & Animal",
            17: "Sports",
            19: "Travel & Events",
            20: "Gaming",
            22: "People & Blogs",
            23: "Comedy",
            24: "Entertainment",
            25: "News & Politics",
            26: "Howto & Style",
            27: "Education",
            28: "Science & Technology",
            29: "Nonprofits & Activism",
        }

    async def start(self, progress: callable = None, *args) -> Tuple[bool, str]:
        try:
            loop = asyncio.get_running_loop()

            auth = GoogleAuth(
                Config.CLIENT_ID,
                Config.CLIENT_SECRET
            )

            if not os.path.isfile(Config.CRED_FILE):
                return False, "Upload failed because you did not authenticate me."

            auth.LoadCredentialsFile(Config.CRED_FILE)
            google = await loop.run_in_executor(None, auth.authorize)

            if Config.VIDEO_CATEGORY in self.video_category:
                categoryId = Config.VIDEO_CATEGORY
            else:
                categoryId = random.choice(list(self.video_category.keys()))

            categoryName = self.video_category[categoryId]

            title = self.title if self.title else os.path.basename(self.file)
            title = (
                Config.VIDEO_TITLE_PREFIX
                + title
                + Config.VIDEO_TITLE_SUFFIX
            ).replace("<", "").replace(">", "")[:100]

            description = Config.VIDEO_DESCRIPTION[:5000]

            privacyStatus = (
                Config.UPLOAD_MODE if Config.UPLOAD_MODE else "private"
            )

            properties = {
                "title": title,
                "description": description,
                "category": categoryId,
                "privacyStatus": privacyStatus,
            }

            youtube = YouTube(google)

            response = await loop.run_in_executor(
                None,
                youtube.upload_video,
                self.file,
                properties,
            )

            if not response:
                return False, "Upload failed! No response from YouTube."

            video_id = response.get("id")

            if not video_id:
                return False, f"Upload completed but video id not found.\nResponse:\n{response}"

            youtube_url = f"https://youtu.be/{video_id}"

            message = (
                "✅ **ᴜᴘʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇ!**\n\n"
                f"🎬 **Title:** {title}\n\n"
                f"🔗 **Link:** {youtube_url}\n\n"
                f"📂 **Category:** {categoryName} ({categoryId})"
            )

            return True, message

        except Exception as e:
            log.exception(e)
            return False, f"Error occurred during upload.\n\n{e}"
