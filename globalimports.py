import json

with open('setup.json') as file:
    setup = json.load(file)

def is_owner(ctx):
    return ctx.message.author.id == setup['ownerid']