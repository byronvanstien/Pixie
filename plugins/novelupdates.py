from discord.ext import commands
from .raitonoberu import Raitonoberu

class NovelUpdates:

    def __init__(self, bot):
        self.bot = bot
        self.raitonoberu_instance = Raitonoberu()

    @commands.command(description="Novel lookup from NovelUpdates.", name="novel")
    async def novel_search(self, *, novelname: str):
        try:
            data = await self.raitonoberu_instance.page_info_parser(novelname)
            await self.bot.say('```Title: {}\nCover: {}\nGenres: {}\nNovel Status: {}\nLicensed: {}\nFully Translated: {}\nLink: {}```'.format(data['title'], None if data['cover'] == 'http://www.novelupdates.com/img/noimagefound.jpg' else data['cover'], ', '.join(data['genre']), data['novel_status'], data['licensed'], data['completely_translated'], data['link']))
        except:
            await self.bot.say('```Error: Contact the owner you pleb```')


def setup(bot):
    bot.add_cog(NovelUpdates(bot))
