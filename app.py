import os
import asyncio
import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("I'm ready.")
    target_channel
    target_channel = bot.get_channel(635916613320835099)
    await target_channel.send("I'm ready.")

bot.run(os.environ.get('BOT_TOKEN'))
