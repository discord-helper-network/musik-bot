import discord
import asyncio
from discord.ext import commands
import json

with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    


bot = commands.Bot(command_prefix='!')

bot.load_extension("cogs.music")


@bot.event
async def on_ready():
    
    print('██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗')
    print('██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝')
    print('██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝ ')
    print('██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝  ')
    print('██║  ██║███████╗██║  ██║██████╔╝   ██║   ')
    print('╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ')

    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('created by Discord Helper Network'),
                                     status=discord.Status.offline)
        await asyncio.sleep(10)




bot.run(token)
