from pyrogram import Client, filters
import os

bot_token = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

app = Client("my_bot", bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Salam! Bot işə düşdü.")

app.run()
