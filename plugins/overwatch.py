from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup


class OverWatch:

    def __init__(self, bot):
        self.bot = bot
        self.battletag = None
        self.platform = None
        self.region = None
        self.searchfor = None
        self.baseurl = 'https://owapi.net/v1/u/'

    @commands.group(pass_context=True)
    async def overwatch(self, ctx):
        if ctx.invoked_subcommand is None:
            self.bot.say('Invalid command.')

    @commands.command()
    async def stats(self, *, username: str):
        with aiohttp.ClientSession() as session:
            async with session.get(self.baseurl + username + '/stats') as response:
                parse = BeautifulSoup(await response.json(), 'lxml')
                await self.bot.say(parse)

        # except:
            # await self.bot.say('```Error, names are case sensitive. Try
            # again.```')


def setup(bot):
    bot.add_cog(OverWatch(bot))
