from discord.ext import commands
from Shosetsu import Shosetsu

class VisualNovelDatabase:

    def __init__(self, bot):
        self.bot = bot
        self.vndb = Shosetsu()

    @commands.command(pass_context=True, description="Gives visual novel information", name="vndb")
    async def visual_novel_db_visual_novel_lookup(self, ctx, *, visualnovelname: str):
        info = await self.vndb.get_novel(visualnovelname)
        await self.bot.say('```Title: {}\nCover: {}\nLength: {}\nDevelopers: {}\nPublishers: {}```'.format(info['titles']['english'], info['img'], info['length'], ', '.join(info['developers']), ', '.join(info['publishers'])))



def setup(bot):
    bot.add_cog(VisualNovelDatabase(bot))
