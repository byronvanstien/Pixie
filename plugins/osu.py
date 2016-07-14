import aiohttp
from discord.ext import commands
import json
import sys
import urllib

# Opens files from one level up in the directory
sys.path.append('..')

with open('setup.json') as file:
    osu = json.load(file)

class Osu:
    def __init__(self, bot):
        self.bot = bot
        self.__osu_key = osu['osu_key']

    @commands.command(pass_context=True, description="Displays information from Osu!", name="osu")
    async def user_info(self, *, username: str):
        pass

def setup(bot):
    bot.add_cog(Osu(bot))
