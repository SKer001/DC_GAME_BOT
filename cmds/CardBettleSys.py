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
    return_data = CBC.check_card(type, name)
    if return_data != False:
      if type == "magics":

        stars_str = str("")
        for i in range(int(return_data["SP"])):
          stars_str = stars_str + "✨"

        magic_embed = discord.Embed(title="Mew", description="卡牌小助手")
        magic_embed.set_author(
            name=stars_str,
            icon_url=
            "https://cdn.discordapp.com/avatars/1147725051421016276/4d6b2777f0d18dfea2c67abb4fe8b911.png?size=4096"
        )
        magic_embed.add_field(name="卡牌名字",
                              value=return_data['name'],
                              inline=True)
        magic_embed.add_field(name="種類", value=type.name, inline=True)
        magic_embed.add_field(name="技能",
                              value=return_data['skill'],
                              inline=False)
        magic_embed.add_field(name="=========卡牌介紹=========",
                              value=return_data['skill-description'],
                              inline=False)
        await ctx.send(embed=magic_embed)
      elif type == "monsters":

        stars_str = str("")
        for i in range(int(return_data["SP"])):
          stars_str = stars_str + "✨"

        monster_embed = discord.Embed(title="Mew", description="卡牌小助手")
        monster_embed.set_author(
            name=stars_str,
            icon_url=
            "https://cdn.discordapp.com/avatars/1147725051421016276/4d6b2777f0d18dfea2c67abb4fe8b911.png?size=4096"
        )
        monster_embed.add_field(name="卡牌名字",
                                value=return_data['name'],
                                inline=True)
        monster_embed.add_field(name="種類", value=type.name, inline=False)
        monster_embed.add_field(name="攻擊力",
                                value=return_data['ATK'],
                                inline=True)
        monster_embed.add_field(name="魔法攻擊力",
                                value=return_data['MATK'],
                                inline=True)
        monster_embed.add_field(name="防禦力",
                                value=return_data['DEF'],
                                inline=True)
        monster_embed.add_field(name="魔法防禦力",
                                value=return_data['MDEF'],
                                inline=True)
        monster_embed.add_field(name="生命值",
                                value=return_data['HP'],
                                inline=True)
        monster_embed.add_field(name="閃避率",
                                value=return_data['AGI'],
                                inline=True)
        monster_embed.add_field(name="屬性",
                                value=return_data['CON'],
                                inline=False)
        monster_embed.add_field(name="=========卡牌介紹=========",
                                value=return_data['description'],
                                inline=False)
        monster_embed.set_footer(text="牌牌好好玩🎉🎉🎉")

        await ctx.send(embed=monster_embed)
      elif type == "traps":

        stars_str = str("")

        for i in range(int(return_data["SP"])):
          stars_str = stars_str + "✨"

        trap_embed = discord.Embed(title="Mew", description="卡牌小助手")
        trap_embed.set_author(
            name=stars_str,
            icon_url=
            "https://cdn.discordapp.com/avatars/1147725051421016276/4d6b2777f0d18dfea2c67abb4fe8b911.png?size=4096"
        )
        trap_embed.add_field(name="卡牌名字",
                             value=return_data['name'],
                             inline=True)
        trap_embed.add_field(name="種類", value=type.name, inline=True)
        trap_embed.add_field(name="技能",
                             value=return_data['skill'],
                             inline=False)
        trap_embed.add_field(name="=========卡牌介紹=========",
                             value=return_data['skill-description'],
                             inline=False)
        await ctx.send(embed=trap_embed)
    else:
      await ctx.send(f"種類或名字打錯了喵!")
    reback(ctx.author.name, ctx.author.id, " Check Cards")
################################################################################################################################
async def setup(bot):
  await bot.add_cog(CardBettleSys(bot))
