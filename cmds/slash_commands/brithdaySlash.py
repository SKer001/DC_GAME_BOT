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

def load_birthday():
  with open(f"birthday.json", "r", encoding="utf-8") as Bfile:
    return json.load(Bfile)
  
def updata_birthday(file):
  with open(f"birthday.json","w",encoding="utf-8") as Bfile:
    json.dump(file, Bfile,indent=4)

class brithdaySlash(Cog_Extension):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
##################################################################
    async def check_birthday():
      await self.bot.wait_until_ready()
      while not self.bot.is_closed():
        await asyncio.sleep(10)
        birth_data = load_birthday()
        today = [int(datetime.datetime.now().strftime("%m")), int(datetime.datetime.now().strftime("%d"))]
        if bool(birth_data):
          for guild in birth_data.keys():
            celebrate_channel = self.bot.get_channel(birth_data[guild]["celebrate_channel"])
            for user in birth_data[guild].keys():
              if user != "celebrate_channel":
                User = self.bot.get_user(int(user))
                tf1 = birth_data[guild][user]["birthday"][1] == today[0] 
                tf2 = birth_data[guild][user]["birthday"][2] == today[1] 
                tf3 = birth_data[guild][user]["celebrated"] == False
                if tf1 and tf2 and tf3:
                  await celebrate_channel.send(f"{User.mention} 祝你生日快樂!!!")
                  birth_data[guild][user]["celebrated"] = True
                  updata_birthday(birth_data)
                  reback(User.name,User.id,"birthday")
                elif (not tf1) or (not tf2):
                  birth_data[guild][user]["celebrated"] = False
                  updata_birthday(birth_data)
              else:
                pass
    self.bg_task = self.bot.loop.create_task(check_birthday())
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
      CBC.birth_set_date(
        name=interaction.user.name,
        id=interaction.user.id,
        guild_id=interaction.user.guild.id,
        birthday=[
          resource[0],
          resource[1],
          resource[2]
        ]
      )

    await interaction.response.send_message(f"{interaction.user.mention}的生日是 {resource[0]}年{resource[1]}月{resource[2]}日，我記得了喵!!!")
    reback(interaction.user.name, interaction.user.id, "slash remember me")
##################################################################
  @app_commands.command(name="set-birthday-channel",description="set birthday channel for celebrating")
  @app_commands.describe(channel="which text channel you want to celebrate birthday")
  async def set_birthday_channel(self,interaction:DInteraction,channel:discord.TextChannel=None):
    if channel != None:
      CBC.birth_set_channel(channel)
      await interaction.response.send_message(f"慶生頻道已經設在{channel.mention}了喵!!!")
    else:
      CBC.birth_set_channel(interaction.channel)
      await interaction.response.send_message(f"慶生頻道已經設在{interaction.channel.mention}了喵!!!")
##################################################################
async def setup(bot):
  await bot.add_cog(brithdaySlash(bot))