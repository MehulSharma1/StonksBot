import discord
import os
from discord.ext import commands
import random

client = discord.Client()
bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    print(os.getcwd())


@bot.command(name="99")
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "I'm the human form of the 💯 emoji.",
        "Bingpot!",
        (
            "Cool. Cool cool cool cool cool cool cool, "
            "no doubt no doubt no doubt no doubt."
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name="test")
async def foo(ctx, arg):
    await ctx.send(arg)


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Stonk"):
        await message.channel.send(
            file=discord.File("/home/elvis/StonksBot/images/fig1.png")
        )
    await bot.process_commands(message)


bot.run(os.getenv("DISCORDAPIKEY"))
