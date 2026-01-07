from pyrogram import Client, filters
import os

bot_token = os.environ.get("BOT_TOKEN", "8265190067:AAE0H1PTXJmUVXKKpW2S0iQJC6_IThpKw6Q")

app = Client("my_bot", bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Salam! Bot işə düşdü.")

app.run()
