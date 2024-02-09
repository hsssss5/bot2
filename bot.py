import discord
import ffmpeg
import time
import random
import threading
from discord.ext import commands
from botToken import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="+", case_insensitive=True, intents=intents)
client = discord.Client(intents=intents)

TOUROU = 209704345350963201
Razzzir = 267744597126545408


@bot.event
async def on_ready():
    channel = bot.get_channel(351452206077313027)
    if not channel:
        return
    await channel.send("i hate niggers")


@bot.command(aliases=["pong"])
async def ping(this):
    print("ping")
    await this.send("pong")


@bot.command()
async def pidor(this):
    await ping_user(this, Razzzir)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("test"):
        await message.channel.send("test")

    await bot.process_commands(message)


threadStarted = False
client = discord.Client(intents=intents)


def play_ahaha():
    source = discord.FFmpegOpusAudio(
        source="ahaha.mp3", executable="F:/bot/anal/bin/ffmpeg.exe"
    )
    vClient.play(source)
    if vClient.is_connected():
        threading.Timer(random.randrange(30, 60), play_ahaha).start()


@bot.event
async def on_message(message):
    global threadStarted, vClient
    if message.content.startswith("1986") and threadStarted is False:
        threadStarted = True
        vChannel = message.author.voice.channel
        vClient = await vChannel.connect()
        vClient.stop()
        threading.Timer(random.randrange(30, 60), play_ahaha).start()


"""
@param this: контекст
@param user: id пользователя
"""


async def ping_user(this, user):
    await this.channel.send(f"<@{(user)}>")


bot.run(token)
