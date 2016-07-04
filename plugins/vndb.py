from discord.ext import commands
from Shosetsu import Shosetsu


class VisualNovelDatabase:
    def __init__(self, bot):
        self.bot = bot
        self.vndb = Shosetsu()

    @commands.group(pass_context=True)
    async def vndb(self, ctx):
        self.bot.say('Test')

    @vndb.command(name="vn", pass_context=True)
    async def visual_novel_db_visual_novel_lookup(self, ctx, *, visualnovelname: str):
        try:
            firstnovel = await self.vndb.get_novel(visualnovelname)
            await self.bot.say('```Title: {}\nAliases: {}\nDevelopers: {}\nCover: {}\nLength: {}```'.format(firstnovel['Titles']['English'], firstnovel['Titles']['Aliases'], firstnovel['Developers'], firstnovel['Img'], firstnovel['Length']))
        except:
            await self.bot.say('```Check your spelling. Currently an issue selecting novels that do exist, if your name is correct, be aware this issue is being looked into.```')


def setup(bot):
    bot.add_cog(VisualNovelDatabase(bot))
