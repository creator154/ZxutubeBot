class Messages:

    IMAGE_LIST = [
        "https://files.catbox.moe/vg3vae.jpg"
    ]

    START_MSG = (
        "<blockquote>"
        "<b>👋 ʜᴇʟʟᴏ {}!</b>\n\n"

        "<b>🎬 ʏᴏᴜᴛᴜʙᴇ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ</b>\n\n"

        "<b>✨ ᴡᴇʟᴄᴏᴍᴇ!</b>\n"
        "ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏꜱ\n"
        "ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ʏᴏᴜᴛᴜʙᴇ.\n\n"

        "<b>📌 ᴄᴏᴍᴍᴀɴᴅꜱ</b>\n"
        "• /login\n"
        "• /help\n"
        "• /upload\n\n"

        "<b>🚀 ᴇɴᴊᴏʏ ᴜᴘʟᴏᴀᴅɪɴɢ!</b>"
        "</blockquote>"
    )

    HELP_MSG = [
        ".",
        "Welcome! This bot uploads Telegram videos to YouTube.",
        "<b>Step 1</b>\nLogin.\n\n<b>Step 2</b>\nReply to a video.\n\n<b>Step 3</b>\nUse <code>/upload</code>.",
        "<b>Create a YouTube Channel</b>",
        "<b>Verify your YouTube Account</b>",
        "<b>Authenticate</b>\n\nUse <code>/authorise YOUR_CODE</code>"
    ]

    NOT_A_REPLY_MSG = "Please reply to a video."
    NOT_A_MEDIA_MSG = "No media found."
    NOT_A_VALID_MEDIA_MSG = "Invalid media."
    DAILY_QOUTA_REACHED = "Daily upload limit reached."
    PROCESSING = "⏳ <b>Processing...</b>"
    NOT_AUTHENTICATED_MSG = "<b>❌ Please use /login first.</b>"
    NO_AUTH_CODE_MSG = "Authentication code required."
    AUTH_SUCCESS_MSG = "<b>✅ Authentication Successful!</b>"
    AUTH_FAILED_MSG = "<b>❌ Authentication Failed</b>\n{}"
    AUTH_DATA_SAVE_SUCCESS = "<b>✅ Authentication Data Saved.</b>"
