import discord
import random
import os
from discord.ext import commands
from flask import Flask
from threading import Thread

# ===== Renderでスリープしないよう対策 =====
app = Flask('')

@app.route('/')
def home():
    return "あいうえおボット起動中"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ===== Discord Bot =====
TOKEN = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

AIUEO = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ"]

@bot.event
async def on_ready():
    print(f"ログイン: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user not in message.mentions:
        return

    reply = random.choice(AIUEO)
    await message.channel.send(reply)

keep_alive()
bot.run(TOKEN)
