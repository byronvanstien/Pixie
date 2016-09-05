# Third party libraries
import discord
from discord.ext import commands


# This needs to be rewritten entirely lol
class Moderation:
    """Pixie's small set of moderation commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True, name="purge")
    async def purge(self, ctx, limit: int):
        """Allows someone with the correct permissions to delete mass amounts of messages"""
        try:
            await self.bot.purge_from(ctx.message.channel, limit=limit, before=ctx.message)
            await self.bot.say("```{0} messages deleted.```".format(limit))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `manage messages` permission")

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True, name="ban")
    async def ban_member(self, ctx, banned_for, days_to_delete: int = 1, *, reason: str):
        """Allows someone with the correct permissions to ban someone from the server"""
        try:
            await self.bot.ban(ctx.message.mentions[0], delete_message_days=days_to_delete)
            await self.bot.say('```{0} has been banned for {1}```'.format(banned_for, reason))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `ban` permission")

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True, name="kick")
    async def kick_member(self, ctx, kicked_for, *, reason: str):
        """Allows someone with the correct permissions to kick someone from the server"""
        try:
            await self.bot.kick(ctx.message.mentions[0])
            await self.bot.say("```{0} has been kicked for {1}```".format(kicked_for, reason))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `kick` permission")

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True, name="softban")
    async def soft_ban(self, ctx, softbanned_for, days_to_delete: int = 1, *, reason: str):
        """A kick with the added benefit of deleting messages"""
        try:
            await self.bot.ban(ctx.message.mentions[0], delete_message_days=days_to_delete)
            await self.bot.unban(ctx.message.server, ctx.message.mentions[0])
            await self.bot.say("```{0} has been softbanned for {1}```".format(softbanned_for, reason))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry I don't have the `ban` permission")


def setup(bot):
    bot.add_cog(Moderation(bot))
