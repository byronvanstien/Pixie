import discord
from discord.ext import commands

from utils.checks import (
    is_owner,
    pixie_admin,
    server_owner,
    server_admin,
    server_moderator
)


# This needs to be rewritten entirely lol
class Moderation:
    """Pixie's small set of moderation commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.check(server_moderator)
    @commands.command(pass_context=True, name="purge")
    async def purge(self, ctx, limit: int):
        try:
            await self.bot.purge_from(ctx.message.channel, limit=limit, before=ctx.message)
            await self.bot.say("```{0} messages deleted.```".format(limit))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `manage messages` permission")

    @commands.check(server_moderator)
    @commands.command(pass_context=True, name="ban")
    async def ban_member(self, ctx, banned_for, days_to_delete: int = 1, *, reason: str):
        try:
            await self.bot.ban(ctx.message.mentions[0], delete_message_days=days_to_delete)
            await self.bot.say('```{0} has been banned for {1}```'.format(banned_for, reason))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `ban` permission")

    @commands.check(server_moderator)
    @commands.command(pass_context=True, name="kick")
    async def kick_member(self, ctx, kicked_for, *, reason: str):
        try:
            await self.bot.kick(ctx.message.mentions[0])
            await self.bot.say("```{0} has been kicked for {1}```".format(kicked_for, reason))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry, I don't have the `kick` permission")

    @commands.check(server_moderator)
    @commands.command(pass_context=True, name="softban")
    async def soft_ban(self, ctx, softbanned_for, days_to_delete: int = 1, *, reason: str):
        try:
            await self.bot.ban(ctx.message.mentions[0], delete_message_days=days_to_delete)
            await self.bot.unban(ctx.message.server, ctx.message.mentions[0])
            await self.bot.say("```{0} has been softbanned for {1}```".format(softbanned_for, reason))
        except discord.errors.Forbidden:
            await self.bot.say("Sorry I don't have the `ban` permission")


def setup(bot):
    bot.add_cog(Moderation(bot))
