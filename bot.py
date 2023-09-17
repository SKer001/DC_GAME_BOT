import discord
from discord.ext import commands
from discord import app_commands
import json
import os
import datetime
import asyncio
from core.Def import custom_bot_command as CBC

intents = discord.Intents.default()
intents.members = True  
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='^',intents=intents)

DChoice = discord.app_commands.Choice

reback = CBC.reback

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
################################################################
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
    reback(ctx.author.name,ctx.message.author.id,ping)
################################################################
@bot.command()
async def info(ctx,choices):
    if choices == "bot":
        cat_embed=discord.Embed(
        title="關於Mew機器人", 
        description="uwu!!", 
        color=0xffc21a, 
        timestamp = datetime.datetime.now()
        )
        cat_embed.set_author(
        name="Yurei",
        url="https://discord.gg/t7SXq4E5pF",
        icon_url="https://cdn.discordapp.com/attachments/693782101463400498/1147878445406228610/icon.png"
        )
        cat_embed.add_field(
            name="邀請連結", 
            value="https://discord.com/api/oauth2/authorize?client_id=1147725051421016276&permissions=8&scope=bot", 
            inline=False)
        cat_embed.set_footer(text="the best cat bot")
        await ctx.send(embed=cat_embed)
        reback(ctx.author.name,ctx.message.author.id,"info_bot")
    elif choices == "owner":
        ctx.send(f"我還沒做這個XD")
        reback(ctx.author.name,ctx.message.author.id,"info_owner")
################################################################
@bot.command()
async def load(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.load_extension(f"cmds.{extension}")
        await ctx.send(f"Loaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,load)
    else:
        await ctx.send(f"你沒資格")
################################################################
@bot.command()
async def unload(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.unload_extension(f"cmds.{extension}")
        await ctx.send(f"Unloaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,unload)
    else:
        await ctx.send(f"你沒資格")
################################################################
@bot.command()
async def reload(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.reload_extension(f"cmds.{extension}")
        await ctx.send(f"Reloaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,reload)
    else:
        await ctx.send(f"你沒資格")
##################################################################
@bot.command()
async def reloadall(ctx):
    if ctx.author.id == 403895664666214400:
        for filename in os.listdir("cmds"):
            if filename.endswith(".py"):
                await bot.reload_extension(f"cmds.{filename[:-3]}")
        await ctx.send(f"Has reloaded all extensions",ephemeral=True)
        reback(ctx.author.name,ctx.author.id,"slash_reloadall")
    else:
        await ctx.send("你沒資格")
##################################################################
async def Allload():
    for filename in os.listdir("cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    reback("the bot","000000000000000001",">>>Allload<<<")

loop = asyncio.get_event_loop()
loop.run_until_complete(Allload())
if __name__ == "__main__":
    bot.run(config["token"])
