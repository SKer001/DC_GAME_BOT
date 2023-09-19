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

class Cards(app_commands.Group):
##################################################################

    @app_commands.command(name="test",description="test")
    async def test(self, interaction:DInteracion):
        pass

    @app_commands.command(name="test2",description="test2")
    async def test2(self, interaction:DInteracion):
        pass

    testing = app_commands.Group(name="testing",description="testing")

    @testing.command(name="test3",description="test3")
    async def test3(self, interaction:DInteracion):
        pass

async def setup(bot):
    bot.tree.add_command(Cards(name="card",description="test"))