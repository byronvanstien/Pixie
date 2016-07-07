from datetime import datetime
from discord.ext import commands
import json
from prettytable import PrettyTable

with open('setup.json') as file:
    setup = json.load(file)


def is_owner(ctx):
    return ctx.message.author.id == setup['ownerid']


class Status:

    def __init__(self, bot):
        self.bot = bot
        self.uptime = datetime.now()
        self.gametable = PrettyTable()

    @commands.command(pass_context=True, description="Shows current status of bot", name="status", hidden=True)
    async def status(self, ctx):
        timeonline = datetime.now() - self.uptime
        self.gametable.add_row(
            ['Current Server', '{}'.format(ctx.message.server)])
        self.gametable.add_row(['Uptime', "{}".format(timeonline)])
        await self.bot.say("```{}```".format(self.gametable))


def setup(bot):
    bot.add_cog(Status(bot))
