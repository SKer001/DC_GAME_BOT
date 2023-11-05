import discord
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import random
import json
from core.Def import custom_bot_command as CBC

with open("./For_Eat.json","r", encoding="utf-8") as Jfile:
    data = list(json.load(Jfile))

reback = CBC.reback

class food(Cog_Extension):
    @commands.command()
    async def EatFood(self,ctx):
        food = random.choice(data["data"])
        await ctx.send(f"{ctx.author.mention} 吃>{food}<吧喵!!")
        reback(ctx.author.name,ctx.author.id,"EatFood")
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
################################################################
    @commands.command()
    async def FoodList(self,ctx):
        list = data["data"]
        reback(ctx.author.name,ctx.author.id,"EatList")
        await ctx.send(f"有\n{list}\n可以吃")    
################################################################
async def setup(bot):
    await bot.add_cog(food(bot))