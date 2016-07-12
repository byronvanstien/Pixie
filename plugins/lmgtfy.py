from discord.ext import commands
import sys

sys.path.append('..')


class Lmgtfy:

    def __init__(self, bot):
        self.bot = bot
        self.baseurl = 'http://lmgtfy.com/'

    @commands.command(pass_context=True, description="Lets the user have the bot google for you", name="lmgtfy")
    async def lmgtfy(self, ctx, searchterm: str):
        await self.bot.say(self.baseurl + '?=' + searchterm)


def setup(bot):
    bot.add_cog(Lmgtfy(bot))
