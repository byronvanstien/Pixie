from discord.ext import commands
from .NovelAPI import NovelUpdatesAPI


class NovelUpdates:

    def __init__(self, bot):
        self.bot = bot
        self.raitonoberu = NovelUpdatesAPI()

    @commands.command(description="Novel lookup from NovelUpdates.", name="novel", hidden=True)
    async def novel_search(self, *, novelname: str):
        try:
            data = await self.raitonoberu.page_info_parser(novelname)
            await self.bot.say('```Title: {}\nCover: {}\nGenres: {}\nNovel Status: {}\nLicensed: {}\nFully Translated: {}\nLink: {}```'.format(data['title'], None if data['cover'] == 'http://www.novelupdates.com/img/noimagefound.jpg' else data['cover'], ', '.join(data['genre']), data['novel_status'], data['licensed'], data['completely_translated'], data['link']))
        except:
            await self.bot.say('```Error: Contact the owner you pleb```')


def setup(bot):
    bot.add_cog(NovelUpdates(bot))
