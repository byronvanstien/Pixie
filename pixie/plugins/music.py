# Standard library imports
import asyncio

import discord
from discord.ext import commands
from discord.opus import OpusNotLoaded
from utils import setup_file, user_agent


class WeebMusic:

    """WeebMusic is a class within Pixie's plugins that's dedicated to creating a
    stream from listen.moe and allowing the users to listen to music from the stream"""

    def __init__(self, bot):
        self.bot = bot
        # The dictionary that hold player objects
        self.players = {}
        # Default volume for WeebMusic
        self.default_vol = 100

    @commands.group(pass_context=True)
    async def music(self, ctx):
        """A set of commands to play music from listen.moe"""
        # If a subcommand isn't called
        if ctx.invoked_subcommand is None:
            self.bot.say("Sorry, that's not a valid subcommand of WeebMusic")

    @music.command(name="join", pass_context=True)
    async def join_vc_and_play_stream(self, ctx, *, channel: discord.Channel = None):
        """Has the bot join a voice channel and also starts the stream from listen.moe"""
        try:
            # Because the bot needs a channel to join, if it's None we'll just return the function assuming they're not in a voice channel
            if channel is None:
                # Set it to the voice channel for the member who triggers the command
                channel = ctx.message.author.voice.voice_channel
                # Check if again None (If the command user isn't in a voice channel)
                if channel is None:
                    # Tell the user they actually need to tell us what channel they want Pixie to join
                    await self.bot.say(
                        "```xl\nSorry, I'm not too sure what channel you want me to join unless you tell me!```")
                    # Exit out of the function so we don't try joining None
                    return
            # Get the VoiceClient object
            voice_client = await self.bot.join_voice_channel(channel)
            # Set it to stereo and set sample rate to 48000
            voice_client.encoder_options(sample_rate=48000, channels=2)
            # Set the user agent and create the player
            player = voice_client.create_ffmpeg_player("http://listen.moe:9999/stream", headers={"User-Agent": user_agent})
            # Set default player volume
            player.volume = self.default_vol / 100
            # Start the player
            player.start()
            # Be a tsun while telling the user that you joined the channel
            await self.bot.say("```xl\nI-I didn't join {0.channel} because you told me to... you b-b-baka! *hmph*```".format(voice_client))
            # Add to the dict of server ids linked to objects
            self.players.update({ctx.message.server.id: player})
        # Here we account for our bot not having enough perms or for the bot region being a bit dodgy
        except asyncio.TimeoutError:
            await self.bot.say("```xl\nSorry, I timed out trying to join!```")
        # This here pms the owner of the bot by the owner id in the setup file telling them if Opus isn't loaded
        except OpusNotLoaded:
            # Get the member object (here we assume the owner is in a server that the bot can see)
            member = discord.utils.get(self.bot.get_all_members(), id=setup_file["discord"]["owner_id"])
            # Send a message to tell the owner that the Opus isn't loaded
            await self.bot.send_message(member, "```xl\nOpus library not loaded.```")
        # Account for if the bot is in a channel on the server already
        except discord.ClientException:
            await self.bot.say("```xl\nSorry, I'm already in a voice channel on this server!```")

    @music.command(name="pause", pass_context=True)
    async def pause_audio_stream(self, ctx):
        """Pauses the music"""
        # Get the player object from the dict using the server id as a key
        player = self.players[ctx.message.server.id]
        # Pause the bot's stream
        player.pause()
        # Tell the user who executed the command that the bot's stream is paused
        await self.bot.say("```xl\nStream has been paused```")

    @music.command(name="resume", pass_context=True)
    async def resume_audio_stream(self, ctx):
        """Unpauses the music"""
        # Get the player object from the dict using the server id as a key
        player = self.players[ctx.message.server.id]
        # Resume the bots stream
        player.resume()
        # Tell the user who executed the command that the stream is resumed
        await self.bot.say("```xl\nStream has been resumed```")

    @music.command(name="volume", pass_context=True)
    async def change_volume(self, ctx, volume: int = 100):
        """Allows the user to change the volume of the bot"""
        # Get the player object from the dict using the server id as a key
        player = self.players[ctx.message.server.id]
        # We divide volume by 100 because for some reason discord works on 1.0 as 100%
        player.volume = volume / 100
        # Check if the player volume is above 200
        if (player.volume * 100) > 200:
            # Tell the user their input isn't allowed
            await self.bot.say("```xl\nSorry, the max input is 200```")
            # Return the function as we don't want to set the volume
            return
        # Tell the user what the current volume now is
        await self.bot.say("```py\nVolume has been changed to: {}```".format(str(volume)))

    @music.command(name="check_vol", pass_context=True)
    async def check_volume(self, ctx):
        """Checks the volume for the servers voice channel that it's in"""
        # Get the player object from the dict using the server id as a key
        player = self.players[ctx.message.server.id]
        # Have the bot say the volume
        await self.bot.say(player.volume * 100)

    @music.command(name="disconnect", pass_context=True)
    async def leave_vc(self, ctx):
        """Leaves the voice channel and stops the stream"""
        # Get the voice and player objects using the server id as a key
        voice = self.bot.voice_client_in(ctx.message.server)
        # Account for voice being None due to voice_client_in returning None if the bot isn't in a voice channel
        if voice is None:
            await self.bot.say("```xl\nSorry it doesn't seem like I'm in a voice channel in this server!```")
            return
        # Disconnect everything from the voice client object that the server is accessing
        await voice.disconnect()
        # Remove from the dictionaries since we no longer need to access this
        self.players.pop(ctx.message.server.id)


def setup(bot):
    bot.add_cog(WeebMusic(bot))
