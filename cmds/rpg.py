from core.classes import Cog_Extension
from discord.ext import commands
import json
from core.Def import reback

class rpg(Cog_Extension):
    pass

async def setup(bot):
    await bot.add_cog(rpg(bot))