import inspect

import discord
from checks import is_owner
from discord.ext import commands


class Admin:
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

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Change avatar of the bot", name="avatar")
    async def avatar(self, ctx, image: str):
        with open("{}.jpeg".format(image), 'rb') as image:
            image = image.read()
            await self.bot.edit_profile(avatar=image)

    @commands.check(is_owner)
    @commands.command(pass_context=True, hidden=True)
    async def debug(self, ctx, *, code: str):
        """Evaluates code."""
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.server,
            'channel': ctx.message.channel,
            'author': ctx.message.author
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await self.bot.say(python.format(type(e).__name__ + ': ' + str(e)))
            return

        await self.bot.say(python.format(result))


def setup(bot):
    bot.add_cog(Admin(bot))