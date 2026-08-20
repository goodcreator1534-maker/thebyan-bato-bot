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
        await channel.send("あ")
        if i < 回数 - 1:
            await asyncio.sleep(1.0)
    
    stop_flag = False
    await interaction.followup.send("おわり")
