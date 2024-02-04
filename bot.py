import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('MTIwMjI0MTU1MDA1NTM5MTIzMg.GoU2OG.2KyNmSIhg_wF4h5rW9IBNVK__gs3XQ79O5-Z-8')