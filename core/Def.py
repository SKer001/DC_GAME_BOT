import discord
from discord.ext import commands
import json
import os
import asyncio
import datetime

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True
intents.guilds = True

bot_def = commands.Bot(command_prefix='^', intents=intents)

path = "log/" + str(
    datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt"


class custom_bot_command():

  def create_monster_card(name: str, ATK: int, DEF: int, MATK: int, MDEF: int,
                          HP: int, AGI: int, CON: str, SP: int):
    with open(f"cards/monster.json", "r", encoding="utf-8") as file:
      filecard = list(json.load(file))
    card_dic_basic = {
        "name": name,
        "ATK": ATK,
        "DEF": DEF,
        "MATK": MATK,
        "MDEF": MDEF,
        "HP": HP,
        "AGI": AGI,
        "CON": CON,
        "SP": SP,
        "description": ""
    }
    filecard.append(card_dic_basic)
    with open(f"cards/monster.json", "w", encoding="utf-8") as CardFile:
      json.dump(filecard, CardFile, indent=4, ensure_ascii=False)

  def reback(user_name, user_id, command):
    print(
        f"{datetime.datetime.utcnow()} used {command} by {user_name} {user_id}"
    )
    with open(path, "a", encoding="utf-8") as LogFile:
      LogFile.write(
          f"{datetime.datetime.now()} used {command} by {user_name} {user_id}\n"
      )
