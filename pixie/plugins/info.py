import discord
from discord.ext import commands


class Info:

    """Info is a class within Pixie that is only for accessing data from discords built in things (Although we add Pixie's status command here)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo", pass_context=True)
    async def user_info(self, ctx, user: discord.Member = None):
        """Gets information about the desired user (defaults to the message sender)"""
        if not user:
            user = ctx.message.author
        msg = "```\n"
        msg += "User: %s\n" % user.name
        msg += "Nickname %s\n" % user.nick
        msg += "ID: %s\n" % user.id
        msg += "Created at: %s\n" % user.created_at
        msg += "Joined on: %s\n" % user.joined_at
        msg += "Game: %s\n" % user.game
        msg += "Roles: %s\n" % ", ".join([role.name for role in user.roles if role.name != "@everyone"])
        msg += "```\n"
        msg += "Avatar: %s" % user.avatar_url
        await self.bot.send_message(ctx.message.channel, msg)

    @commands.command(name="guildinfo", pass_context=True)
    async def guild_info(self, ctx):
        """Gets information about the current server"""
        await self.bot.say("```xl\n"
                           "Guild: {0}\n"
                           "ID: {0.id}\n"
                           "Region: {0.region}\n"
                           "Member Count: {1}\n"
                           "Owner: {0.owner}\n"
                           "Icon: {0.icon_url}\n"
                           "Roles: {2}"
                           "```".format(ctx.message.server, sum(1 for x in ctx.message.server.members),
                                        ", ".join([x.name for x in ctx.message.server.roles])))

    @commands.command(name="status")
    async def status(self):
        """Gives some general information about Pixie's current situation"""
        await self.bot.say("```xl\n"
                           "I'm in {0} guilds\n"
                           "I can currently see {1} people, {2} of which are unique\n"
                           "I'm also in {3} voice channels"
                           "```".format(len(self.bot.servers),
                                        sum(1 for x in self.bot.get_all_members()),
                                        len(set(self.bot.get_all_members())),
                                        len(self.bot.voice_clients)))

    @commands.command(name="info")
    async def info(self):
        await self.bot.say("```xl\n"
                           "Hiya, I'm Pixie; I'm a bot built for weebs by Recchan.\n"
                           "Check me out on Github, where you can see my codebase: https://github.com/GetRektByMe/Pixie\n"
                           "Here's my invite link: https://discordapp.com/oauth2/authorize?client_id=175319652073734144&scope=bot&permissions=536083519```")


def setup(bot):
    bot.add_cog(Info(bot))
