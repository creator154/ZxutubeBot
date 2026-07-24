class Messages:

    IMAGE_LIST = [
        "https://files.catbox.moe/vg3vae.jpg"
    ]

    START_MSG = (
        "🌸 Hi there {}.\n\n"
        "🤖 Welcome to YouTube Uploader Bot!\n\n"
        "🎥 I can upload your Telegram videos directly to your YouTube channel.\n\n"
        "📖 Use /help to learn how to use me.\n"
        "🔐 Use /login to authorize your YouTube account.\n\n"
        "❤️ Thank you for using this bot."
    )

    HELP_MSG = [
        ".",
        "Hi there.\n\nFirst things first. You should be aware that YouTube processes every uploaded video and may flag copyrighted content.",
        "Step 1: Authorize the bot.\nStep 2: Forward a Telegram video.\nStep 3: Reply /upload to the video.\nStep 4: Bot uploads it.\nStep 5: Bot sends the YouTube link.",
        "Create a YouTube channel if you don't have one.",
        "Verify your YouTube account to upload videos longer than 15 minutes.",
        "Authorize the bot by opening the authorization link and sending the code using /authorise."
    ]

    NOT_A_REPLY_MSG = "Please reply to a video."

    NOT_A_MEDIA_MSG = "No media found. Please reply to a video."

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media."

    DAILY_QOUTA_REACHED = (
        "You may have reached YouTube's daily upload limit."
    )

    PROCESSING = "Processing..."

    NOT_AUTHENTICATED_MSG = (
        "You are not authenticated. Use /login or see /help."
    )

    NO_AUTH_CODE_MSG = "Please provide the authorization code."

    AUTH_SUCCESS_MSG = (
        "✅ Authentication successful.\nHappy Uploading!"
    )

    AUTH_FAILED_MSG = "❌ Authentication failed.\nDetails: {}"

    AUTH_DATA_SAVE_SUCCESS = "✅ Authentication data saved successfully."
