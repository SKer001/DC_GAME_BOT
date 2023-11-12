import discord
from discord import interactions
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import datetime
import os
import random
import json
from core.Def import *

CBC = custom_bot_command


DChoice = discord.app_commands.Choice

DInteracion = discord.Interaction

reback = CBC.reback

all_tag = []

def get_all_food_tag():
  global all_tag 
  all_tag_keys = CBC.load_food_tag()
  values = 1
  for data in all_tag_keys:
    all_tag.append(DChoice(name=data,value=values))
    values += 1

get_all_food_tag()

class slash_food(Cog_Extension):
  @app_commands.command(name="eat-food",description="Random choose the food that you eat")
  async def eatfood(self, interaction: DInteracion):
    # foods = CBC.load_food_data()
    # food = random.choice(foods["total"])
    # await interaction.response.send_message(
    #     f"{interaction.user.mention} 吃>{food}<吧喵!!")
    # reback(interaction.user.name, interaction.user.id, "slash_eatfood")
    pass
##################################################################
  @app_commands.command(name="add-food", description="Add food to the list")
  @app_commands.describe(addfood="Add a kind of food that you want to eat") 
  @app_commands.describe(tag1="Add the food's tag")
  @app_commands.describe(tag2="Add the food's tag")
  @app_commands.describe(tag3="Add the food's tag")
  @app_commands.describe(tag4="Add the food's tag")
  @app_commands.describe(tag5="Add the food's tag")
  @app_commands.choices(
    tag1=all_tag,
    tag2=all_tag,
    tag3=all_tag,
    tag4=all_tag,
    tag5=all_tag
    )
  async def addeat(
    self,
    interaction:DInteracion,
    addfood:str,
    tag1:DChoice[int]=None,
    tag2:DChoice[int]=None,
    tag3:DChoice[int]=None,
    tag4:DChoice[int]=None,
    tag5:DChoice[int]=None
    ):
    tags = [tag1, tag2, tag3, tag4, tag5]
    New_tags = []
    for i in tags:
      if i is not None:
        New_tags.append(i.name)
    CBC.add_food_in(food_name=addfood,food_tags=New_tags)
    await interaction.response.send_message(f"已添加 >>>{addfood}<<< 到選單中，喵!!!")
    reback(interaction.user.name, interaction.user.id, "slash_AddEat")
    pass
##################################################################
  @app_commands.command(name="food-list", description="To see the list of food")
  async def foodlist(self, interaction: DInteracion):
    foods = load_food()
    List = "|"
    for data in (foods["total"].keys()):
      List += f"{data}|"
    await interaction.response.send_message(f"有>>>{List}<<<可以吃")
    reback(interaction.user.name, interaction.user.id, "slash_EatList")
    pass
##################################################################

async def setup(bot):
  await bot.add_cog(slash_food(bot))