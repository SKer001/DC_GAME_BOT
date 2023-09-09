import discord
from discord.ext import commands
import json
import os
import datetime
import asyncio
from core.Def import reback

intents = discord.Intents.default()  
intents.message_content = True
intents.messages = True

with open('guild_info.json',mode='r',encoding="utf-8") as file:
    guild_info = json.load(file)

with open("config.json",mode='r',encoding="utf-8") as file:
    config = json.load(file)

bot = commands.Bot(command_prefix='^',intents=intents)

################################################################
@bot.event
async def on_ready():
    config["online_times"] = config["online_times"] + 1
    times = config["online_times"]
    Channel = bot.get_guild(832219486153080883).get_channel(config["retrack_channel_id"])
    await Channel.send("第"+ str(times) +"次上線ING")
    print("Online")
    with open("config.json",mode='w',encoding="utf-8") as file:
        json.dump(config,file,indent=4)
################################################################

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
    reback(ctx.author.name,ctx.message.author.id,ping)
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
    embed.set_footer(text="the best cat bot")
    await ctx.send(embed=embed)
    reback(ctx.author.name,ctx.message.author.id,info)

################################################################
@bot.command()
async def load(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.load_extension(f"cmds.{extension}")
        await ctx.send(f"Loaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,load)
    else:
        await ctx.send(f"你沒資格")
@bot.command()
async def unload(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.unload_extension(f"cmds.{extension}")
        await ctx.send(f"Unloaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,unload)
    else:
        await ctx.send(f"你沒資格")
@bot.command()
async def reload(ctx,extension):
    if  ctx.message.author.id == 403895664666214400:
        await bot.reload_extension(f"cmds.{extension}")
        await ctx.send(f"Reloaded {extension} done")
        reback(ctx.author.name,ctx.message.author.id,reload)
    else:
        await ctx.send(f"你沒資格")
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
