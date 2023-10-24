import discord
from discord import interactions
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import datetime
import os
import random
import json
from core.Def import custom_bot_command as CBC
from core.Def import Card_Bettle_System as CBS


DChoice = discord.app_commands.Choice

DInteracion = discord.Interaction

DMember = discord.Member

reback = CBC.reback

class slash_crad_bettle_sys(Cog_Extension):
  @app_commands.command(name="create-monster-card",
                        description="Create a new monster card")
  @app_commands.describe(name="The name of card")
  @app_commands.describe(atk="Attack power")
  @app_commands.describe(defense="Defense")
  @app_commands.describe(matk="Magic attack power")
  @app_commands.describe(mdef="Magic defense")
  @app_commands.describe(hp="Health Points")
  @app_commands.describe(agi="Agility")
  @app_commands.describe(con="Constitutioncards")
  @app_commands.choices(con=[
      DChoice(name="光", value=1),
      DChoice(name="暗", value=2),
      DChoice(name="水", value=3),
      DChoice(name="火", value=4),
      DChoice(name="木", value=5),
      DChoice(name="土", value=6)
  ])
  @app_commands.describe(sp="Star points")
  async def createmonstercard(self, interaction: DInteracion, name: str,
                              atk: int, defense: int, matk: int, mdef: int,
                              hp: int, agi: int, con: DChoice[int], sp: int):
    if interaction.user.id == 403895664666214400:
      CBC.create_monster_card(name=name,
                              ATK=atk,
                              DEF=defense,
                              MATK=matk,
                              MDEF=mdef,
                              HP=hp,
                              AGI=agi,
                              CON=con.name,
                              SP=sp)
      await interaction.response.send_message(
          f"{interaction.user.mention} Has created a new monster card into data"
      )
      reback(interaction.user.name, interaction.user.id,
             "slash_create monster card")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
##################################################################
  @app_commands.command(name="create-trap-card",
                        description="Create a new trap card")
  @app_commands.describe(name="The name of card")
  @app_commands.describe(skill="The name of skill")
  @app_commands.describe(sp="Star points")
  async def createtrapcard(self, interaction: DInteracion, name: str,
                           skill: str, sp: int):
    if interaction.user.id == 403895664666214400:
      CBC.create_trap_card(name=name, SK=skill, SP=sp)
      await interaction.response.send_message(
          f"{interaction.user.mention} Has created a new trap card into data")
      reback(interaction.user.name, interaction.user.id,
             "slash_create trap card")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
##################################################################
  @app_commands.command(name="create-magic-card",
                        description="Create a new magic card")
  @app_commands.describe(name="The name of card")
  @app_commands.describe(skill="The name of skill")
  @app_commands.describe(sp="Star points")
  async def createmagiccard(self, interaction: DInteracion, name: str,
                            skill: str, sp: int):
    if interaction.user.id == 403895664666214400:
      CBC.create_magic_card(name=name, SK=skill, SP=sp)
      await interaction.response.send_message(
          f"{interaction.user.mention} Has created a new magic card into data")
      reback(interaction.user.name, interaction.user.id,
             "slash_create magic card")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
##################################################################
  @app_commands.command(name="check-card", description="Check the card")
  @app_commands.describe(type="The type of card")
  @app_commands.choices(type=[
      DChoice(name="monsters", value=1),
      DChoice(name="magics", value=2),
      DChoice(name="traps", value=3)
  ])
  @app_commands.describe(name="The name of card")
  async def checkcard(self, interaction: DInteracion, type: DChoice[int],
                      name: str):
    return_data = CBC.check_card(type.name, name)
    if return_data != False:
      if type.name == "magics":

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
        await interaction.response.send_message(embed=magic_embed)
      elif type.name == "monsters":

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

        await interaction.response.send_message(embed=monster_embed)
      elif type.name == "traps":

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
        await interaction.response.send_message(embed=trap_embed)
    else:
      await interaction.response.send_message(f"種類或名字打錯了喵!")
    reback(interaction.user.name, interaction.user.id, "slash Check Cards")
##################################################################
  @app_commands.command(name="card_fight",description="The local cradfight")
  @app_commands.describe(competitor="yo~~ battle")
  async def card_fight(self, interaction:DInteracion,competitor:DMember):
    duelist = interaction.user
    CBS.start_game(duelist=duelist,competitor=competitor)
    await interaction.response.send_message(f"注意!! {duelist.mention}將要跟{competitor.mention}進行決鬥!!")
##################################################################
    pass

async def setup(bot):
  await bot.add_cog(slash_crad_bettle_sys(bot))