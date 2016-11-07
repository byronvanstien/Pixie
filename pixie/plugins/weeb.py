from discord.ext import commands
from utils import setup_file, user_agent

from pyanimelist import PyAnimeList


class Weeb:
    """A set of commands for interacting with typical weeb things like MyAnimeList and NovelUpdates"""

    def __init__(self, bot):
        self.bot = bot
        # Our instance of pyanimelist, we pass a username and password here because it's needed for their (terrible) API
        self.pyanimelist = PyAnimeList(
                            username=setup_file["weeb"]["MAL"]["username"],
                            password=setup_file["weeb"]["MAL"]["password"],
                            user_agent=user_agent
                        )

    @commands.command(pass_context=True)
    async def anisearch(self, ctx, *, anime_name: str):
        # List of anime objects
        animes = await self.pyanimelist.search_all_anime(anime_name)
        # Put the first 10 in a dictionary with ints as keys
        animes_ = dict(enumerate(animes[:10]))
        # Add all the anime names there to let the user select
        message = "```What anime would you like:\n"
        for anime in animes_.items():
            message += "[{}] {}\n".format(str(anime[0]), anime[1].title)
        message += "\nUse the number to the side of the anime as a key to select it!```"
        await self.bot.send_message(ctx.message.channel, message)
        msg = await self.bot.wait_for_message(timeout=10.0, author=ctx.message.author)
        if msg:
            key = msg.content
            try:
                # Get the anime object the user wants
                requested_anime = animes_[int(key)]
            except (ValueError, KeyError):
                await self.bot.send_message(ctx.message.channel, "Invalid Key.")

            anime_data = "```\nID: {0.id}\n".format(requested_anime)
            anime_data += "Title: {0.title}\n".format(requested_anime)
            anime_data += "English Title: {0.english}\n".format(requested_anime)
            anime_data += "Episode Count: {0.episodes}\n".format(requested_anime)
            anime_data += "Type: {0.type}\n".format(requested_anime)
            anime_data += "Status: {0.status}\n\n".format(requested_anime)
            anime_data += "Synopsis: {0.synopsis}```".format(requested_anime)
            anime_data += "Image: {0.image}".format(requested_anime)

            await self.bot.send_message(ctx.message.channel, anime_data)
        else:
            return

    @commands.command(pass_context=True)
    async def mangasearch(self, ctx, *, manga_name: str):
        """
        Lets the user get data from a manga from myanimelist
        """
        mangas = await self.pyanimelist.search_all_manga(manga_name)
        mangas_ = dict(enumerate(mangas[:10]))
        message = "```What manga would you like:\n"
        for manga in mangas_.items():
            message += "[{}] {}\n".format(str(manga[0]), manga[1].title)
        message += "\nUse the number to the side of the manga as a key to select it!```"
        await self.bot.send_message(ctx.message.channel, message)
        msg = await self.bot.wait_for_message(timeout=10.0, author=ctx.message.author)
        if msg:
            key = msg.content
            try:
                requested_manga = mangas_[int(key)]
            except (ValueError, KeyError):
                await self.bot.send_message(ctx.message.channel, "Invalid key.")

            manga_data = "```\nID: {0.id}\n".format(requested_manga)
            manga_data += "Title: {0.title}\n".format(requested_manga)
            manga_data += "English Title: {0.english}\n".format(requested_manga)
            manga_data += "Volume Count: {0.volumes}\n".format(requested_manga)
            manga_data += "Type {0.type}\n".format(requested_manga)
            manga_data += "Status: {0.status}\n\n".format(requested_manga)
            manga_data += "Synopsis: {0.synopsis}```".format(requested_manga)
            manga_data += "Image: {0.image}".format(requested_manga)

            await self.bot.send_message(ctx.message.channel, manga_data)
        else:
            return


class NSFW:
    """
    A class for interacting with sites like Gelbooru
    """
    def __init__(self, bot):
        pass


def setup(bot):
    bot.add_cog(Weeb(bot))
    bot.add_cog(NSFW(bot))
