import sys
import urllib

from checks import safe_roles
from discord.ext import commands

from .raitonoberu import Raitonoberu

sys.path.append("..")


class Utility:
    def __init__(self, bot):
        self.bot = bot
        self.LMGTFY_BASE_URL = "http://lmgtfy.com/"
        self.raitonoberu_instance = Raitonoberu()

    @commands.command(pass_context=True, description="Lets the user have the bot google for you", name="lmgtfy")
    async def lmgtfy(self, ctx, searchterm: str):
        params = urllib.parse.urlencode({'q': searchterm})
        await self.bot.say('<' + self.LMGTFY_BASE_URL + '?' + params + '>')

    @commands.command(description="Novel lookup from NovelUpdates.", name="novel")
    async def novel_search(self, *, novelname: str):
        try:

            data = await self.raitonoberu_instance.page_info_parser(novelname)
            await self.bot.say(
                '```Title: {}\nCover: {}\nGenres: {}\nNovel Status: {}\nLicensed: {}\nFully Translated: {}\nLink: {}```'.format(
                    data['title'],
                    None if data['cover'] == 'http://www.novelupdates.com/img/noimagefound.jpg' else data['cover'],
                    ', '.join(data['genre']), data['novel_status'], data['licensed'], data['completely_translated'],
                    data['link']))
        except AttributeError as AE:
            await self.bot.say(AE)

    @commands.command(pass_context=True, description='Shows information for current server', name='serverinfo')
    async def server_info(self, ctx):
        await self.bot.say("```xl\nCurrent Server: {0.name}\nServer ID: {0.id}\nServer Owner: {0.owner}"
                           "\nMembers: {0.member_count}\nServer Region: {0.region}"
                           "\nServer Icon: {0.icon_url}\nChannels Count: {1}\n"
                           "Roles: {2}```".format(ctx.message.server, len(ctx.message.server.channels),
                                                  ', '.join(safe_roles(ctx.message.server.roles))))

    @commands.command(pass_context=True, description='Shows information for a user', name='userinfo')
    async def user_info(self, ctx, *, user=None):
        if user is None:
            await self.bot.say(
                "```xl\nNickname: {0.nick}\nUsername: {0.name}\nDiscriminator: {0.discriminator}\nUser ID: {0.id}"
                "\nAvatar: https://discordapp.com/api/users/{0.id}/avatars/{0.avatar}.jpg\nColour: {0.colour}"
                "\nHighest Role: {0.top_role} \nPlaying: {0.game}\nAccount created: {0.created_at}"
                "\nJoined on: {0.joined_at}""\nRoles: {1}```".format(ctx.message.author,
                                                                     ', '.join(
                                                                         safe_roles(ctx.message.author.roles))))
        else:
            return


def setup(bot):
    bot.add_cog(Utility(bot))
