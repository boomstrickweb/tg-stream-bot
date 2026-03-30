import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

userbot = Client("userbot", api_id=API_ID, api_hash=API_HASH)
bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
tgcalls = PyTgCalls(userbot)

@bot.on_message(filters.command("stream") & filters.group)
async def stream_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("İstifadə: `/stream <video_url>`")
        return
    url = message.command[1]
    await message.reply("⏳ Stream başlayır...")
    try:
        await tgcalls.play(message.chat.id, MediaStream(url))
        await message.reply(f"▶️ Stream başladı:\n`{url}`")
    except Exception as e:
        await message.reply(f"❌ Xəta: {e}")

@bot.on_message(filters.command("stop") & filters.group)
async def stop_cmd(client: Client, message: Message):
    try:
        await tgcalls.leave_call(message.chat.id)
        await message.reply("⏹ Stream dayandırıldı.")
    except Exception as e:
        await message.reply(f"❌ Xəta: {e}")

async def main():
    await userbot.start()
    await bot.start()
    await tgcalls.start()
    print("✅ Bot işləyir...")
    await asyncio.gather(userbot.idle(), bot.idle())

asyncio.run(main())
```

**`Procfile`** (Railway üçün):
```
worker: python bot.py
