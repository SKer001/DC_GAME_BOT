from typing import Optional
import discord
from discord.ext import commands
import json
import os
import asyncio
import datetime
import requests
import calendar

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True
intents.guilds = True

bot_def = commands.Bot(command_prefix='^', intents=intents)

DInteraction = discord.Interaction

DMember = discord.Member

DButton = discord.ui.Button

path = "log/" + str(
    datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt"

def create_game_match(duelist):
  with open(f"match/{duelist}.json", 'w',encoding="utf-8") as Mfile:
    pass

def updata_match_info(user,something):
  with open(f"match/{user}.json", "w",encoding="utf-8") as Mfile:
    json.dump(something, Mfile,indent=4)

def load_birthday():
  with open(f"birthday.json", "r", encoding="utf-8") as Bfile:
    return json.load(Bfile)
  
def updata_birthday(file):
  with open(f"birthday.json","w",encoding="utf-8") as Bfile:
    json.dump(file, Bfile,indent=4)

def load_food():
  with open("./For_Eat.json", "r", encoding="utf-8") as Jfile:
    food_data = json.load(Jfile)
  return food_data

def food_updata(something):
  with open("./For_Eat.json", "w", encoding="utf-8") as Jfile:
    json.dump(something, Jfile, indent=4, ensure_ascii=False)

class custom_bot_command():
  ################################################################################################################################
  def create_monster_card(name: str, ATK: int, DEF: int, MATK: int, MDEF: int,
                          HP: int, AGI: int, CON: str, SP: int):
    with open(f"cards/monsters.json", "r", encoding="utf-8") as file:
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
    with open(f"cards/monsters.json", "w", encoding="utf-8") as CardFile:
      json.dump(filecard, CardFile, indent=4, ensure_ascii=False)
################################################################################################################################
  def create_trap_card(name: str, SK: str,SP: int):
    with open(f"cards/traps.json", "r", encoding="utf-8") as file:
      filecard = list(json.load(file))
    card_dic_basic = {"name": name, "SP": SP,"skill":SK, "skill-description": ""}
    filecard.append(card_dic_basic)
    with open(f"cards/traps.json", "w", encoding="utf-8") as CardFile:
      json.dump(filecard, CardFile, indent=4, ensure_ascii=False)
################################################################################################################################
  def create_magic_card(name: str, SK: str,SP: int):
    with open(f"cards/magics.json", "r", encoding="utf-8") as file:
      filecard = list(json.load(file))
    card_dic_basic = {"name": name, "SP": SP,"skill":SK, "skill-description": ""}
    filecard.append(card_dic_basic)
    with open(f"cards/magics.json", "w", encoding="utf-8") as CardFile:
      json.dump(filecard, CardFile, indent=4, ensure_ascii=False)
################################################################################################################################
#
  def check_card(types, name):
    data_count = 0
    if types == "magics":
      with open (f"cards/{types}.json", "r", encoding="utf-8") as file:
        filecard = list(json.load(file))
      lone = len(filecard)
      for cards in filecard :
        if cards["name"] == name:
          return cards
        else:
          data_count += 1
      if data_count == lone:
        return False
    elif types == "monsters":
      with open (f"cards/{types}.json", "r", encoding="utf-8") as file:
        filecard = list(json.load(file))
      lone = len(filecard)
      for cards in filecard :
        if cards["name"] == name:
          return cards
        else:
          data_count += 1
      if data_count == lone:
        return False
    elif types == "traps":
      with open (f"cards/{types}.json", "r", encoding="utf-8") as file:
        filecard = list(json.load(file))
      lone = len(filecard)
      for cards in filecard :
        if cards["name"] == name:
          return cards
        else:
          data_count += 1
      if data_count == lone:
        return False
    else:
      return False   
################################################################################################################################
  def reback(user_name, user_id, command):
    print(
        f"{datetime.datetime.now()} used {command} by {user_name} {user_id}"
    )
    with open(path, "a", encoding="utf-8") as LogFile:
      LogFile.write(
          f"{datetime.datetime.now()} used {command} by {user_name} {user_id}\n"
      )

################################################################################################################################
  def datetime_translate(data:list):

    datetime_simple = datetime.datetime.now().strftime("%Y")
    data[1] = int(data[1])
    data[2] = int(data[2])
    if data[0] != None:
      if len(data[0]) == 4:
        if int(data[0]) < 1900:
          return "Year-error"
        else:
          data[0] = int(data[0])
      elif len(data[0]) == 2:
        if int(data[0]) > int(datetime_simple[2:]):
          data[0] = (int((datetime_simple)[0:2]) - 1)*100 + int(data[0])
        else:
          data[0] = int((datetime_simple)[0:2])      *100 + int(data[0])
      elif len(data[0]) == 1:
        data[0] = int((datetime_simple)[0:2])        *100 + int(data[0])
      elif len(data[0]) == 3:
        return "Year-error"
      elif data[2] > (calendar.monthrange(data[0],data[1]))[1]:
        return "date-error"
    else:
      pass
    if data[1] > 12:
      return "month-error"
    data[1] = int(data[1])
    data[2] = int(data[2])
    return data

################################################################################################################################
  def birth_set_date(name,id,guild_id,birthday):
    base_data = dict(load_birthday())
    base_data[f"{str(guild_id)}"][f"{id}"]={
        "discord-name":name,
        "birthday":[
          birthday[0],
          birthday[1],
          birthday[2]
        ],
        "celebrated":False
      } 
    updata_birthday(base_data)
################################################################################################################################
  def birth_set_channel(channel:discord.TextChannel):
    base_data = load_birthday()
    base_data[str(channel.guild.id)]["celebrate_channel"]=channel.id
    updata_birthday(base_data)
################################################################################################################################
  def add_food_in(food_name:str,food_tags:list):
    data = load_food()
    data["total"][food_name] = food_tags
    for tag in food_tags:
      if food_name not in data[tag]:
        data[tag].append(food_name)
    food_updata(data)
################################################################################################################################
  def load_food_tag():
    data = dict(load_food())
    List = list(data.keys())
    List.remove("total")
    return List
################################################################################################################################################################################################################################################################
class Card_Bettle_System():
  def start_game(duelist:DMember,competitor:DMember):
    print(f"{datetime.datetime.utcnow()} {duelist.name} and {competitor.name} start a match")
    create_game_match(duelist)
    match_info = {
      "members":[duelist.name,competitor.name],
      "time":datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S"),
      "Darea":[None,None,None,None,None],
      "Carea":[None,None,None,None,None],
      "drop_cards":[]
    }
    updata_match_info(duelist, match_info)
    pass
  pass