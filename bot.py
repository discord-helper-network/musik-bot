import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

bot.load_extension("cogs.music")


@bot.event
async def on_ready():
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('created by Discord Helper Network'),
                                     status=discord.Status.offline)
        await asyncio.sleep(10)




bot.run("TOKEN")
