import discord
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import datetime
import os
import random
import json
from core.Def import reback

DChoice = discord.app_commands.Choice

DInteracion = discord.Interaction

with open('guild_info.json',mode='r',encoding="utf-8") as file:
    guild_info = json.load(file)

with open("./For_Eat.json","r", encoding="utf-8") as Jfile:
    food_data = json.load(Jfile)

class slashcommand(Cog_Extension):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
##################################################################
    @app_commands.command(name="slash", description="for test")
    @app_commands.describe(choices="what do yuo want to see?")
    @app_commands.choices(choices=[
        discord.app_commands.Choice(name="yor name",value=1)
    ])
    async def slash(self,interaction:DInteracion,choices:discord.app_commands.Choice[int]):
        if choices.value == 1:
            await interaction.response.send_message(f"your name is {interaction.user.name}",ephemeral=True)
        reback(interaction.user.name,interaction.user.id,"slash_slash")    
##################################################################
    @app_commands.command(name="reload",description="Reload Cog")
    @app_commands.describe(extensions="Choices one to reload it")
    @app_commands.choices(extensions=[
        DChoice(name=f"CardBettleSys",value=1),
        DChoice(name=f"event",value=2),
        DChoice(name=f"guild",value=3),
        DChoice(name=f"rpg",value=4),
        DChoice(name=f"slashcommand",value=5)
    ])
    async def reload(self,interaction:DInteracion,extensions:DChoice[int]):
        if  interaction.user.id == 403895664666214400:
            await self.bot.reload_extension(f"cmds.{extensions.name}")
            await interaction.response.send_message(f"Reloaded {extensions.name} done",ephemeral=True)
            reback(interaction.user.name,interaction.user.id,"slash_reload")
        else:
            await interaction.response.send_message(f"你沒資格",ephemeral=True)
##################################################################
    @app_commands.command(name="load",description="Load Cog")
    @app_commands.describe(extensions="Choices one to Load it")
    @app_commands.choices(extensions=[
        DChoice(name=f"CardBettleSys",value=1),
        DChoice(name=f"event",value=2),
        DChoice(name=f"guild",value=3),
        DChoice(name=f"rpg",value=4),
        DChoice(name=f"slashcommand",value=5)
    ])
    async def load(self,interaction:DInteracion,extensions:DChoice[int]):
        if  interaction.user.id == 403895664666214400:
            await self.bot.load_extension(f"cmds.{extensions.name}")
            await interaction.response.send_message(f"Loaded {extensions.name} done",ephemeral=True)
            reback(interaction.user.name,interaction.user.id,"slash_load")
        else:
            await interaction.response.send_message(f"你沒資格",ephemeral=True)
##################################################################
    @app_commands.command(name="unload",description="Unload Cog")
    @app_commands.describe(extensions="Choices one to Unload it")
    @app_commands.choices(extensions=[
        DChoice(name=f"CardBettleSys",value=1),
        DChoice(name=f"event",value=2),
        DChoice(name=f"guild",value=3),
        DChoice(name=f"rpg",value=4),
        DChoice(name=f"slashcommand",value=5)
    ])
    async def unload(self,interaction:DInteracion,extensions:DChoice[int]):
        if  interaction.user.id == 403895664666214400:
            await self.bot.unload_extension(f"cmds.{extensions.name}")
            await interaction.response.send_message(f"Unloaded {extensions.name} done",ephemeral=True)
            reback(interaction.user.name,interaction.user.id,"slash_unload")
        else:
            await interaction.response.send_message(f"你沒資格",ephemeral=True)
################################################################## (not done yet)
    @app_commands.command(name="info",description="you can see what about the this cat")
    @app_commands.describe(info="choice bot or owner")
    @app_commands.choices(info=[
        DChoice(name="bot",value=1),
        DChoice(name="owner",value=2)
    ])
    async def info(self, interaction:DInteracion,info:DChoice[int]):
        if info.value == 1:
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
                inline=False
            )
            cat_embed.set_footer(text="the best cat bot")
            await interaction.response.send_message(embed=cat_embed)
            reback(interaction.user.name,interaction.user.id,"slash_info_bot")
        elif info.value == 2:
            await interaction.response.send_message(f"我還沒做這個XD")
            reback(interaction.user.name,interaction.user.id,"slash_info_owner")
##################################################################
    @app_commands.command(name="ping",description="To test the latency between the guild and bot")
    async def ping(self, interaction:DInteracion):
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")
        reback(interaction.user.name,interaction.user.id,"slash_ping")
##################################################################
    @app_commands.command(name="dellog",description="delete the old log files(only for bot owner use)")
    async def dellog(self,interaction:DInteracion):
        if interaction.user.id == 403895664666214400:
            for filename in os.listdir("log"):
                if filename[8:-13] != datetime.datetime.now().strftime("%d"):
                    os.remove(f"log/{filename}")
            reback(interaction.user.name,interaction.user.id,"slash_dellog_success")
            await interaction.response.send_message(f"已刪除舊紀錄了喵!!")
        else:
            await interaction.response.send_message(f"你沒資格",ephemeral=True)
            reback(interaction.user.name,interaction.user.id,"slash_dellog_fail")
##################################################################
    @app_commands.command(name="addfood",description="Add food to the list")
    @app_commands.describe(food="Add a kind of food that you want to eat")
    async def addeat(self,ineraction:discord.Interaction,food:str):
        global food_data
        food_data["data"].append(food)
        with open("./For_Eat.json","w",encoding="utf-8") as Jfile:
            json.dump(food_data,Jfile,indent=4,ensure_ascii=False)
        await ineraction.response.send_message(f"已添加 >>>{food}<<< 到選單中，喵!!!")
        reback(ineraction.user.name,ineraction.user.id,"slash_AddEat")
        with open("./For_Eat.json","r", encoding="utf-8") as Jfile:
            data = json.load(Jfile)
##################################################################
    @app_commands.command(name="foodlist",description="To see the list of food")
    async def foodlist(self,ineraction:discord.Interaction):
        List = "|"
        for data in food_data["data"]:
            List = (f"{List + data}|")
        await ineraction.response.send_message(f"有>>>{List}<<<可以吃")
        reback(ineraction.user.name,ineraction.user.id,"slash_EatList")
##################################################################
##################################################################
##################################################################
##################################################################
async def setup(bot):
    await bot.add_cog(slashcommand(bot))