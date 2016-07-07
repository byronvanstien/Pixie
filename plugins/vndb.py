from discord.ext import commands
import json
from Shosetsu import Shosetsu

with open('setup.json') as file:
    setup = json.load(file)


def is_owner(ctx):
    return ctx.message.author.id == setup['ownerid']


class VisualNovelDatabase:

    def __init__(self, bot):
        self.bot = bot
        self.vndb = Shosetsu()

    @commands.command(pass_context=True, description="Gives visual novel information", name="vndb", hidden=True)
    async def visual_novel_db_visual_novel_lookup(self, ctx, *, visualnovelname: str):
        info = await self.vndb.get_novel(visualnovelname)
        await self.bot.say('```Title: {}\nCover: {}\nLength: {}\nDevelopers: {}\nPublishers: {}```'.format(info['titles']['english'], info['img'], info['length'], ', '.join(info['developers']), ', '.join(info['publishers'])))



def setup(bot):
    bot.add_cog(VisualNovelDatabase(bot))
