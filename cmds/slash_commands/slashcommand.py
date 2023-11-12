import discord
from discord import interactions
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import datetime
import os
import random
import pprint
import json
from core.Def import custom_bot_command as CBC
from core.button_and_selection import * 


DChoice = discord.app_commands.Choice

DInteraction = discord.Interaction

reback = CBC.reback

with open('guild_info.json', mode='r', encoding="utf-8") as file:
  guild_info = json.load(file)

with open("./For_Eat.json", "r", encoding="utf-8") as Jfile:
  food_data = json.load(Jfile)


class slashcommand(Cog_Extension):

  def __init__(self, bot: commands.Bot):
    self.bot = bot
##################################################################

  @app_commands.command(name="slash", description="for test")
  @app_commands.describe(user="you or other one")
  @app_commands.describe(choices="what do yuo want to see?")
  @app_commands.choices(choices=[
      DChoice(name="name", value=1),
      DChoice(name="discord id", value=2),
      DChoice(name="icon", value=3)
  ])
  async def slash(self, interaction: DInteraction,user:discord.Member, choices: DChoice[int]):
    if choices.value == 1:
      await interaction.response.send_message(
          f"{interaction.user.mention} name is {user.name}",
          ephemeral=True)
    elif choices.value == 2:
      await interaction.response.send_message(
          f"{interaction.user.mention} discord id is {user.id}",
          ephemeral=True)
    elif choices.value == 3:
      icon = user.avatar
      await interaction.response.send_message(
          f"{interaction.user.mention} icon is here{icon}")
    reback(interaction.user.name, interaction.user.id, "slash_slash")
##################################################################
  @app_commands.command(name="help", description="The help menu")
  async def help(self,interaction:DInteraction):
    await interaction.response.send_message(view=slash_Help_Menu())
    reback(interaction.user.name, interaction.user.id,"slash_help")
##################################################################

  @app_commands.command(name="reloadall", description="Reload all Cogs")
  async def reloadall(self, interaction: DInteraction):
    if interaction.user.id == 403895664666214400:
      for filename in os.listdir("cmds"):
        if filename.endswith(".py"):
          await self.bot.reload_extension(f"cmds.{filename[:-3]}")
      for filename in os.listdir("cmds/slash_commands"):
        if filename.endswith(".py"):
          await self.bot.reload_extension(f"cmds.slash_commands.{filename[:-3]}")
      await interaction.response.send_message(f"Has reloaded all extensions",
                                              ephemeral=True)
      reback(interaction.user.name, interaction.user.id, "slash_reloadall")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
##################################################################

  @app_commands.command(name="reload", description="Reload Cog")
  @app_commands.describe(extensions="Choices one to reload it")
  @app_commands.choices(extensions=[
      DChoice(name=f"CardBettleSys", value=1),
      DChoice(name=f"event", value=2),
      DChoice(name=f"guild", value=3),
      DChoice(name=f"rpg", value=4),
      DChoice(name=f"slashcommand", value=5)
  ])
  async def reload(self, interaction: DInteraction, extensions: DChoice[int]):
    if interaction.user.id == 403895664666214400:
      await self.bot.reload_extension(f"cmds.{extensions.name}")
      await interaction.response.send_message(
          f"Reloaded {extensions.name} done", ephemeral=True)
      reback(interaction.user.name, interaction.user.id, "slash_reload")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
##################################################################

  @app_commands.command(name="load", description="Load Cog")
  @app_commands.describe(extensions="Choices one to Load it")
  @app_commands.choices(extensions=[
      DChoice(name=f"CardBettleSys", value=1),
      DChoice(name=f"event", value=2),
      DChoice(name=f"guild", value=3),
      DChoice(name=f"rpg", value=4),
      DChoice(name=f"slashcommand", value=5)
  ])
  async def load(self, interaction: DInteraction, extensions: DChoice[int]):
    if interaction.user.id == 403895664666214400:
      await self.bot.load_extension(f"cmds.{extensions.name}")
      await interaction.response.send_message(f"Loaded {extensions.name} done",
                                              ephemeral=True)
      reback(interaction.user.name, interaction.user.id, "slash_load")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
##################################################################

  @app_commands.command(name="unload", description="Unload Cog")
  @app_commands.describe(extensions="Choices one to Unload it")
  @app_commands.choices(extensions=[
      DChoice(name=f"CardBettleSys", value=1),
      DChoice(name=f"event", value=2),
      DChoice(name=f"guild", value=3),
      DChoice(name=f"rpg", value=4),
      DChoice(name=f"slashcommand", value=5)
  ])
  async def unload(self, interaction: DInteraction, extensions: DChoice[int]):
    if interaction.user.id == 403895664666214400:
      await self.bot.unload_extension(f"cmds.{extensions.name}")
      await interaction.response.send_message(
          f"Unloaded {extensions.name} done", ephemeral=True)
      reback(interaction.user.name, interaction.user.id, "slash_unload")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
################################################################## (not done yet)

  @app_commands.command(name="info",
                        description="You can see what about the this cat")
  @app_commands.describe(info="choice bot or owner")
  @app_commands.choices(
      info=[DChoice(name="bot", value=1),
            DChoice(name="owner", value=2)])
  async def info(self, interaction: DInteraction, info: DChoice[int]):
    if info.value == 1:
      cat_embed = discord.Embed(title="關於Mew機器人",
                                description="uwu!!",
                                color=0xffc21a,
                                timestamp=datetime.datetime.now())
      cat_embed.set_author(
          name="Yurei",
          url="https://discord.gg/t7SXq4E5pF",
          icon_url=
          "https://cdn.discordapp.com/attachments/693782101463400498/1147878445406228610/icon.png"
      )
      cat_embed.add_field(
          name="邀請連結",
          value=
          "https://discord.com/api/oauth2/authorize?client_id=1147725051421016276&permissions=8&scope=bot",
          inline=False)
      cat_embed.set_footer(text="the best cat bot")
      await interaction.response.send_message(embed=cat_embed)
      reback(interaction.user.name, interaction.user.id, "slash_info_bot")
    elif info.value == 2:
      await interaction.response.send_message(f"我還沒做這個XD")
      reback(interaction.user.name, interaction.user.id, "slash_info_owner")
##################################################################

  @app_commands.command(
      name="ping", description="To test the latency between the guild and bot")
  async def ping(self, interaction: DInteraction):

    await interaction.response.send_message(
        f"Wait for your ping!!!",view=ping_button(ms=round(self.bot.latency * 10000)))
    reback(interaction.user.name, interaction.user.id, "slash_ping")
##################################################################

  @app_commands.command(
      name="dellog",
      description="Delete the old log files(only for bot owner use)")
  async def dellog(self, interaction: DInteraction):
    if interaction.user.id == 403895664666214400:
      for filename in os.listdir("log"):
        if filename[8:-13] != datetime.datetime.now().strftime("%d"):
          os.remove(f"log/{filename}")
      reback(interaction.user.name, interaction.user.id,
             "slash_dellog_success")
      await interaction.response.send_message(f"已刪除舊紀錄了喵!!")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
      reback(interaction.user.name, interaction.user.id, "slash_dellog_fail")
##################################################################

async def setup(bot):
  await bot.add_cog(slashcommand(bot))
