from discord.ext import commands
import json

description = "A bot programmed by Recchan\n\nThis bot's main focus is to provide some useful utilities for use primarily by otakus. Enjoy!"

with open('setup.json') as file:
    setup = json.load(file)


def is_owner(ctx):
    return ctx.message.author.id == setup['ownerid']

bot = commands.Bot(command_prefix=[setup[
                   'prefix']], description=description, pm_help=True, help_attrs=dict(hidden=True))

initial_extensions = [
    'plugins.changer',
    'plugins.status',
    'plugins.moderation',
    'plugins.novelupdates',
    'plugins.vndb',
    'plugins.overwatch'
]


@commands.check(is_owner)
@bot.command(description="Allows me to evaluate code", name='eval', hidden=True)
async def eval_me(preeval: str):
    code = eval(preeval[5:])
    await bot.say("```" + code + "```")


@commands.check(is_owner)
@bot.command(description="Loads all the plugins at once", name="load", hidden=True)
async def load_all():
    for plugins in initial_extensions:
        bot.load_extension(plugins)
    await bot.say('```Plugins have been loaded.```')


@commands.check(is_owner)
@bot.command(description="Unloads all plugins at once", name="unload", hidden=True)
async def unload_all():
    for plugins in initial_extensions:
        bot.unload_extension(plugins)
    await bot.say("```Plugins have been unloaded.```")


@bot.event
async def on_ready():
    bot.connect()
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('https://discordapp.com/oauth2/authorize?client_id=175319652073734144&scope=bot&permissions=536083519')
    print('------')

bot.run(setup['token'])
