from discord.ext import commands
import sys

sys.path.append(',,')

def is_owner(ctx):
    with open('setup.json') as file:
        setup = json.load(file)
        return ctx.message.author.id == setup['ownerid']


class BotEdits:

    def __init__(self, bot):
        self.bot = bot

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows the name of the bot to be changed", name="namechange")
    async def name_change(self, ctx, *, name: str):
        await self.bot.edit_profile(password=None, username=name)
        await self.bot.say("```Bot name has been changed to: {}```".format(name))

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows the game the bot is playing to be changed", name="gamechange")
    async def game_change(self, ctx, *, game: str):
        await self.bot.change_status(discord.Game(name=game))
        await self.bot.say('```Game has now been changed to: {}```'.format(game))


def setup(bot):
    bot.add_cog(BotEdits(bot))
