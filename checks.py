import json

with open('setup.json') as file:
    setup_file = json.load(file)


def headers():
    return {'User-Agent': 'Pixie'}

def is_owner(ctx):
    return ctx.message.author.id == setup_file['ownerid']


def safe_roles(roles: list):
    names = []
    for role in roles:
        if role.name == "@everyone":
            names.append("@\u200beveryone")
        else:
            names.append(role.name)
    return names
