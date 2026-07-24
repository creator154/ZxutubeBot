class Messages:

    IMAGE_LIST = [
        "https://files.catbox.moe/vg3vae.jpg"
    ]

    START_MSG = (
        "👋 **Hi there {} 🇮🇳**\n\n"

        "**I'm YouTube Uploader Bot.** ❤️\n\n"

        "**Made with ❤️ by @SumitTripathi.**\n\n"

        "📤 **I can upload your Telegram videos directly to YouTube after authentication.**\n\n"

        "**✨ Available Commands:**\n"
        "• **/login** - Login with Google Account\n"
        "• **/help** - Help & User Guide\n"
        "• **/upload** - Upload a replied video\n"
        "• **/cancel** - Cancel current upload\n\n"

        "**🚀 Get started by using /login.**"
    )

    HELP_MSG = [
        ".",
        "Hi there.\n\nFirst things first. You should be aware that YouTube processes every uploaded video and may detect copyrighted content automatically.",
        "**Step 1:** Authenticate the bot.\n\n**Step 2:** Forward a Telegram video.\n\n**Step 3:** Reply `/upload` to the video.\n\n**Step 4:** Wait for upload.\n\n**Step 5:** Receive the YouTube link.",
        "**Create a YouTube Channel**\n\nCreate a YouTube channel before using this bot.",
        "**Verify your YouTube Account**\n\nVerify your account to upload videos longer than 15 minutes.",
        "**Authentication**\n\nOpen the authentication URL and send:\n\n`/authorise your_code`",
    ]

    NOT_A_REPLY_MSG = "Please reply to a video."
    NOT_A_MEDIA_MSG = "No media found. Please reply to a video."
    NOT_A_VALID_MEDIA_MSG = "Invalid media."

    DAILY_QOUTA_REACHED = (
        "You have reached today's YouTube upload limit."
    )

    PROCESSING = "⏳ **Processing... Please wait.**"

    NOT_AUTHENTICATED_MSG = (
        "❌ You are not authenticated.\nUse **/login** first."
    )

    NO_AUTH_CODE_MSG = "Please provide the authentication code."

    AUTH_SUCCESS_MSG = (
        "✅ Authentication successful!\nYou can now upload videos."
    )

    AUTH_FAILED_MSG = "❌ Authentication failed.\n\n{}"

    AUTH_DATA_SAVE_SUCCESS = (
        "✅ Authentication data saved successfully."
    )
