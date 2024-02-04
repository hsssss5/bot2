import discord
from discord.ext import commands
from botToken import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='+', case_insensitive=True, intents=intents)
client = discord.Client(intents=intents)

TOUROU = 209704345350963201

@bot.event
async def on_ready():
    channel = bot.get_channel(351452206077313027)
    if not channel:
        return
    await channel.send('i hate niggers')

@bot.command(aliases=['pong'])
async def ping(this):
    print('ping')
    await this.send('pong')

@bot.command()
async def pidor(this):
    await ping_user(this, TOUROU)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('test'):
        await message.channel.send('test')

    await bot.process_commands(message)

"""
@param this: контекст
@param user: id пользователя
"""
async def ping_user(this, user):
    await this.channel.send(f'<@{(user)}>')

bot.run(token)