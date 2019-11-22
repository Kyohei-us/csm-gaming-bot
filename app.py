import os
import asyncio
import discord
from discord.ext.commands import Bot
import datetime
import pytz

bot = Bot(command_prefix='-')


# @bot.event
# async def on_ready():
#     print("I'm ready.")
#     #general channel
#     target_channel = bot.get_channel(int(os.environ.get('GENERAL_CHANNEL')))
#     await target_channel.send("I'm online.")

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

@bot.command(name='roleAdjustment')
async def role(ctx):
    guild = ctx.message.guild
    channel = bot.get_channel(int(os.environ.get("GENERAL_CHANNEL")))#temp channel

    for member in guild.members:
        await channel.send('Starting role adjustment for {}'.format(member.name))
        role_group_games = discord.utils.get(guild.roles, id=622296223772180480)
        for role in member.roles:
            if role != role_group_games:
                await member.add_roles(role_group_games)
            if role == role_group_games:
                continue
            role_group_gaming_platform = discord.utils.get(guild.roles, id=622300532245266432)
            if role != role_group_gaming_platform:
                await member.add_roles(role_group_gaming_platform)
            if role == role_group_gaming_platform:
                continue
        await channel.send("{} finished his/her role adjustment.".format(member.name))

    for member in guild.members:
        for role in member.roles:
            # role_member = discord.utils.get(guild.roles, id=618656228280762390)
            # if role == role_member:
            #     await member.add_roles(role_member)
            role_group_games = discord.utils.get(guild.roles, id=622296223772180480)
            if role == role_group_games:
                await member.add_roles(role_group_games)
                role_group_gaming_platform = discord.utils.get(guild.roles, id=622300532245266432)
                if role == role_group_gaming_platform:
                    await member.add_roles(role_group_gaming_platform)
                    channel = bot.get_channel(int(os.environ.get("GENERAL_CHANNEL")))
                    await channel.send("{} finished his/her role adjustment.".format(member.name))

@bot.event
async def on_message(message):
    try:
        imageURL = message.attachments[0].url
    except Exception as e:
        print(e)
    else:
        channel = bot.get_channel(int(os.environ.get("IMAGE_REPOST_CHANNEL")))
        author = message.author
        try:
            attachmentID = message.attachments[0].id
        except Exception as e:
            print(e)
        else:
            await channel.send("{} : {} : {}".format(imageURL, author, attachmentID))
    await bot.process_commands(message)

# @bot.command(name='addrole')
# async def addrole(ctx):
#     guild = ctx.message.guild
#     role = discord.utils.get(guild.roles, name="admin")
#     try:
#         await ctx.message.author.add_roles(role)
#     except Exception as e:
#         print(e)
#         await ctx.message.channel.send("You failed to add role im sorry.")

@bot.event
async def on_member_join(member):
    guild = member.guild

    role_member = discord.utils.get(guild.roles, id=618656228280762390)
    role_group_games = discord.utils.get(guild.roles, id=622296223772180480)
    role_group_gaming_platform = discord.utils.get(guild.roles, id=622300532245266432)

    try:
        await member.add_roles(role_member)
    except Exception as e:
        print(e)
        channel = bot.get_channel(int(os.environ.get("GENERAL_CHANNEL")))
        await channel.send("{} failed to add role on join. I'm sorry.".format(member.name))
    else:
        channel = bot.get_channel(int(os.environ.get("GENERAL_CHANNEL")))
        await channel.send("{} get this role :  {}".format(member.name, role_member.name))
        
        try:
            await member.add_roles(role_group_games)
        except Exception as e:
            print(e)
            channel = bot.get_channel(int(os.environ.get("GENERAL_CHANNEL")))
            await channel.send("{} failed to add role on join. I'm sorry.".format(member.name))
        else:
            channel = bot.get_channel(int(os.environ.get("GENERAL_CHANNEL")))
            await channel.send("{} get this role :  {}".format(member.name, role_group_games.name))

            try:
                await member.add_roles(role_group_gaming_platform)
            except Exception as e:
                print(e)
                channel = bot.get_channel(int(os.environ.get("GENERAL_CHANNEL")))
                await channel.send("{} failed to add role on join. I'm sorry.".format(member.name))
            else:
                channel = bot.get_channel(int(os.environ.get("GENERAL_CHANNEL")))
                await channel.send("{} get this role :  {}".format(member.name, role_group_gaming_platform.name))





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

    name_of_channel_message_was_in = message.channel.name

    embed = discord.Embed(
        title=message.author.name,
        description=message.content,
        color=discord.Colour.gold()
    )
    embed.add_field(name="Time sent", value=timelog, inline=False)
    embed.add_field(name="Channel sent in", value=name_of_channel_message_was_in, inline=False)
    try:
        imageIdAttached = message.attachments[0].id
    except Exception as e:
        print(e)
    else:
        imageChannel = bot.get_channel(int(os.environ.get("IMAGE_REPOST_CHANNEL")))#image repost channel
        messages = await imageChannel.history(limit=1000).flatten()
        for a in messages:
            if str(imageIdAttached) in a.content:
                print("This is image id : \n{} and this is a.content : \n{}".format(imageIdAttached, a.content))
                try:
                    messageSplitBySpaceList = a.content.split(" ")
                except Exception as e:
                    print(e)
                else:
                    print("There will be an url of Image deleted below.")
                    embed.set_image(url=messageSplitBySpaceList[0])


    await channel.send(embed=embed)


    #await channel.send("{} : {} : {}".format(timelog, message.author.name, message.content))

bot.run(os.environ.get('BOT_TOKEN'))
