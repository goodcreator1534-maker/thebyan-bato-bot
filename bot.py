import discord
import random
import os
import asyncio
from discord.ext import commands
from discord import app_commands
from flask import Flask
from threading import Thread

# ===== Renderでスリープしないよう対策 =====
app = Flask('')

@app.route('/')
def home():
    return "ザ𰻞ばとーbot起動中"

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

AIUEO = ["汚いジャイアン", "ザビャンの生え際は頭頂部", "【悲報】ザビャン、地球に住んでいる", "#ヒカマーズルネサンス", "🤓←ザビャン", "迷路みたいで話が見えないよザビャンきゅん", "ザビャカスファン共、口論したいなら知識をつけてこい🤪", "反ザビャン万歳🙌", "おい、ザビャン！お前の脳みそ、カプチーノにされちゃったの？🥺", "aiが可哀想", "薄い本(hikakin_mania)", "ボカロP(笑)", "インフルエンサー(笑)", "電力と水がかわいそう", "イタリアに土下座しろ", "おもんねーよ4ね", "ザビャン・アナル丸"]

# ===== 停止フラグ =====
stop_flag = False

@bot.event
async def on_ready():
    print(f"ログイン: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"スラッシュコマンド {len(synced)}個 同期完了")
    except Exception as e:
        print(f"同期エラー: {e}")

# ===== スラッシュコマンド =====
@bot.tree.command(name="ばとー", description="ランダムにばとーテキストを送信する")
async def bato(interaction: discord.Interaction):
    reply = random.choice(AIUEO)
    await interaction.response.send_message(reply)

@bot.tree.command(name="いけ", description="行ってきます")
@app_commands.describe(回数="何回送るか")
async def ike(interaction: discord.Interaction, 回数: int = 1):
    global stop_flag
    
    回数 = max(1, 回数)
    stop_flag = False
    
    await interaction.response.defer()
    
    for i in range(回数):
        if stop_flag:
            await interaction.followup.send("止めたで")
            stop_flag = False
            return
            
        reply = random.choice(AIUEO)
        await interaction.followup.send(reply)
        if i < 回数 - 1:
            await asyncio.sleep(0.01)
    
    stop_flag = False

@bot.tree.command(name="すとっぷ", description="/いけを止める")
async def stop(interaction: discord.Interaction):
    global stop_flag
    stop_flag = True
    await interaction.response.send_message("止めるで")

# ===== メンション反応（従来通り）=====
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
