import discord
from discord.ext import commands
from discord import app_commands
from discord import interactions
from core.classes import Cog_Extension
from core.Def import *
import datetime,os,random,json,langid

CBC = custom_bot_command

DChoice = discord.app_commands.Choice

DInteracion = discord.Interaction

reback = CBC.reback

def load_english():
    with open("English.json", "r", encoding="utf-8") as Efile:
        return dict(json.load(Efile))
  
def upload_english(file):
    with open("English.json", "w", encoding="utf-8") as Efile:
        json.dump(file, Efile,indent=4,ensure_ascii=False)

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
                all_guilds = [i for i in (english_words["user"]).keys()]
                for guild in all_guilds:
                    if (english_words["user"][guild]["question_sent"] == False) and (english_words["user"][guild]["enable"] == True):
                        await self.bot.get_channel(english_words["user"][guild]["set_channel"]).send(f"not done")
                        english_words["user"][guild]["question_sent"] = True
                upload_english(english_words)
        self.bg_task = self.bot.loop.create_task(test())
##################################################################
    @app_commands.command(name="add-english-word",description="Add English words to list which will be the question")
    @app_commands.describe(word="English word")
    @app_commands.describe(meaning="The mean of word")
    @app_commands.describe(part_of_speech="part of speech")
    @app_commands.choices(part_of_speech=load_part_of_speech())
    async def add_english_word(self,interaction:DInteracion,word:str,meaning:str,part_of_speech:DChoice[int]):
        english_words = load_english()
        if langid.classify(word)[0] == "en":
            if langid.classify(meaning)[0] == "zh":
                english_words[part_of_speech.name][word] = meaning
                upload_english(english_words)
                await interaction.response.send_message(f"已添加>>>{word}<<<到英文單字庫了喵")
                reback(interaction.user.name,interaction.user.id,"Slash add English words")
            elif langid.classify(meaning)[0] != "zh":
                await interaction.response.send_message(f"{interaction.user.mention} >>>{meaning}<<<好像不是中文欸喵ᓚᘏᗢ")
        elif langid.classify(word)[0] != "en":
            await interaction.response.send_message(f"{interaction.user.mention} >>>{word}<<<好像不是英文欸喵ᓚᘏᗢ")
##################################################################
    @app_commands.command(name="set-english-channel",description="Set test channel")
    @app_commands.describe(channel="The channel you want to set")
    @app_commands.describe(open="Do you want to take the exam?")
    @app_commands.choices(open=[DChoice(name="Yes",value=True), DChoice(name="No",value=False)])
    async def setchannel(self,interaction:DInteracion,channel:discord.TextChannel=None,open:DChoice[int]=True):
        english_words = load_english()
        if channel != None:
            english_words["user"][str(channel.guild.id)] = {
                "guild_name":channel.guild.name,
                "set_channel":channel.id,
                "enable":open.value,
                "question_sent":False
            }
            await interaction.response.send_message(f"已經設{channel.mention}為英文單字考試的頻道了喵!!!")
        else:
            english_words["user"][str(interaction.guild.id)] = {
                "guild_name":interaction.guild.name,
                "set_channel":interaction.channel_id,
                "enable":open.value,
                "question_sent":False
            }
            await interaction.response.send_message(f"已經設{interaction.channel.mention}為英文單字考試的頻道了喵!!!")
        upload_english(english_words)
        reback(interaction.user.name,interaction.user.id,"Slash set English channel")
##################################################################
async def setup(bot):
    await bot.add_cog(english(bot))