from datetime import datetime
from discord.ext import commands
from prettytable import PrettyTable

class Status:

    def __init__(self, bot):
        self.bot = bot
        self.uptime = datetime.now()
        self.gametable = PrettyTable()

    @commands.command(pass_context=True, description="Shows current status of bot", name="status")
    async def status(self, ctx):
        timeonline = datetime.now() - self.uptime
        self.gametable.add_row(
            ['Current Server', '{}'.format(ctx.message.server)])
        self.gametable.add_row(['Uptime', "{}".format(timeonline)])
        await self.bot.say("```{}```".format(self.gametable))


def setup(bot):
    bot.add_cog(Status(bot))
