from discord.ext import commands
from datetime import datetime, timedelta
import json
import psutil

description = "A bot programmed by Recchan\n\nThis bot's main focus is to be a bot for weebs, by weebs. Enjoy!"

with open('setup.json') as file:
    setup = json.load(file)


def is_owner(ctx):
    return ctx.message.author.id == setup['ownerid']


bot = commands.Bot(command_prefix=[setup[
                                       'prefix']], description=description, pm_help=False, help_attrs=dict(hidden=True))

initial_extensions = [
    'plugins.changer',
    'plugins.moderation',
    'plugins.novelupdates',
    'plugins.vndb',
    'plugins.overwatch',
    'plugins.lmgtfy',
    'plugins.osu'
]


def safe_roles(roles: list):
    names = []
    for role in roles:
        if role.name == "@everyone":
            names.append("@\u200beveryone")
        else:
            names.append(role.name)

    return names


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


@bot.command(pass_context=True, description='Shows information for current server', name='serverinfo')
async def server_info(ctx):
    await bot.say("```xl\nCurrent Server: {0.name}\nServer ID: {0.id}\nServer Owner: {0.owner}"
                  "\nMembers: {0.member_count}\nServer Region: {0.region}"
                  "\nServer Icon: {0.icon_url}\nChannels Count: {1}\n"
                  "Roles: {2}```".format(ctx.message.server, len(ctx.message.server.channels),
                                         ', '.join(safe_roles(ctx.message.server.roles))))


@bot.command(pass_context=True, description='Shows information for a user', name='userinfo')
async def user_info(ctx, *, user=None):
    await bot.say("```xl\nNickname: {0.nick}\nUsername: {0.name}\nDiscriminator: {0.discriminator}\nUser ID: {0.id}"
                  "\nAvatar: https://discordapp.com/api/users/{0.id}/avatars/{0.avatar}.jpg\nColour: {0.colour}"
                  "\nHighest Role: {0.top_role} \nPlaying: {0.game}\nAccount created: {0.created_at}"
                  "\nJoined on: {0.joined_at}""\nRoles: {1}```".format(ctx.message.author,
                                                                       ', '.join(safe_roles(ctx.message.author.roles))))


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
async def on_ready():
    bot.connect()
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('https://discordapp.com/oauth2/authorize?client_id=175319652073734144&scope=bot&permissions=536083519')
    print('------')


bot.run(setup['token'])
