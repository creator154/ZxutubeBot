import os
import random
import asyncio
import logging
from typing import Optional, Tuple

from..youtube import GoogleAuth, YouTube
from..config import Config

log = logging.getLogger(__name__)

class Uploader:
    def __init__(self, file: str, title: Optional[str] = None):
        self.file = file
        self.title = title
        self.video_category = {
            1: "Film & Animation", 2: "Autos & Vehicles", 10: "Music", 15: "Pets & Animal",
            17: "Sports", 19: "Travel & Events", 20: "Gaming", 22: "People & Blogs",
            23: "Comedy", 24: "Entertainment", 25: "News & Politics", 26: "Howto & Style",
            27: "Education", 28: "Science & Technology", 29: "Nonprofits & Activism",
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
                self.status = False
                self.message = "Upload failed because you did not authenticate me."
                return

            auth.LoadCredentialsFile(Config.CRED_FILE)
            google = await loop.run_in_executor(None, auth.authorize)

            categoryId = Config.VIDEO_CATEGORY if Config.VIDEO_CATEGORY in self.video_category else random.choice(list(self.video_category))
            categoryName = self.video_category[categoryId]

            title = self.title if self.title else os.path.basename(self.file)
            title = (Config.VIDEO_TITLE_PREFIX + title + Config.VIDEO_TITLE_SUFFIX).replace("<", "").replace(">", "")[:100]
            description = (Config.VIDEO_DESCRIPTION)[:5000]
            privacyStatus = "private" if not Config.UPLOAD_MODE else Config.UPLOAD_MODE

            properties = dict(title=title, description=description, category=categoryId, privacyStatus=privacyStatus)
            log.debug(f"payload for {self.file} : {properties}")

            youtube = YouTube(google)
            video_id = await loop.run_in_executor(None, youtube.upload_video, self.file, properties) # <-- Direct ID aa rahi hai

            if not video_id:
                raise Exception("Video ID not returned from YouTube")

            video_url = f"https://youtu.be/{video_id}"
            log.info(f"Upload successful: {video_url}")

            self.status = True
            self.message = video_url # <-- Sirf URL return

        except Exception as e:
            log.error(e, exc_info=True)
            self.status = False
            self.message = f"Error occurred during upload.\nError: {e}"
