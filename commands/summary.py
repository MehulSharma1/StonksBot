from discord.ext import commands
import discord
import yfinance 


class Summary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def summary(self, ctx, stockSymbol):
        await ctx.send('Please wait while we load the data for you!')
        stockTicker = yfinance.Ticker(stockSymbol);
        await ctx.send(stockTicker.get_info())