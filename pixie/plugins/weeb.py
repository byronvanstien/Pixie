# Third party libraries
from raitonoberu import Raitonoberu
from discord.ext import commands
from utils import setup_file, user_agent

from pyanimelist import PyAnimeList


class Weeb:
    """A set of commands for interacting with typical weeb things like MyAnimeList and NovelUpdates"""

    def __init__(self, bot):
        self.bot = bot
        # Our instance of pyanimelist, we pass a username and password here because it's needed for their (terrible) API
        # noinspection PyCallingNonCallable
        self.anime = PyAnimeList(username=setup_file["weeb"]["MAL"]["username"],
                                 password=setup_file["weeb"]["MAL"]["password"],
                                 user_agent=user_agent)
        # Our instance of Raitonoberu
        self.raitonoberu = Raitonoberu(user_agent=user_agent)

    @commands.command(name="novel")
    async def novel(self, novel_name: str):
        """
        Allows the user to search for a novels info from NovelUpdates.com using Raitonoberu (https://github.com/getrektbyme/raitonoberu)
        """
        n_data = await self.raitonoberu.get_first_search_result(novel_name)
        # Send a message with all the data we want
        await self.bot.say("Cover: {0.cover}\n"
                           "```xl\n"
                           "Title: {0.title}\n"
                           "Author: {1}\n"
                           "Genres: {2}\n"
                           "Language: {0.language}\n"
                           "Description: {0.description}\n"
                           "```"
                           "Link: <{0.link}>".format(n_data, ", ".join(x for x in n_data.authors),
                                                     ", ".join(x for x in n_data.genre)))

    @commands.group(pass_context=True, invoke_without_subcommand=True)
    async def mal(self, ctx):
        """
        A set of commands that allow the user to do different things with myanimelist
        """
        if ctx.invoked_subcommand is None:
            await self.bot.say("Invalid subcommand of MAL")

    @mal.command(name="anisearch")
    async def search_anime(self, *, anime_name: str):
        """
        Lets the user get data from an anime from myanimelist
        """
        x = (await self.anime.search_all_anime(anime_name))[0]
        await self.bot.say("MAL ID: {0}\n"
                           "Title: {1}\n"
                           "Episodes: {2}\n"
                           "Status: {3}\n"
                           "Synopsis: {4}\n"
                           "Cover: {5}\n".format(x.id, x.title, x.episodes,
                                                 x.status, x.synopsis, x.image))

    @mal.command(name="mangasearch")
    async def search_manga(self, *, manga_name: str):
        """
        Lets the user get data from a manga from myanimelist
        """
        manga = (await self.anime.search_all_manga(manga_name))[0]
        await self.bot.say("MAL ID: {0}\n"
                           "Title: {1}\n"
                           "Status: {2}\n"
                           "Synopsis: {3}\n"
                           "Type: {4}\n"
                           "Cover: {5}\n".format(manga.id, manga.title, manga.status,
                                                 manga.synopsis, manga.type, manga.image))


class NSFW:
    """
    A class for interacting with sites like Gelbooru
    """
    def __init__(self, bot):
        pass


def setup(bot):
    bot.add_cog(Weeb(bot))
    bot.add_cog(NSFW(bot))
