class Messages:

    IMAGE_LIST = [
        "https://files.catbox.moe/vg3vae.jpg"
    ]

    START_MSG = (
        "<b>Hi there {} 🇮🇳.</b>\n\n"
        "<b>I'm YouTube Uploader Bot. Made with ❤️ by @SumitTripathi.</b>\n\n"
        "You can use me to upload any Telegram video to YouTube once you authorise me.\n\n"
        "<b>You can know more from</b> /help.\n"
        "<b>Or use</b> /login <b>to get started.</b>"
    )

    HELP_MSG = [
        ".",

        "Hi there.\n\n"
        "First things first. You should be aware that YouTube processes every uploaded video. "
        "Copyrighted videos may be blocked or removed.",

        "<b>Let's learn how I work.</b>\n\n"
        "<b>Step 1:</b> Authorise me using Google.\n"
        "<b>Step 2:</b> Forward any Telegram video.\n"
        "<b>Step 3:</b> Reply <code>/upload</code> to the video.\n"
        "<b>Step 4:</b> I upload it to YouTube.\n"
        "<b>Step 5:</b> I send you the YouTube link.",

        "<b>Create a YouTube Channel</b>\n\n"
        "If you don't have a channel, create one before using me.",

        "<b>Verify your YouTube Account</b>\n\n"
        "Verification allows uploading videos longer than 15 minutes.",

        "<b>Now let's Authorise.</b>\n\n"
        "Click the Authentication URL button.\n"
        "Allow access and copy the code.\n\n"
        "Then send:\n"
        "<code>/authorise YOUR_CODE</code>"
    ]

    NOT_A_REPLY_MSG = "Please reply to a video."

    NOT_A_MEDIA_MSG = "No media found. Please reply to a video."

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media."

    DAILY_QOUTA_REACHED = (
        "Looks like you've reached YouTube's daily upload limit."
    )

    PROCESSING = "⏳ Processing..."

    NOT_AUTHENTICATED_MSG = (
        "❌ You are not authenticated.\nUse /login or /help."
    )

    NO_AUTH_CODE_MSG = "Please provide the authentication code."

    AUTH_SUCCESS_MSG = (
        "✅ Successfully authenticated!\n\nHappy Uploading 🎉"
    )

    AUTH_FAILED_MSG = "❌ Authentication Failed.\n\nDetails:\n{}"

    AUTH_DATA_SAVE_SUCCESS = (
        "✅ Authentication data saved successfully."
    )
