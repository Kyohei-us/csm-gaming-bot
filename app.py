import os
import asyncio
import discord
from discord.ext.commands import Bot
import datetime
import pytz

bot = Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("I'm ready.")
    #general channel
    target_channel = bot.get_channel(int(os.environ.get('GENERAL_CHANNEL')))
    await target_channel.send("I'm online.")

@bot.command(name='roleShift')
async def role(ctx):
    guild = ctx.message.guild

    for member in guild.members:
        for role in member.roles:
            role1 = discord.utils.get(guild.roles, id=622296223772180480)
            if role == role1:
                await member.remove_roles(role)
            role2 = discord.utils.get(guild.roles, id=622298746331332620)
            if role == role2:
                await member.remove_roles(role)
            role3 = discord.utils.get(guild.roles, id=622298861934739467)
            if role == role3:
                await member.remove_roles(role)
            # role_games = 
            # await member.add_roles()


# @bot.event
# async def on_message(message):
#     if message.content.lower() == 'hello':
#         channel = message.channel
#         await channel.send("Hello i'm a bot.")
#     await bot.process_commands(message)

# @bot.command(name='addrole')
# async def addrole(ctx):
#     guild = ctx.message.guild
#     role = discord.utils.get(guild.roles, name="admin")
#     try:
#         await ctx.message.author.add_roles(role)
#     except Exception as e:
#         print(e)
#         await ctx.message.channel.send("You failed to add role im sorry.")

# @bot.event
# async def on_member_join(member):
#     guild = member.guild
#     role = discord.utils.get(guild.roles, name="aggin")
#     try:
#         await member.add_roles(role)
#     except Exception as e:
#         print(e)
#         channel = bot.get_channel(636689612659490816)
#         await channel.send("You failed to add role im sorry.")
#     else:
#         channel = bot.get_channel(636689612659490816)
#         await channel.send("You get this role :  aggin")


@bot.event
async def on_message_delete(message):
    #log to logs channel
    channel = bot.get_channel(int(os.environ.get('LOGS_CHANNEL')))
    #fetching current time in PST
    now = datetime.datetime.utcnow()
    utc_time = pytz.utc.localize(now)
    timezone = utc_time.astimezone(pytz.timezone("America/Los_Angeles"))
    #formatting time
    timelog = timezone.strftime("%Y,%B,%d,%a,%X")
    await channel.send("{} : {} : {}".format(timelog, message.author.name, message.content))

bot.run(os.environ.get('BOT_TOKEN'))
