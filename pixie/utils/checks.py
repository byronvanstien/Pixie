# Standard library imports
import json

# Our setup file
with open('../../pixie/setup.json') as file:
    setup_file = json.load(file)

# Our user agent
user_agent = "Pixie (https://github.com/getrektbyme/pixie)"


# A function to use with checks to check for owner
def is_owner(ctx):
    return ctx.message.author.id == setup_file["discord"]['owner_id']


# Sanitises roles so when functions that print roles are used it doesn't ping @everyone
def safe_roles(roles: list):
    names = []
    for role in roles:
        if role.name == "@everyone":
            names.append("@\u200beveryone")  # \u200b is an invisible space
        else:
            names.append(role.name)
    return names
