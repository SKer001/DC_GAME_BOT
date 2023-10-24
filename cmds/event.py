import discord
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import random
import json
from core.Def import custom_bot_command as CBC
data = {}
with open("./For_Eat.json","r", encoding="utf-8") as Jfile:
    data = json.load(Jfile)
reback = CBC.reback

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith("eat"): #for food event
            reback(msg.author.name,msg.author.id ,msg.content)
            output = str(random.choice(data["data"]))
            await msg.channel.send(f"吃{output}ᓚᘏᗢ")
################################################################
async def setup(bot):
    await bot.add_cog(event(bot))