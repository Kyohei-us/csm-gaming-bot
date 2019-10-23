import os
import asyncio
import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("I'm ready.")
    global target_channel
    target_channel = bot.get_channel(636689612659490816)
    await target_channel.send("I'm ready.")

@bot.event
async def on_message(message):
    if message.content == 'hello':
        channel = message.channel
        channel.send("Hello i'm finally working")

bot.run(os.environ.get('BOT_TOKEN'))
