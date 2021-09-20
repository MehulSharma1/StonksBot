from typing import List
from discord.ext import commands
import discord
import yfinance as yf
import plotly.graph_objects as go
import random
import os


def generate_graph(symbol, period="5d", interval="1h"):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="5d", interval="1h")
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df.index,
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
            )
        ]
    )
    fig.update_xaxes(
        rangeslider_visible=True,
        rangebreaks=[
            # NOTE: Below values are bound (not single values), ie. hide x to y
            dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
            dict(bounds=[16, 9.5], pattern="hour"),  # hide hours outside of 9.30am-4pm
            # dict(values=["2020-12-25", "2021-01-01"])  # hide holidays (Christmas and New Year's, etc)
        ],
    )
    fig.update_layout(
        title="Stock Analysis",
        yaxis_title=f"{symbol} Stock",
        xaxis_rangeslider_visible=False,
    )
    return fig
    # hist = ticker.history(period="5d", interval="1h")


class Plot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def plot(self, ctx, args, member: discord.Member = None):

        args = args.split()
        symbol = args[0]
        if len(args) == 1:
            fig = generate_graph(symbol)
            print(type(fig))
            image_path = f"./temp/temp{str(random.randint(0,9999999))}.png"
            fig.write_image(image_path)
            await ctx.send(file=discord.File(image_path))
            os.remove(image_path)
            return

        # hist = ticker.history(period="5d", interval="1h")
        await ctx.send("Invalid number of args ".format(member))
