# Standard library imports
import json

# Our setup file
with open('../setup.json') as file:
    setup_file = json.load(file)

# Our user agent
user_agent = "Pixie (https://github.com/GetRektByMe/Pixie)"


# A function to use with checks to check for owner
def is_owner(ctx):
    return ctx.message.author.id == setup_file["discord"]['owner_id']
