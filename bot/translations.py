class Messages:

    IMAGE_LIST = [
        "https://files.catbox.moe/vg3vae.jpg"
    ]

    START_MSG = (
        "**Hi there {} 🇮🇳.**\n\n"

        "**I'm YouTube Uploader Bot. Made with ❤️ by @SumitTripathi.** "
        "You can use me to upload any Telegram video to YouTube once you authorise me.\n\n"

        "**You can know more from** /help.\n"
        "**Or use** /login **to get started.**"
    )

    HELP_MSG = [
        ".",
        "Hi there.\n\nFirst things first. You should be aware that YouTube processes every uploaded video. Copyrighted videos may be blocked or removed.",

        "**Let's learn how I work.**\n\n"
        "**Step 1:** Authorise me using Google.\n"
        "**Step 2:** Forward any Telegram video.\n"
        "**Step 3:** Reply `/upload` to the video.\n"
        "**Step 4:** I upload it to YouTube.\n"
        "**Step 5:** I send you the YouTube link.",

        "**Create a YouTube Channel**\n\n"
        "If you don't have a channel, create one before using me.",

        "**Verify your YouTube Account**\n\n"
        "Verification allows uploading videos longer than 15 minutes.",

        "**Now let's Authorise.**\n\n"
        "Click the Authentication URL button below.\n"
        "Allow access and copy the code.\n"
        "Then send:\n\n"
        "`/authorise YOUR_CODE`"
    ]

    NOT_A_REPLY_MSG = "Please reply to a video."

    NOT_A_MEDIA_MSG = "No media found. Please reply to a video."

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media."

    DAILY_QOUTA_REACHED = (
        "Looks like you've reached YouTube's daily upload limit."
    )

    PROCESSING = "
