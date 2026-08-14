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

# ===== ここにサーバーIDを入れる =====
# Discordでサーバー名を長押し→「サーバーIDをコピー」→下の数字と置き換え
GUILD_ID = 1527486638509391904

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

AIUEO = ["汚いジャイアン", "ザビャンの生え際は頭頂部", "【悲報】ザビャン、地球に住んでいる", "#ヒカマーズルネサンス", "🤓←ザビャン", "迷路みたいで話が見えないよザビャンきゅん", "ザビャカスファン共、口論したいなら知識をつけてこい🤪", "反ザビャン万歳🙌", "おい、ザビャン！お前の脳みそ、カプチーノにされちゃったの？🥺", "aiが可哀想", "薄い本(hikakin_mania)", "ボカロP(笑)", "インフルエンサー(笑)", "電力と水がかわいそう", "イタリアに土下座しろ", "おもんねーよ4ね", "ザビャン・アナル丸"]

stop_flag = False

@bot.event
async def on_ready():
    print(f"ログイン: {bot.user}")
    try:
        guild = discord.Object(id=GUILD_ID)
        # 既存コマンドをクリアして再登録（反映を確実にする）
        bot.tree.clear_commands(guild=guild)
        await bot.tree.sync(guild=guild)
        synced = await bot.tree.sync(guild=guild)
        print(f"スラッシュコマンド {len(synced)}個 同期完了")
    except Exception as e:
        print(f"同期エラー: {e}")

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
    
    try:
        for i in range(回数):
            if stop_flag:
                await interaction.followup.send("止めたで")
                stop_flag = False
                return
            reply = random.choice(AIUEO)
            await interaction.followup.send(reply)
            if i < 回数 - 1:
                await asyncio.sleep(1.0)
    except Exception as e:
        await interaction.followup.send(f"エラー: {e}")
    stop_flag = False

@bot.tree.command(name="さえんす", description="なんだ亀頭か")
@app_commands.describe(回数="何回送るか")
async def saensu(interaction: discord.Interaction, 回数: int = 1):
    global stop_flag
    回数 = max(1, 回数)
    stop_flag = False
    
    await interaction.response.defer()
    
    try:
        for i in range(回数):
            if stop_flag:
                await interaction.followup.send("止めたで")
                stop_flag = False
                return
            await interaction.followup.send("設x設x設x設x 愛液愛液愛液愛液　えっちえっちえっちえっち　抜ける👍抜ける👍抜ける👍抜ける👍　射精射精射精射精　ごしごしごしごし　膣膣膣膣　お尻お尻お尻お尻　変態変態変態変態　満己満己満己満己　TN己TN己TN己TN己　クンニクンニクンニクンニ　オナニーオナニーオナニーオナニー　アナ、ゥアナ、ゥアナ、ゥアナ、ゥ　金玉金玉金玉金玉　イラマチオ イラマチオ イラマチオ イラマチオ　スカトロ スカトロ スカトロ スカトロ　マスカキ マスカキ マスカキ マスカキ　中出し中出し中出し中出し　淫乱淫乱淫乱淫乱　クリトリス クリトリス クリトリス　潮吹き 潮吹き 潮吹き 潮吹き　ロリコン ロリコン ロリコン ロリコン　手コキ手コキ手コキ手コキ　満己満己満己満己　イクイクイクイク　エロエロエロエロ　マラマラマラマラ　TENGA TENGA TENGA TENGA TN TN TN TN カキカキカキカキ　アナニーアナニーアナニーアナニー　卑猥卑猥卑猥卑猥　強姦強姦強姦強姦　青姦青姦青姦青姦　痴漢痴漢痴漢痴漢　和姦和姦和姦和姦　近親相姦 近親相姦 近親相姦　ふたなり ふたなり ふたなり ふたなり　下ネタ下ネタ下ネタ下ネタ　陰毛陰毛陰毛陰毛　孕ませ孕ませ孕ませ孕ませ　亀頭亀頭亀頭　股股股股　早漏早漏早漏")
            if i < 回数 - 1:
                await asyncio.sleep(1.0)
    except Exception as e:
        await interaction.followup.send(f"エラー: {e}")
    stop_flag = False

@bot.tree.command(name="すとっぷ", description="/いけを止める")
async def stop(interaction: discord.Interaction):
    global stop_flag
    stop_flag = True
    await interaction.response.send_message("止めるで")

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
