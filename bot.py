import discord
from discord.ext import commands
from discord import app_commands
import json
import os
import datetime
import asyncio
from core.Def import reback
from core.Def import custom_bot_command

intents = discord.Intents.default()
intents.members = True  
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='^',intents=intents)

with open('guild_info.json',mode='r',encoding="utf-8") as file:
    guild_info = json.load(file)

with open("config.json",mode='r',encoding="utf-8") as file:
    config = json.load(file)

################################################################
@bot.event
async def on_ready():
    config["online_times"] = config["online_times"] + 1
    times = config["online_times"]
    Channel = bot.get_guild(832219486153080883).get_channel(config["retrack_channel_id"])
    await Channel.send("第"+ str(times) +"次上線ING")
    try:
        sycned = await bot.tree.sync()
        print (f"Synced {len(sycned)} commands")
    except Exception as e:
        print (e)
    print("Online")
    with open("config.json",mode='w',encoding="utf-8") as file:
        json.dump(config,file,indent=4)
################################################################
@bot.command()
async def dellog(ctx):
    if ctx.author.id == 403895664666214400:
        for filename in os.listdir("log"):
            if filename[8:-13] != datetime.datetime.now().strftime("%d"):
                os.remove(f"log/{filename}")
        reback(ctx.author.name,ctx.author.id,dellog)
        await ctx.send(f"已刪除舊紀錄了喵!!")
    else :
        await ctx.send(f"你沒資格")
@bot.tree.command(name="dellog",description="To delete the log files(only the bot owner can use)")
async def dellog(interaction:discord.Interaction):
    if interaction.user.id == 403895664666214400:
        for filename in os.listdir("log"):
            if filename[8:-13] != datetime.datetime.now().strftime("%d"):
                os.remove(f"log/{filename}")
        reback(interaction.user.name,interaction.user.id,"slash_dellog")
        await interaction.response.send_message(f"已刪除舊紀錄了喵!!")
    else:
        await interaction.response.send_message(f"你沒資格",ephemeral=True)
################################################################
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
    reback(ctx.author.name,ctx.message.author.id,ping)
@bot.tree.command(name="ping", description="Ping the server")
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")
    reback(interaction.user.name,interaction.user.id,"slash_ping")
################################################################
@bot.tree.command(name="hello",description="this is for test slash command")
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message(f"hello! {interaction.user.mention} !!",ephemeral=True)
    reback(interaction.user.name,interaction.user.id,"slash_hello")
################################################################
@bot.command()
async def info(ctx):
    embed=discord.Embed(
    title="關於Mew機器人", 
    description="uwu!!", 
    color=0xffc21a, 
    timestamp = datetime.datetime.now()
    )
    embed.set_author(
    name="Yurei",
    url="https://discord.gg/t7SXq4E5pF",
    icon_url="https://cdn.discordapp.com/attachments/693782101463400498/1147878445406228610/icon.png"
    )
    embed.add_field(
        name="邀請連結", 
        value="https://discord.com/api/oauth2/authorize?client_id=1147725051421016276&permissions=8&scope=bot", 
        inline=False)
    embed.set_footer(text="the best cat bot")
    await ctx.send(embed=embed)
    reback(ctx.author.name,ctx.message.author.id,info)
@bot.tree.command(name="info",description="chack the bot's information")
async def info(interaction:discord.Interaction):
    embed=discord.Embed(
    title="關於Mew機器人", 
    description="uwu!!", 
    color=0xffc21a, 
    timestamp = datetime.datetime.now()
    )
    embed.set_author(
    name="Yurei",
    url="https://discord.gg/t7SXq4E5pF",
    icon_url="https://cdn.discordapp.com/attachments/693782101463400498/1147878445406228610/icon.png"
    )
    embed.add_field(
        name="邀請連結", 
        value="https://discord.com/api/oauth2/authorize?client_id=1147725051421016276&permissions=8&scope=bot", 
        inline=False)
    embed.set_footer(text="the best cat bot")
    await interaction.response.send_message(embed=embed)
    reback(interaction.user.name,interaction.user.id,"slash_info")
################################################################
@bot.command()
async def load(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.load_extension(f"cmds.{extension}")
        await ctx.send(f"Loaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,load)
    else:
        await ctx.send(f"你沒資格")
@bot.tree.command(name="load",description="for load Cog(only the bot owner can use)")
async def load(interaction,extension:str):
    if  interaction.user.id == 403895664666214400:
        await bot.load_extension(f"cmds.{extension}")
        await interaction.response.send_message(f"Loaded {extension} done",ephemeral=True)
        reback(interaction.user.name,interaction.user.id,"slash_load")
    else:
        await interaction.response.send_message(f"你沒資格",ephemeral=True)
################################################################
@bot.command()
async def unload(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.unload_extension(f"cmds.{extension}")
        await ctx.send(f"Unloaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,unload)
    else:
        await ctx.send(f"你沒資格")
@bot.tree.command(name="unload",description="for unload Cog(only the bot owner can use)")
async def unload(interaction,extension:str):
    if  interaction.user.id == 403895664666214400:
        await bot.unload_extension(f"cmds.{extension}")
        await interaction.response.send_message(f"Unloaded {extension} done",ephemeral=True)
        reback(interaction.user.name,interaction.user.id,"slash_unload")
    else:
        await interaction.response.send_message(f"你沒資格",ephemeral=True)
################################################################
@bot.command()
async def reload(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.reload_extension(f"cmds.{extension}")
        await ctx.send(f"Reloaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,reload)
    else:
        await ctx.send(f"你沒資格")
@bot.tree.command(name="reload",description="for reload Cog(only the bot owner can use)")
async def reload(interaction,extension:str):
    if  interaction.user.id == 403895664666214400:
        await bot.reload_extension(f"cmds.{extension}")
        await interaction.response.send_message(f"Reloaded {extension} done",ephemeral=True)
        reback(interaction.user.name,interaction.user.id,"slash_reload")
    else:
        await interaction.response.send_message(f"你沒資格",ephemeral=True)
################################################################

async def Allload():
    for filename in os.listdir("cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")

    reback("the bot","000000000000000001",">>>Allload<<<")

loop = asyncio.get_event_loop()
loop.run_until_complete(Allload())


if __name__ == "__main__":
    bot.run(config["token"])
