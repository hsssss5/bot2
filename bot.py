import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('MTIwMjI0MTU1MDA1NTM5MTIzMg.G-ZXwL.r7Szcr9zetMzazeXaeIfILIY1ayxlfrGHXUIdI')