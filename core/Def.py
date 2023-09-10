import discord
from discord.ext import commands
import json
import os
import asyncio
import datetime

intents = discord.Intents.default()
intents.members = True  
intents.message_content = True
intents.messages = True
intents.guilds = True


bot_def = commands.Bot(command_prefix='^',intents=intents)

path = "log/" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt"
with open(path,"w",encoding="utf-8") as f:
    pass
def reback(user_name,user_id,command):
    print(f"{datetime.datetime.utcnow()} used {command} by {user_name} {user_id}")
    with open(path, "a",encoding="utf-8") as LogFile:
        LogFile.write(f"{datetime.datetime.now()} used {command} by {user_name} {user_id}\n")

class custom_bot_command():
    def get_user_from_id(id):
        return bot_def.get_user(id)
    def get_channel_from_id(id):
        return bot_def.get_channel(id)
        