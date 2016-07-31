from checks import is_owner
from discord.ext import commands


class Moderation:

    def __init__(self, bot):
        self.bot = bot

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows mass deletion of messages", name="purge")
    async def purge(self, ctx, *, limit: int):
        try:
            await self.bot.purge_from(ctx.message.channel, limit=limit, before=ctx.message)
            await self.bot.say("```{} messages deleted.```".format(limit))
        except Exception as e:
            await self.bot.say('```{}```'.format(e))

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows bans to be done through a bot", name="ban")
    async def ban_member(self, ctx, bannedfor, *, reason:  str):
        try:
            await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
            await self.bot.say('```{} has been banned for {}```'.format(bannedfor, reason))
        except Exception as e:
            await self.bot.say('```{}```'.format(e))

    @commands.check(is_owner)
    @commands.command(pass_context=True, description="Allows user to be kicked from server via bot command", name="kick")
    async def kick_member(self, ctx):
        try:
            await self.bot.kick(ctx.message.mentions[0])
        except Exception as e:
            await self.bot.say('```{}```'.format(e))


def setup(bot):
    bot.add_cog(Moderation(bot))
