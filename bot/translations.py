class Messages:

    IMAGE_LIST = [
        "https://files.catbox.moe/vg3vae.jpg"
    ]

    START_MSG = (
        "<blockquote>"
        "👋 <b>ʜɪ ᴛʜᴇʀᴇ {}!</b>\n\n"

        "🎬 <b>ʏᴏᴜᴛᴜʙᴇ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ</b>\n\n"

        "✨ <b>ᴡᴇʟᴄᴏᴍᴇ!</b>\n"
        "<b>ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏꜱ</b>\n"
        "<b>ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ʏᴏᴜᴛᴜʙᴇ.</b>\n\n"

        "📌 <b>ᴄᴏᴍᴍᴀɴᴅꜱ</b>\n\n"

        "• <b>/login</b> ━ <b>ʟᴏɢɪɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ ᴀᴄᴄᴏᴜɴᴛ</b>\n"
        "• <b>/help</b> ━ <b>ʜᴇʟᴘ & ᴜꜱᴇʀ ɢᴜɪᴅᴇ</b>\n"
        "• <b>/upload</b> ━ <b>ᴜᴘʟᴏᴀᴅ ᴀ ʀᴇᴘʟɪᴇᴅ ᴠɪᴅᴇᴏ</b>\n"
        "• <b>/cancel</b> ━ <b>ᴄᴀɴᴄᴇʟ ᴄᴜʀʀᴇɴᴛ ᴜᴘʟᴏᴀᴅ</b>\n\n"

        "❤️ <b>ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @SumitTripathi</b>"
        "</blockquote>"
    )

    HELP_MSG = [
        ".",

        "<b>📖 ʜᴇʟᴘ ɢᴜɪᴅᴇ</b>\n\n"
        "ᴛʜɪꜱ ʙᴏᴛ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ʏᴏᴜᴛᴜʙᴇ.",

        "<b>📌 ꜱᴛᴇᴘ 1</b>\n"
        "• /login\n\n"
        "<b>📌 ꜱᴛᴇᴘ 2</b>\n"
        "Reply to your video.\n\n"
        "<b>📌 ꜱᴛᴇᴘ 3</b>\n"
        "Use <code>/upload</code>.",

        "<b>🎬 ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ</b>",

        "<b>✅ ᴠᴇʀɪꜰʏ ʏᴏᴜʀ ʏᴏᴜᴛᴜʙᴇ ᴀᴄᴄᴏᴜɴᴛ</b>",

        "<b>🔑 ʟᴏɢɪɴ</b>\n\n"
        "Use:\n"
        "<code>/authorise YOUR_CODE</code>"
    ]

    NOT_A_REPLY_MSG = "⚠️ Reply to a video."

    NOT_A_MEDIA_MSG = "⚠️ No media found."

    NOT_A_VALID_MEDIA_MSG = "❌ Invalid video."

    DAILY_QOUTA_REACHED = "⚠️ Daily upload limit reached."

    PROCESSING = "⏳ <b>ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b>"

    NOT_AUTHENTICATED_MSG = (
        "🔒 <b>You are not logged in.</b>\n\n"
        "Use <code>/login</code> first."
    )

    NO_AUTH_CODE_MSG = "❌ Authentication code missing."

    AUTH_SUCCESS_MSG = (
        "✅ <b>Authentication Successful!</b>\n\n"
        "Now you can upload videos."
    )

    AUTH_FAILED_MSG = (
        "❌ <b>Authentication Failed!</b>\n\n{}"
    )

    AUTH_DATA_SAVE_SUCCESS = (
        "✅ <b>Authentication data saved successfully.</b>"
    )
