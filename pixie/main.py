# Standard library imports
import logging
import sys

# Third party libraries
import discord
from discord.ext import commands
from discord.ext.commands import Bot, when_mentioned_or
import logbook
from logbook import Logger, StreamHandler
from logbook.compat import redirect_logging
from utils import setup_file, user_agent

# List of initial plugins to start up with (Loaded in Pixie.run())
plugins = ["plugins.weeb", "plugins.owner", "plugins.info", "plugins.moderation", "plugins.music"]


class Pixie(Bot):

    def __init__(self, *args, **kwargs):
        # Call super, get our command prefix and set our description
        super().__init__(command_prefix=when_mentioned_or(setup_file["discord"]["command_prefix"]),
                         description="A bot for weebs programmed by Recchan")

        # Set a custom user agent for Pixie
        self.http.user_agent = user_agent

        # Logging setup
        redirect_logging()
        StreamHandler(sys.stderr).push_application()
        self.logger = Logger("Pixie")
        self.logger.level = getattr(logbook, setup_file.get("log_level", "INFO"), logbook.INFO)
        logging.root.setLevel(self.logger.level)

    # Prints out the user we're logged into as
    async def on_ready(self):
        self.logger.info("Logged in as Bot Name: {0.user.name} Bot ID: {0.user.id}".format(self))

    # Exit if the command isn't found, so our console isn't spammed
    # Tell the user that they can't run the command if they don't pass the checks
    async def on_command_error(self, exception, ctx):
        print(exception)  # Remove once I've finished debugging Pixie
        if isinstance(exception, commands.errors.CommandNotFound):
            return
        if isinstance(exception, commands.errors.CheckFailure):
            await self.send_message(ctx.message.channel, "You don't have the required permissions to run this command.")

    async def on_member_join(self, member):
        # Auto roles people in the Mahouka (Onii-sama) server with the role "Member"
        if member.server.id == '209121677148160000':
            await bot.say("Hey {0.name}, welcome to {0.server.name}".format(member))
            role = discord.utils.get(member.server.roles, name="Member")
            await bot.add_roles(member, role)

    async def on_voice_state_update(self, before, after):
        # If nothing changes just exit out of the function
        if before.voice.voice_channel == after.voice.voice_channel:
            return
        # Exit on channel being None as it errors if Pixie isn't in a voice channel
        if not after.server.me.voice_channel:
            return
        # Checks the length of the list of members in the voice channel
        if len(after.server.me.voice.voice_channel.voice_members) == 1:
            # Get the VoiceClient object
            voice = self.voice_client_in(after.server)
            # Disconnect the VoiceClient and close the stream
            await voice.disconnect()
            await self.send_message(after.server.default_channel,
                                    "```\nSorry! Since no one was using me I left :c you can have me re-join easily though!```")

    def run(self):
        # We load plugins in run rather than on_ready due to on_ready being able to be called multiple times
        for plugin in plugins:
            # We try to load the extension, and we account for if it fails
            try:
                self.load_extension(plugin)
                self.logger.info("{0} has been loaded".format(plugin))
            # Except discord.ClientException so it doesn't fail to load all cogs when a cog doesn't have a setup function
            except discord.ClientException:
                self.logger.critical("{0} does not have a setup function!".format(plugin))
            # Except import error (importlib raises this) so bot doesn't crash when it's raised
            except ImportError as IE:
                self.logger.critical(IE)
        # We check if discord.opus is loaded, despite it not having a reason to be
        if not discord.opus.is_loaded():
            # Load discord.opus so we can use voice
            discord.opus.load_opus()
            self.logger.info("Opus has been loaded")
        super().run(setup_file["discord"]["token"])


# Actually start up the bot
if __name__ == "__main__":
    bot = Pixie()
    bot.run()
