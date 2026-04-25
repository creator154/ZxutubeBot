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
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message

    async def _upload(self) -> None:
        try:
            loop = asyncio.get_running_loop()

            auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)

            if not os.path.isfile(Config.CRED_FILE):
                log.debug(f"{Config.CRED_FILE} does not exist")
                self.status = False
                self.message = "❌ Upload failed: Bot is not authenticated."
                return

            auth.LoadCredentialsFile(Config.CRED_FILE)
            google = await loop.run_in_executor(None, auth.authorize)

            # Category
            if Config.VIDEO_CATEGORY and Config.VIDEO_CATEGORY in self.video_category:
                categoryId = Config.VIDEO_CATEGORY
            else:
                categoryId = random.choice(list(self.video_category))

            categoryName = self.video_category[categoryId]

            # Title
            title = self.title if self.title else os.path.basename(self.file)
            title = (
                (Config.VIDEO_TITLE_PREFIX + title + Config.VIDEO_TITLE_SUFFIX)
                .replace("<", "")
                .replace(">", "")[:100]
            )

            # Description
            description = (
                Config.VIDEO_DESCRIPTION
                + "\nUploaded via Telegram Bot"
            )[:5000]

            # Privacy
            privacyStatus = Config.UPLOAD_MODE if Config.UPLOAD_MODE else "private"

            properties = dict(
                title=title,
                description=description,
                category=categoryId,
                privacyStatus=privacyStatus,
            )

            log.debug(f"Uploading {self.file} with {properties}")

            youtube = YouTube(google)

            response = await loop.run_in_executor(
                None, youtube.upload_video, self.file, properties
            )

            log.debug(response)

            # ✅ LINK FIX
            video_id = response.get("id")

            if video_id:
                url = f"https://www.youtube.com/watch?v={video_id}"
                self.status = True
                self.message = (
                    f"✅ Uploaded Successfully!\n\n"
                    f"🎬 Title: {title}\n"
                    f"📂 Category: {categoryName}\n"
                    f"🔒 Privacy: {privacyStatus}\n"
                    f"🔗 Link: {url}"
                )
            else:
                self.status = False
                self.message = "❌ Upload hua but video ID nahi mila"

        except Exception as e:
            log.error(e, exc_info=True)
            self.status = False
            self.message = f"❌ Upload failed!\nError: {e}"
