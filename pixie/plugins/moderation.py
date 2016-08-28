# Third party libraries
import discord
from discord.ext import commands


class Moderation:

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True, name="purge")
    async def purge(self, ctx, *, limit: int):
        """Allows someone with the correct permissions to delete mass amounts of messages"""
        try:
            await self.bot.purge_from(ctx.message.channel, limit=limit, before=ctx.message)
            await self.bot.say("```{} messages deleted.```".format(limit))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `manage messages` permission")

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True, name="ban")
    async def ban_member(self, ctx, banned_for, *, reason:  str):
        """Allows someone with the correct permissions to ban someone from the server"""
        try:
            await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
            await self.bot.say('```{} has been banned for {}```'.format(banned_for, reason))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `ban` permission")

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True, name="kick")
    async def kick_member(self, ctx, kicked_for, *, reason: str):
        """Allows someone with the correct permissions to kick someone from the server"""
        try:
            await self.bot.kick(ctx.message.mentions[0])
            await self.bot.say("```{} has been kicked for {}```".format(kicked_for, reason))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `kick` permission")


def setup(bot):
    bot.add_cog(Moderation(bot))
