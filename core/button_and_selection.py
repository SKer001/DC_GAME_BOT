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

  def __init__(self, ms: int):
    super().__init__()
    self.ms = ms

  @discord.ui.button(label="ping me!!!", style=discord.ButtonStyle.green)
  async def ping(self, interaction: DInteraction, button: DButton):
    await interaction.response.send_message(
        f"{interaction.user.mention} Pong! {self.ms}ms")


class slash_Help_Menu(DView):

  def __init__(self):
    super().__init__()

  @discord.ui.select(max_values=1,
                     min_values=1,
                     placeholder="Choose a page",
                     options=[
                         discord.SelectOption(
                             label="Page 1",
                             value="1",
                             description="About this bot",
                             emoji="1️⃣",
                         ),
                         discord.SelectOption(label="Page 2",
                                              value="2",
                                              description="About food command",
                                              emoji="2️⃣"),
                         discord.SelectOption(label="Page 3",
                                              value="3",
                                              description="About card command",
                                              emoji="3️⃣"),
                         discord.SelectOption(
                             label="Page 4",
                             value="4",
                             description="About other command",
                             emoji="4️⃣")
                     ])
  async def helpmenu(self, interaction: DInteraction, selection: DSelection):
    message_id = interaction.message.id

    page_1 = discord.Embed(title="第一頁", description="關於機器人", color=0xe202f2)
    page_1.add_field(
      name="做這個機器人的理由?",
      value="純粹就是因為不想用付費的機器人XD",
      inline=False
      )
    page_1.add_field(
      name="這機器人的未來發展?",
      value="努力地朝著縫合怪之王的稱號前進",
      inline=False
      )
    page_1.add_field(
      name="關於指令",
      value="[XXX]為必要參數\n{XXX}則為非必要參數",
      inline=False
      )

    page_2 = discord.Embed(title="第二頁", description="關於食物的指令", color=0xe202f2)
    page_2.add_field(
      name="隨機性選擇主餐",
      value="/eatfood",
      inline=False
      )
    page_2.add_field(
      name="增加主餐選擇",
      value="/addfood [addfood]",
      inline=False
      )
    page_2.add_field(
      name="查看食物的表單",
      value="/foodlist",
      inline=False
      )

    page_3 = discord.Embed(title="第三頁", description="關於卡牌的指令", color=0xe202f2)

    page_4 = discord.Embed(title="第四頁", description="關於其他的指令", color=0xe202f2)

    if selection.values[0] == "1":
      await interaction.response.edit_message(embed=page_1, view=self)
      #await interaction.followup.edit_message(message_id=message_id, view=self)
    elif selection.values[0] == "2":
      await interaction.response.edit_message(embed=page_2, view=self)
      #await interaction.followup.edit_message(message_id=message_id, view=self)
    elif selection.values[0] == "3":
      await interaction.response.edit_message(embed=page_3, view=self)
      #await interaction.followup.edit_message(message_id=message_id, view=self)
    elif selection.values[0] == "4":
      await interaction.response.edit_message(embed=page_4, view=self)
      #await interaction.followup.edit_message(message_id=message_id, view=self)
    pass
