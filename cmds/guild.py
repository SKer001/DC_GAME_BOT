from core.classes import Cog_Extension
from discord.ext import commands
import json
from core.Def import custom_bot_command as CBC 
reback = CBC.reback#(user_name,user_id,command)
class guild(Cog_Extension):
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        reback("the bot","000000000000000001","on_guild_join")
        guild_data = {}
        with open("guild_info.json","r",encoding="utf-8") as jfile:
            guild_data = json.load(jfile)
        guild_data[f"{guild.name}"] = [guild.id, guild.owner.name, guild.owner_id]
        with open("guild_info.json","w",encoding="utf-8") as jfile:
            json.dump(guild_data, jfile, indent=4,ensure_ascii=False)

    @commands.command()
    async def SetupGuild(self,ctx):
        reback(ctx.author.name,ctx.author.id,"SetupGuild")
        guild_data = {}
        with open("guild_info.json","r",encoding="utf-8") as jfile:
            guild_data = json.load(jfile)
        guild_data[f"{ctx.guild.name}"] = [ctx.guild.id,ctx.guild.owner.name, ctx.guild.owner_id]
        with open("guild_info.json","w",encoding="utf-8") as jfile:
            json.dump(guild_data, jfile, indent=4,ensure_ascii=False)
        await ctx.send(f"已經成功為伺服器[{ctx.guild.name}]創建好資料了喵!!")

async def setup(bot):
    await bot.add_cog(guild(bot))