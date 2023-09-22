import discord
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import random
import json
from core.Def import custom_bot_command as CBC

options = discord.app_commands.Choice

reback = CBC.reback

class CardBettleSys(Cog_Extension):
    @commands.group()
    async def cards(self,ctx):
        pass
################################################################################################################################
    @cards.group()
    async def monster(self,ctx):
        pass
    @cards.group()
    async def trap(self,ctx):
        pass
    @cards.group()
    async def magic(self,ctx):
        pass
################################################################################################################################
    @monster.command()
    async def CreateMonster(self,ctx,name:str,ATK:int,DEF:int,MATK:int,MDEF:int,HP:int,AGI:int,CON:str,SP:int):
        if CON == "光" or "暗" or "水" or "火" or "木" or "土" and ctx.author.id == 403895664666214400:
            if ctx.author.id == 403895664666214400:
                CBC.create_monster_card(name=name,ATK=ATK,DEF=DEF,MATK=MATK,MDEF=MDEF,HP=HP,AGI=AGI,CON=CON,SP=SP)
                await ctx.send(f"{ctx.author.mention} Has created a new monster card into data")
                reback(ctx.author.name,ctx.author.id,"Create Monster Card")
        else:
            await ctx.send(f"你沒資格")
################################################################################################################################
    @trap.command()
    async def CreateTrap(self,ctx,name:str,SP:int):
        if ctx.author.id == 403895664666214400:
            CBC.create_card(name=name,SP=SP)
            await ctx.send(f"{ctx.author.mention} Has created a new trap card into data")
            reback(ctx.author.name,ctx.author.id,"Create Trap Card")
        else:
            await ctx.send(f"你沒資格")
################################################################################################################################
    @magic.command()
    async def CreateMagic(self,ctx,name:str,SP:int):
        if ctx.author.id == 403895664666214400:
            CBC.create_card(name=name,SP=SP)
            await ctx.send(f"{ctx.author.mention} Has created a new magic card into data")
            reback(ctx.author.name,ctx.author.id,"Create Magic Card")
        else:
            await ctx.send(f"你沒資格")
################################################################################################################################
async def setup(bot):
    await bot.add_cog(CardBettleSys(bot))