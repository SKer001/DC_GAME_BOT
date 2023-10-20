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
  async def cards(self, ctx):
    pass
################################################################################################################################

  @cards.group()
  async def monster(self, ctx):
    pass

  @cards.group()
  async def trap(self, ctx):
    pass

  @cards.group()
  async def magic(self, ctx):
    pass

  @cards.group()
  async def check(self, ctx):
    pass
################################################################################################################################

  @monster.command()
  async def CreateMonster(self, ctx, name: str, ATK: int, DEF: int, MATK: int,
                          MDEF: int, HP: int, AGI: int, CON: str, SP: int):
    if CON == "光" or "暗" or "水" or "火" or "木" or "土" and ctx.author.id == 403895664666214400:
      if ctx.author.id == 403895664666214400:
        CBC.create_monster_card(name=name,
                                ATK=ATK,
                                DEF=DEF,
                                MATK=MATK,
                                MDEF=MDEF,
                                HP=HP,
                                AGI=AGI,
                                CON=CON,
                                SP=SP)
        await ctx.send(
            f"{ctx.author.mention} Has created a new monster card into data")
        reback(ctx.author.name, ctx.author.id, "Create Monster Card")
    else:
      await ctx.send(f"你沒資格")
################################################################################################################################

  @trap.command()
  async def CreateTrap(self, ctx, name: str,skill:str, SP: int):
    if ctx.author.id == 403895664666214400:
      CBC.create_card(name=name,SK=skill,SP=SP)
      await ctx.send(
          f"{ctx.author.mention} Has created a new trap card into data")
      reback(ctx.author.name, ctx.author.id, "Create Trap Card")
    else:
      await ctx.send(f"你沒資格")
################################################################################################################################

  @magic.command()
  async def CreateMagic(self, ctx, name: str,skill:str, SP: int):
    if ctx.author.id == 403895664666214400:
      CBC.create_card(name=name,SK=skill, SP=SP)
      await ctx.send(
          f"{ctx.author.mention} Has created a new magic card into data")
      reback(ctx.author.name, ctx.author.id, "Create Magic Card")
    else:
      await ctx.send(f"你沒資格")
################################################################################################################################

  @check.command()
  async def CheckCards(self, ctx, type: str, name: str):
    return_data = CBC.check_card(type,name)
    if return_data != False:
      if type == "magics":
        Name = (f"Name : {return_data['name']}\n")
        SP = (f"Star points : {return_data['SP']}\n")
        SK = (f"Skilld's description : {return_data['skill-description']}")
        await ctx.send(f"card's information:\n>>>{type}<<<\n{Name}{SP}{SK}")
      elif type == "monsters":
        Name = (f"Name : {return_data['name']}\n")
        atk = (f"ATK : {return_data['ATK']}\n")
        Def = (f"DEF : {return_data['DEF']}\n")
        matk = (f"MATK : {return_data['MATK']}\n")
        mdef = (f"MDEF : {return_data['MDEF']}\n")
        hp = (f"HP : {return_data['HP']}\n")
        agi = (f"AGI : {return_data['AGI']}\n")
        con = (f"CON : {return_data['CON']}\n")
        SP = (f"Star points : {return_data['SP']}\n")
        desc = (f"description : {return_data['description']}")
        await ctx.send(f"card's information:\n>>>{type}<<<\n{Name}{atk}{Def}{matk}{mdef}{hp}{agi}{con}{SP}{desc}")
      elif type == "traps":
        Name = (f"Name : {return_data['name']}\n")
        SP = (f"Star points : {return_data['SP']}\n")
        SK = (f"Skilld's description : {return_data['skill-description']}")
        await ctx.send(f"card's information:\n>>>{type}<<<\n{Name}{SP}{SK}")
    else:
      await ctx.send(f"種類或名字打錯了喵!")
    reback(ctx.author.name, ctx.author.id, "Check Cards")
################################################################################################################################
async def setup(bot):
  await bot.add_cog(CardBettleSys(bot))
