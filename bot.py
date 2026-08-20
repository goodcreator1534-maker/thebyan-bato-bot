@bot.tree.command(name="いけ", description="行ってきます")
@app_commands.describe(回数="何回送るか")
async def ike(interaction: discord.Interaction, 回数: int = 1):
    global stop_flag
    回数 = max(1, min(回数, 50))
    stop_flag = False
    
    await interaction.response.defer()
    
    channel = interaction.channel
    if channel is None:
        await interaction.followup.send("チャンネルが取得できないため実行できません")
        return
    
    for i in range(回数):
        if stop_flag:
            await channel.send("止めたで")
            stop_flag = False
            return
        reply = random.choice(AIUEO)
        await channel.send(reply)
        if i < 回数 - 1:
            await asyncio.sleep(1.0)
    
    stop_flag = False
    await interaction.followup.send("おわり")

@bot.tree.command(name="さえんす", description="なんだ亀頭か")
@app_commands.describe(回数="何回送るか")
async def saensu(interaction: discord.Interaction, 回数: int = 1):
    global stop_flag
    回数 = max(1, min(回数, 50))
    stop_flag = False
    
    await interaction.response.defer()
    
    channel = interaction.channel
    if channel is None:
        await interaction.followup.send("チャンネルが取得できないため実行できません")
        return
    
    for i in range(回数):
        if stop_flag:
            await channel.send("止めたで")
            stop_flag = False
            return
        await channel.send ("設x設x設x設x 愛液愛液愛液愛液　えっちえっちえっちえっち　抜ける👍抜ける👍抜ける👍抜ける👍　射精射精射精射精　ごしごしごしごし　膣膣膣膣　お尻お尻お尻お尻　変態変態変態変態　満己満己満己満己　TN己TN己TN己TN己　クンニクンニクンニクンニ　オナニーオナニーオナニーオナニー　アナ、ゥアナ、ゥアナ、ゥアナ、ゥ　金玉金玉金玉金玉　イラマチオ イラマチオ イラマチオ イラマチオ　スカトロ スカトロ スカトロ スカトロ　マスカキ マスカキ マスカキ マスカキ　中出し中出し中出し中出し　淫乱淫乱淫乱淫乱　クリトリス クリトリス クリトリス　潮吹き 潮吹き 潮吹き 潮吹き　ロリコン ロリコン ロリコン ロリコン　手コキ手コキ手コキ手コキ　満己満己満己満己　イクイクイクイク　エロエロエロエロ　マラマラマラマラ　TENGA TENGA TENGA TENGA TN TN TN TN カキカキカキカキ　アナニーアナニーアナニーアナニー　卑猥卑猥卑猥卑猥　強姦強姦強姦強姦　青姦青姦青姦青姦　痴漢痴漢痴漢痴漢　和姦和姦和姦和姦　近親相姦 近親相姦 近親相姦　ふたなり ふたなり ふたなり ふたなり　下ネタ下ネタ下ネタ下ネタ　陰毛陰毛陰毛陰毛　孕ませ孕ませ孕ませ孕ませ　亀頭亀頭亀頭　股股股股　早漏早漏早漏")
        if i < 回数 - 1:
            await asyncio.sleep(1.0)
    
    stop_flag = False
    await interaction.followup.send("おわり")
