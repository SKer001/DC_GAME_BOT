import discord
from discord import interactions
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import datetime
import os
import random
import json
from core.Def import *

CBC = custom_bot_command


DChoice = discord.app_commands.Choice

DInteracion = discord.Interaction

reback = CBC.reback

def load_english():
    with open("English.json", "r", encoding="utf-8") as Efile:
        return dict(json.load(Efile))
  
def upload_english(file):
    with open("English.json", "w", encoding="utf-8") as Efile:
        json.dump(file, Efile,indent=4)

def load_part_of_speech():
    keys = list((dict(load_english())).keys())
    keys.remove("user")
    lis = []
    value = 1
    for i in keys:
        lis.append(DChoice(name=i,value=value))
        value += 1
    return lis
    
class english(Cog_Extension):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
##################################################################
        async def test():
            while not self.bot.is_closed():
                await asyncio.sleep(5)
                english_words = load_english()
                all_channel = english_words["user"].keys()
                for channel in all_channel:
                    if english_words["user"][channel]["question_sent"] == False:
                        await self.bot.get_channel(int(channel)).send(f"not done")
                        english_words["user"][channel]["question_sent"] = True
                upload_english(english_words)
        self.bg_task = self.bot.loop.create_task(test())
##################################################################
    @app_commands.command(name="add-english-word",description="Add English words to list which will be the question")
    @app_commands.describe(word="English word")
    @app_commands.describe(meaning="The mean of word")
    @app_commands.describe(part_of_speech="part of speech")
    @app_commands.choices(part_of_speech=load_part_of_speech())
    async def add_english_word(self,interaction:DInteracion,word:str,meaning:str,part_of_speech:DChoice[int]):
       
       pass



async def setup(bot):
    await bot.add_cog(english(bot))