from core.classes import Cog_Extension
from discord.ext import commands
import json
from core.Def import custom_bot_command as CBC

reback = CBC.reback

class rpg(Cog_Extension):
    pass

async def setup(bot):
    await bot.add_cog(rpg(bot))