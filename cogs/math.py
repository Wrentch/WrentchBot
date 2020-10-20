import discord
from discord.ext import commands
from discord import User
import random
import math

class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sqrt(self, ctx, num: float):
        embed = discord.Embed(name="Square root of {}".format(num), color=0x2718c9)
        sqrt = math.sqrt(num)
        embed.add_field(name="**Square root of {}: **".format(num), value=sqrt)
        await ctx.send(embed=embed)

    @sqrt.error
    async def sqrt_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Square root of what ?")
        pass

    @commands.command()
    async def log(self, ctx, num: int, *, base: int):
        log = math.log(num, base)
        embed = discord.Embed(name="Log", color=0x2718c9)
        embed.add_field(name="**Log function of {}, with the base {} is:**".format(num, base), value=log)
        await ctx.send(embed=embed)

    @log.error
    async def log_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Log of what ?")
        pass
        
    @commands.command()
    async def pi(self, ctx):
        embed = discord.Embed(name="Pi", color=0x2718c9)
        embed.set_author(name = "Pi")
        embed.add_field(name="**First 300 digits of pi**", value="3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1 1 1 7 4 5 0 2 8 4 1 0 2 7 0 1 9 3 8 5 2 1 1 0 5 5 5 9 6 4 4 6 2 2 9 4 8 9 5 4 9 3 0 3 8 1 9 6 4 4 2 8 8 1 0 9 7 5 6 6 5 9 3 3 4 4 6 1 2 8 4 7 5 6 4 8 2 3 3 7 8 6 7 8 3 1 6 5 2 7 1 2 0 1 9 0 9 1 4 5 6 4 8 5 6 6 9 2 3 4 6 0 3 4 8 6 1 0 4 5 4 3 2 6 6 4 8 2 1 3 3 9 3 6 0 7 2 6 0 2 4 9 1 4 1 2 7 3")
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Math(client))