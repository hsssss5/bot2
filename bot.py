import discord
from discord.ext import commands
from botToken import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
client = discord.Client(intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    #

bot.run(token)