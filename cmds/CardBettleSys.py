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
    @commands.command()
    async def CreateCard(self,ctx,name:str,ATK:int,DEF:int,MATK:int,MDEF:int,HP:int,AGI:int,CON:str,SP:int):
        if CON == "光" or "暗" or "水" or "火" or "木" or "土" and ctx.author.id == 403895664666214400:
            if ctx.author.id == 403895664666214400:
                CBC.create_card(name=name,ATK=ATK,DEF=DEF,MATK=MATK,MDEF=MDEF,HP=HP,AGI=AGI,CON=CON,SP=SP)
                await ctx.send(f"{ctx.author.mention} Has created a new card into data")
                reback(ctx.author.name,ctx.author.id,"Create Card")
        else:
            await ctx.send(f"你沒資格")
        pass
async def setup(bot):
    await bot.add_cog(CardBettleSys(bot))