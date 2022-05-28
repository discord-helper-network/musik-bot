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


@bot.event
async def on_voice_state_update(member, before, after):

    if member.id == 234567890:
        await member.move_to(None)



bot.run("OTM4NDQyODg3NDg0NTU5Mzcw.YfqXCw.r9BlsG8thd9Jn8yDVmNOpTlIOcM")
