super().__init__(
    name=Config.SESSION_NAME,   # 👈 session_name hata, name likh
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=dict(root="bot.plugins"),
    workers=6,
)
