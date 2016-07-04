# Pixie
An open-source Discord bot built for Weebs by Weebs.

# Current Features
* Weeb Features
  * Light Novels
    * Grabbing data from NovelUpdates using NovelAPI.
* Owner Restricted
  * Code Eval
  * Changing bot name
  * Changing bot game
* Moderation (Currently owner locked due to not have created any permission checks)
  * Purge
  * Ban
  * Kick


# Planned Features
* Weeb Features
  * Anime
    * Integration with MyAnimelist
    * Integration with Hummingbird
    * Integration with Anilist
  * Visual Novels
    * Being able to extract information from vndb
  * Manga
    * Coming soon!
* Overwatch
  * Ability to rip data and post stats

# Information
Pixie is built using Discord.py (see [here](https://github.com/Rapptz/discord.py))

Some obvious information to state would be that Pixie is done using the Python programming language.

Another important thing to let you all know is that Pixie is under an MIT license, meaning that you can do whatever with any code on this project, no questions asked.

# Setup

Before getting into how your setup file should look, lets get into where it should be placed (by default), unless you change where it originally was, it should be in the same directory as Pixie. You can change it if you want to, but you're going to have to also edit the code a little.

But, now we're through all the boring stuff - here's what you need to get it running.
```
{
  "ownerid": "Your discord ID",
  "prefix": "Whatever prefix you want to use",
  "token": "Your bot token"
}
```
# Requirements

Python 3.5+

lxml

Shosetsu

PrettyTable