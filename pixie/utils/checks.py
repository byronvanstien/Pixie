from . import setup_file


def is_owner(ctx):
    return ctx.message.author.id == setup_file["discord"]['owner_id']


def pixie_admin(ctx):
    if is_owner(ctx):
        return True
    return ctx.message.author.id in setup_file["discord"]["pixie_admins"]


def server_owner(ctx):
    if is_owner(ctx):
        return True
    if pixie_admin(ctx):
        return True
    return ctx.message.author == ctx.message.server.owner


def server_admin(ctx):
    if is_owner(ctx):
        return True
    if pixie_admin(ctx):
        return True
    if server_owner(ctx):
        return True
    return ctx.message.author.server_permissions.administrator


def server_moderator(ctx):
    if is_owner(ctx):
        return True
    if pixie_admin(ctx):
        return True
    if server_owner(ctx):
        return True
    if server_admin(ctx):
        return True
    return "pixie" in [role.name.lower() for role in ctx.message.author.roles]
