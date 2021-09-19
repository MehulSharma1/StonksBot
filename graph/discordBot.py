import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(os.getcwd())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Stonk'):
        await message.channel.send(file=discord.File('/home/elvis/StonksBot/images/fig1.png'))

client.run('ODg5MTIzNDg5OTMwNDMyNTMz.YUcqxw.ADyOgvyr-TRv9kJeMm89e39tmtQ')