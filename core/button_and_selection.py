from typing import Optional
import discord
from discord.ext import commands
import json
import os
import asyncio
import datetime
import requests

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True
intents.guilds = True

bot_def = commands.Bot(command_prefix='^', intents=intents)

DInteraction = discord.Interaction

DMember = discord.Member

DButton = discord.ui.button

DSelection = discord.ui.Select

DView = discord.ui.View

class ping_button(discord.ui.View):
  def __init__(self,ms:int):
    super().__init__()
    self.ms = ms

  @discord.ui.button(label="ping me!!!",style=discord.ButtonStyle.green)
  async def ping(self,interaction:DInteraction,button:DButton):
    await interaction.response.send_message(f"{interaction.user.mention} Pong! {self.ms}ms")

class slash_Help_Menu(DView):
  def __init__(self):
    super().__init__()

  @discord.ui.select(max_values=1,min_values=1,placeholder="Choose a page",options=
                [discord.SelectOption(
                    label="Page 1",
                    value="1",
                    description="About this bot",
                    emoji="1️⃣",
                    ),
                discord.SelectOption(
                    label="Page 2",
                    value="2",
                    description="About food command",
                    emoji="2️⃣"
                    ),
                discord.SelectOption(
                    label="Page 3",
                    value="3",
                    description="About card command",
                    emoji="3️⃣"
                    ),
                discord.SelectOption(
                    label="Page 4",
                    value="4",
                    description="About other command",
                    emoji="4️⃣"
                    )
                ]
             )
  async def helpmenu(self,interaction:DInteraction,selection:DSelection):
    message_id = interaction.message.id
    print(selection.values[0])
    if selection.values[0] == "1":
      await interaction.response.send_message("you choose 1")
      await interaction.followup.edit_message(message_id=message_id,view=self)
    elif selection.values[0] == "2":
      await interaction.response.send_message("you choose 2")
      await interaction.followup.edit_message(message_id=message_id,view=self)
    elif selection.values[0] == "3":
      await interaction.response.send_message("you choose 3")
      await interaction.followup.edit_message(message_id=message_id,view=self)
    elif selection.values[0] == "4":
      await interaction.response.send_message("you choose 4")
      await interaction.followup.edit_message(message_id=message_id,view=self)
    pass