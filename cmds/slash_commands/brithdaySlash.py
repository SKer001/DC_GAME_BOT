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

class brithdaySlash(Cog_Extension):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
##################################################################
  @app_commands.command(name="remember-me", description="The bot will remember you brithday!!!")
  @app_commands.describe(yyyy="full numbers or last two numbers")
  @app_commands.describe(mm="month")
  @app_commands.describe(dd="date")
  async def remembera_me(self,interaction:DInteraction,yyyy:str,mm:str,dd:str):
    resource = CBC.datetime_translate([yyyy,mm,dd])
    if resource in ["Year-error", "month-error", "date-error"]:
      await interaction.response.send_message(f"有東西打錯了喵!!! {resource}")
    else:
      CBC.birth_data(
        name=interaction.user.name,
        id=interaction.user.id,
        birthday=[
          resource[0],
          resource[1],
          resource[2]
        ]
      )
      await interaction.response.send_message(f"{interaction.user.mention}的生日是 {resource[0]}年{resource[1]}月{resource[2]}日，我記得了喵!!!")
    reback(interaction.user.name, interaction.user.id, "slash remember me")
##################################################################
async def setup(bot):
  await bot.add_cog(brithdaySlash(bot))