# Third party libraries
import discord
from discord.ext import commands


class Info:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo", pass_context=True)
    async def user_info(self, ctx, user: discord.Member = None):
        """Gets information about the desired user"""
        if user is None:
            await self.bot.say("```xl\n"
                               "User: {0}\n"
                               "User Nickname: {0.nick}\n"
                               "User ID: {0.id}\n"
                               "User Avatar: {0.avatar_url}\n"
                               "User Created At: {0.created_at}\n"
                               "User Joined On: {0.joined_at}\n"
                               "Users Game: {0.game}\n"
                               "Users Roles: {1}\n"
                               "```".format(ctx.message.author, ", ".join([x.name for x in ctx.message.author.roles if x.name != "@everyone"])))
        else:
            await self.bot.say("```xl\n"
                               "User: {0}\n"
                               "User Nickname: {0.nick}\n"
                               "User ID: {0.id}\n"
                               "User Avatar: {0.avatar_url}\n"
                               "User Created At: {0.created_at}\n"
                               "User Joined On: {0.joined_at}\n"
                               "Users Game: {0.game}\n"
                               "Users Roles: {1}\n"
                               "```".format(user, ", ".join([x.name for x in user.roles if x.name != "@everyone"])))

    @commands.command(name="serverinfo", pass_context=True)
    async def server_info(self, ctx):
        """Gets information about the current server"""
        await self.bot.say("```xl\n"
                           "Server Name: {0}\n"
                           "Server ID: {0.id}\n"
                           "Server Region: {0.region}\n"
                           "Member Count: {1}\n"
                           "Server Owner: {0.owner}\n"
                           "Server Icon: {0.icon_url}\n"
                           "Server Roles: {2}"
                           "```".format(ctx.message.server, sum(1 for x in ctx.message.server.members),
                                        ", ".join([x.name for x in ctx.message.server.roles])))

    @commands.command(name="status")
    async def status(self):
        """Gives some general information about Pixie's current situation"""
        await self.bot.say("I'm currently on {0} servers\n"
                           "I can currently see {1} people, {2} of which are unique\n".format(len(self.bot.servers),
                                                                                              sum(1 for x in self.bot.get_all_members()),
                                                                                              sum(1 for x in (set(self.bot.get_all_members())))))


def setup(bot):
    bot.add_cog(Info(bot))
