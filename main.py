import discord
import psutil
from checks import setup_file, is_owner
from discord.ext import commands

bot = commands.Bot(command_prefix=[setup_file['prefix']],
                   description="A bot programmed by Recchan, main focus on features for weebs.", pm_help=False,
                   help_attrs=dict(hidden=True))

initial_extensions = [
    'plugins.admin',
    'plugins.utility',
    'plugins.moderation',
    'plugins.repl'
]


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


@bot.command(pass_context=True, description='Gets general information for the bot', name='status')
async def bot_status(ctx):
    ram = psutil.virtual_memory()
    ram_used_in_mb = ram.used >> 20
    ram_total_in_mb = ram.total >> 20
    ram_available_in_mb = ram.available >> 20
    await bot.say(
        "```xl\nServers Joined: {0}\nMessages Seen: {1}\nUnique Users: {2}\nRAM (TOTAL/USED/AVAILABLE): {4}/{3}/{5}```".format(
            len(ctx.bot.servers), len(ctx.bot.messages), len(set(bot.get_all_members())), ram_used_in_mb,
            ram_total_in_mb, ram_available_in_mb))


@bot.event
async def on_member_join(member):
    if member.server.id == '209121677148160000':
        role = discord.utils.get(member.server.roles, name="Member")
        await bot.add_roles(member, role)


@bot.event
async def on_ready():
    bot.connect()
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('https://discordapp.com/oauth2/authorize?client_id=175319652073734144&scope=bot&permissions=536083519')
    print('------')


bot.run(setup_file['token'])
