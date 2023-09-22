import discord
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import datetime
import os
import random
import json
from core.Def import custom_bot_command as CBC

DChoice = discord.app_commands.Choice

DInteracion = discord.Interaction

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
  @app_commands.describe(choices="what do yuo want to see?")
  @app_commands.choices(choices=[
      DChoice(name="your name", value=1),
      DChoice(name="your discord id", value=2),
      DChoice(name="your icon", value=3)
  ])
  async def slash(self, interaction: DInteracion, choices: DChoice[int]):
    if choices.value == 1:
      await interaction.response.send_message(
          f"{interaction.user.mention} your name is {interaction.user.name}",
          ephemeral=True)
    elif choices.value == 2:
      await interaction.response.send_message(
          f"{interaction.user.mention} your discord id is `{interaction.user.id}`",
          ephemeral=True)
    elif choices.value == 3:
      icon = interaction.user.avatar
      await interaction.response.send_message(
          f"{interaction.user.mention} your icon is here{icon}")
    reback(interaction.user.name, interaction.user.id, "slash_slash")
##################################################################

  @app_commands.command(name="reloadall", description="Reload all Cogs")
  async def reloadall(self, interaction: DInteracion):
    if interaction.user.id == 403895664666214400:
      for filename in os.listdir("cmds"):
        if filename.endswith(".py"):
          await self.bot.reload_extension(f"cmds.{filename[:-3]}")
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
  async def reload(self, interaction: DInteracion, extensions: DChoice[int]):
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
  async def load(self, interaction: DInteracion, extensions: DChoice[int]):
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
  async def unload(self, interaction: DInteracion, extensions: DChoice[int]):
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
  async def info(self, interaction: DInteracion, info: DChoice[int]):
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
  async def ping(self, interaction: DInteracion):
    await interaction.response.send_message(
        f"Pong! {round(self.bot.latency * 1000)}ms")
    reback(interaction.user.name, interaction.user.id, "slash_ping")
##################################################################
  @app_commands.command(
      name="dellog",
      description="Delete the old log files(only for bot owner use)")
  async def dellog(self, interaction: DInteracion):
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

  @app_commands.command(name="eatfood",
                        description="Random choose the food that you eat")
  async def eatfood(self, interaction: DInteracion):
    food = random.choice(food_data["data"])
    await interaction.response.send_message(
        f"{interaction.user.mention} 吃>{food}<吧喵!!")
    reback(interaction.user.name, interaction.user.id, "slash_eatfood")
##################################################################

  @app_commands.command(name="addfood", description="Add food to the list")
  @app_commands.describe(food="Add a kind of food that you want to eat")
  async def addeat(self, interaction: DInteracion, food: str):
    global food_data
    food_data["data"].append(food)
    with open("./For_Eat.json", "w", encoding="utf-8") as Jfile:
      json.dump(food_data, Jfile, indent=4, ensure_ascii=False)
    await interaction.response.send_message(f"已添加 >>>{food}<<< 到選單中，喵!!!")
    reback(interaction.user.name, interaction.user.id, "slash_AddEat")
    with open("./For_Eat.json", "r", encoding="utf-8") as Jfile:
      food_data = json.load(Jfile)
##################################################################

  @app_commands.command(name="foodlist", description="To see the list of food")
  async def foodlist(self, interaction: DInteracion):
    List = "|"
    for data in food_data["data"]:
      List = (f"{List + data}|")
    await interaction.response.send_message(f"有>>>{List}<<<可以吃")
    reback(interaction.user.name, interaction.user.id, "slash_EatList")
##################################################################
##################################################################
  @app_commands.describe(name="The name of card")
  @app_commands.command(name="create-monster-card",description="Create a new monster card")
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
          f"{interaction.user.mention} Has created a new monster card into data")
      reback(interaction.user.name, interaction.user.id, "slash_create monster card")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
##################################################################
  @app_commands.command(name="create-trap-card",description="Create a new trap card")
  @app_commands.describe(name="The name of card")
  @app_commands.describe(sp="Star points")
  async def createtrapcard(self, interaction: DInteracion, name: str,sp: int):
    if interaction.user.id == 403895664666214400:
      CBC.create_trap_card(name=name,SP=sp)
      await interaction.response.send_message(
          f"{interaction.user.mention} Has created a new trap card into data")
      reback(interaction.user.name, interaction.user.id, "slash_create trap card")
    else:
      await interaction.response.send_message(f"你沒資格", ephemeral=True)
##################################################################
##################################################################
async def setup(bot):
  await bot.add_cog(slashcommand(bot))
