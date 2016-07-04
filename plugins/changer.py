import discord
from discord.ext import commands

__author__ = 'GetRektByMe'
__version__ = '1.0'


def is_owner(ctx):
    return ctx.message.author.id == "163992386094104576"


class BotEdits:

    def __init__(self, bot):
        self.bot = bot

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows the name of the bot to be changed", name="namechange", hidden=True)
    async def name_change(self, ctx, *, name: str):
        await self.bot.edit_profile(password=None, username=name)
        await self.bot.say("```Bot name has been changed to: {}```".format(name))

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows the game the bot is playing to be changed", name="gamechange", hidden=True)
    async def game_change(self, ctx, *, game: str):
        await self.bot.change_status(discord.Game(name=game))
        await self.bot.say('```Game has now been changed to: {}```'.format(game))


def setup(bot):
    bot.add_cog(BotEdits(bot))
