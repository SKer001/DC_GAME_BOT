import discord
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import random
import json
from core.Def import reback
data = {}
with open("./For_Eat.json","r", encoding="utf-8") as Jfile:
    data = json.load(Jfile)

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith("eat"): #for food event
            reback(msg.author.name,msg.author.id ,msg.content)
            output = str(random.choice(data["data"]))
            await msg.channel.send(f"吃{output}ᓚᘏᗢ")
################################################################  
    @commands.command()
    async def AddEat(self,ctx,food):
        global data
        data["data"].append(food)
        with open("./For_Eat.json","w",encoding="utf-8") as Jfile:
            json.dump(data,Jfile,indent=4,ensure_ascii=False)
        await ctx.send(f"已添加 >>>{food}<<< 到選單中，喵!!!")
        reback(ctx.author.name,ctx.author.id,"AddEat")
        with open("./For_Eat.json","r", encoding="utf-8") as Jfile:
            data = json.load(Jfile)
    @app_commands.command(name="addeat",description="Add food to the list")
    async def addeat(self,ineraction:discord.Interaction,food:str):
        global data
        data["data"].append(food)
        with open("./For_Eat.json","w",encoding="utf-8") as Jfile:
            json.dump(data,Jfile,indent=4,ensure_ascii=False)
        await ineraction.response.send_message(f"已添加 >>>{food}<<< 到選單中，喵!!!")
        reback(ineraction.user.name,ineraction.user.id,"slash_AddEat")
        with open("./For_Eat.json","r", encoding="utf-8") as Jfile:
            data = json.load(Jfile)
################################################################
    @commands.command()
    async def EatList(self,ctx):
        list = data["data"]
        reback(ctx.author.name,ctx.author.id,"EatList")
        await ctx.send(f"有\n{list}\n可以吃")
    @app_commands.command(name="eatlist",description="Check the food list")
    async def eatlist(self,ineraction:discord.Interaction):
        list = data["data"]
        await ineraction.response.send_message(f"有\n{list}\n可以吃")
        reback(ineraction.user.name,ineraction.user.id,"slash_EatList")
################################################################
async def setup(bot):
    await bot.add_cog(event(bot))