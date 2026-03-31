import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SESSION_STRING = os.environ.get("SESSION_STRING")

userbot = Client("userbot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
tgcalls = PyTgCalls(userbot)

@bot.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply("✅ Salam!")

@bot.on_message(filters.command("stream"))
async def stream_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("İstifadə: /stream <url>")
        return
    url = message.command[1]
    await message.reply("⏳ Başlayır...")
    try:
        await tgcalls.play(message.chat.id, MediaStream(url))
        await message.reply("▶️ Stream başladı!")
    except Exception as e:
        await message.reply(f"❌ Xəta: {e}")

@bot.on_message(filters.command("stop"))
async def stop_cmd(client: Client, message: Message):
    try:
        await tgcalls.leave_call(message.chat.id)
        await message.reply("⏹ Dayandı.")
    except Exception as e:
        await message.reply(f"❌ Xəta: {e}")

async def main():
    await userbot.start()
    await bot.start()
    await tgcalls.start()
    print("✅ Bot işləyir...")
    await asyncio.Event().wait()

asyncio.run(main())
