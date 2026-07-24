class Messages:

    IMAGE_LIST = [
        "https://files.catbox.moe/vg3vae.jpg"
    ]

    START_MSG = (
        "<b>👋 Hi there {} 🇮🇳</b>\n\n"

        "<b>🎬 I'm YouTube Uploader Bot</b>\n\n"

        "<b>✨ Features</b>\n"
        "• Upload Telegram videos to YouTube\n"
        "• Fast & Easy Uploads\n"
        "• Google Authentication Support\n\n"

        "<b>📌 Commands</b>\n"
        "/login - Login with Google\n"
        "/help - Help Menu\n"
        "/upload - Upload replied video\n\n"

        "<b>🚀 Enjoy Uploading!</b>"
    )

    HELP_MSG = [
        ".",

        "Welcome!\n\nThis bot uploads Telegram videos directly to YouTube.",

        "<b>Step 1</b>\nAuthenticate using Google.\n\n"
        "<b>Step 2</b>\nForward a video.\n\n"
        "<b>Step 3</b>\nReply with /upload.\n\n"
        "<b>Step 4</b>\nWait for upload.\n\n"
        "<b>Step 5</b>\nReceive the YouTube link.",

        "<b>Create a YouTube Channel</b>\n\n"
        "Create a channel if you don't already have one.",

        "<b>Verify your YouTube Account</b>\n\n"
        "Verification allows uploads longer than 15 minutes.",

        "<b>Authentication</b>\n\n"
        "Open the authentication page and send:\n\n"
        "<code>/authorise YOUR_CODE</code>"
    ]

    NOT_A_REPLY_MSG = "Please reply to a video."

    NOT_A_MEDIA_MSG = "No media found. Please reply to a video."

    NOT_A_VALID_MEDIA_MSG = "Invalid media."

    DAILY_QOUTA_REACHED = (
        "You have reached YouTube's daily upload limit."
    )

    PROCESSING = "⏳ <b>Processing...</b>"

    NOT_AUTHENTICATED_MSG = (
        "❌ <b>You are not authenticated.</b>\nUse /login first."
    )

    NO_AUTH_CODE_MSG = "Please provide the authentication code."

    AUTH_SUCCESS_MSG = (
        "✅ <b>Authentication Successful!</b>\n\nHappy Uploading 🎉"
    )

    AUTH_FAILED_MSG = (
        "❌ <b>Authentication Failed!</b>\n\n{}"
    )

    AUTH_DATA_SAVE_SUCCESS = (
        "✅ <b>Authentication data saved successfully.</b>"
    )
