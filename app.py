import os
import asyncio
import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("I'm ready.")
    target_channel
    target_channel = bot.get_channel(636689612659490816)
    await target_channel.send("I'm ready.")
#bot.run(os.environ.get('BOT_TOKEN'))
bot.run('NjM2Njg5MTEzMjIyNzQyMDM3.XbDRfQ.k7Ysq2OZBbBnqs2yQTsg6QwTsRA')