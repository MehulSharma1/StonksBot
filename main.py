import os
from discord.ext import commands
import discord
import os
import random
from commands.greetings import Greetings

from commands.plot import Plot

from commands.summary import Summary


bot = commands.Bot(command_prefix="Stonk:")


@bot.event
async def on_ready():
    print("We have successfully logged in as {0.user}".format(bot))
    print(os.getcwd())


bot.add_cog(Greetings(bot))
bot.add_cog(Plot(bot))
bot.add_cog(Summary(bot))

bot.run(os.getenv("DISCORDAPIKEY"))
