# Pixie
* An open-source Discord bot built for Weebs by Weebs.
* Here's the [invite link](https://discordapp.com/oauth2/authorize?client_id=175319652073734144&scope=bot&permissions=536083519) in case you want to add Pixie to your server. (Although she's not currently hosted by me)

# Current Features
* Admin
  * namechange (Changes the bots name)
  * gamechange (Changes the bots game)
  * avatar (Changes the bots avatar)
  * debug (Allows the user to evaludate python code)
* Moderation
  * purge (Deletes large amounts of messages)
  * ban (Bans a user from a server)
  * kick (Kicks a user from a server)
* REPL
* Utility
  * lmgtfy (Let me google that for you)
  * novel (Searches a light novel and gets data from [Novel Updates](http://novelupdates.com) [using Raitonoberu](https://github.com/GetRektByMe/Raitonoberu))


# Planned Features
* Weeb Features
  * Anime
    * Integration with MyAnimelist
    * Integration with Hummingbird
    * Integration with Anilist
  * Manga
    * Coming soon!
* Let me google that for you
  * Have it set so you can choose if "I'm feeling lucky" is on
* Permission checks
* Prefixes set by individual server owners


# Information
* Pixie is built using Discord.py (see [here](https://github.com/Rapptz/discord.py))
* Some obvious information to state would be that Pixie is done using the Python programming language.
* Another important thing to let you all know is that Pixie is under an MIT license, meaning that you can do whatever with any code on this project, no questions asked.
* Something that I think is pretty cool information wise, Pixie is actually a reference to Mahouka Koukou no Rettousei.

# Setup

Before getting into how your setup file should look, lets get into where it should be placed (by default), unless you change where it originally was, it should be in the same directory as Pixie. You can change it if you want to, but you're going to have to also edit the code a little.

But, now we're through all the boring stuff - here's what you need to get it running.
```
{
  "ownerid": "Your discord ID",
  "prefix": "Whatever prefix you want to use",
  "token": "Your bot token"
  "osu_key": "Your Osu api key"
  "ani_list": "Your ani-list api key"
  "hummingbird": "Your hummingbird api key"
}
```
# Requirements
* Python 3.5+
* lxml
* Shosetsu
* aiohttp
