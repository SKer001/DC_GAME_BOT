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


DChoice = discord.app_commands.Choice

DInteracion = discord.Interaction

reback = CBC.reback

def food_data():
  with open("./For_Eat.json", "r", encoding="utf-8") as Jfile:
    food_data = json.load(Jfile)
  return food_data

def food_update(something):
  with open("./For_Eat.json", "w", encoding="utf-8") as Jfile:
    json.dump(something, Jfile, indent=4, ensure_ascii=False)


class slash_food(Cog_Extension):
  @app_commands.command(name="eatfood",
                        description="Random choose the food that you eat")
  async def eatfood(self, interaction: DInteracion):
    foods = food_data()
    food = random.choice(foods["data"])
    await interaction.response.send_message(
        f"{interaction.user.mention} 吃>{food}<吧喵!!")
    reback(interaction.user.name, interaction.user.id, "slash_eatfood")
##################################################################
  @app_commands.command(name="addfood", description="Add food to the list")
  @app_commands.describe(addfood="Add a kind of food that you want to eat")
  async def addeat(self, interaction: DInteracion, addfood: str):
    food = food_data()
    food["data"].append(addfood)
    food_update(food)
    await interaction.response.send_message(f"已添加 >>>{addfood}<<< 到選單中，喵!!!")
    reback(interaction.user.name, interaction.user.id, "slash_AddEat")
##################################################################
  @app_commands.command(name="foodlist", description="To see the list of food")
  async def foodlist(self, interaction: DInteracion):
    food = food_data()
    List = "|"
    for data in food["data"]:
      List = (f"{List + data}|")
    await interaction.response.send_message(f"有>>>{List}<<<可以吃")
    reback(interaction.user.name, interaction.user.id, "slash_EatList")
##################################################################

async def setup(bot):
  await bot.add_cog(slash_food(bot))