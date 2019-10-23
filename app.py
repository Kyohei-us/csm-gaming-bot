import os
import asyncio
import discord
from discord.ext.commands import Bot
import datetime

bot = Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("I'm ready.")
    #general channel
    target_channel = bot.get_channel(636689612659490816)
    await target_channel.send("I'm ready.")

@bot.event
async def on_message(message):
    if message.content.lower() == 'hello':
        channel = message.channel
        await channel.send("Hello i'm a bot.")

@bot.event
async def on_message_delete(message):
    #log to logs channel
    channel = bot.get_channel(636700968762998784)
    timelog = datetime.datetime.now()
    await channel.send("{} : {} : {}".format(timelog, message.author.name, message.content))

bot.run(os.environ.get('BOT_TOKEN'))
