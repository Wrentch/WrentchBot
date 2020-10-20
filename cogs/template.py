import discord
from discord.ext import commands
from discord import User
import random

class Template(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx):
        flip = random.choice(["Head", "Tail"])
        embed = discord.Embed(name="FLIP", color=0x2718c9)
        embed.add_field(name="📀 Coin:", value= flip)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Template(client))