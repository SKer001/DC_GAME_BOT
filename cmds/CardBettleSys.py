import discord
from core.classes import Cog_Extension
from discord.ext import commands
from discord import app_commands
import random
import json
from core.Def import reback

class CardBettleSys(Cog_Extension):
    pass
async def setup(bot):
    await bot.add_cog(CardBettleSys(bot))