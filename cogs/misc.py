import discord
from discord.ext import commands
from discord import User
import random
import string
from random import randint

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def drama(self, ctx):
        await ctx.send(":popcorn: :popcorn: :popcorn:")

    @commands.command(aliases = ['randompass', 'Password', 'randompassword'])
    async def RandomPass(self, ctx, lenght: int = 16):
        res = ''.join(random.choices(string.ascii_lowercase + string.digits, k = lenght))
        embed = discord.Embed(name="Randomly generated", color=0x2718c9)
        embed.add_field(name="**Randomly generated password: **", value=str((res)))
        await ctx.send(embed=embed)

    @commands.command(aliases=['?id'])
    async def id(self, ctx):
        embed = discord.Embed(title="Where can I find my User/Server/Message ID?", description="🔭[click me](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)", color=0x2718c9)
        await ctx.send(embed=embed)

    @commands.command()
    async def dice(self, ctx, number=6):
        embed = discord.Embed(name="Dice",title ="🎲 You rolled a __**{}**__!".format(randint(1, number)),  color=0x2718c9)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['len', 'length'])
    async def _length(self, ctx, *, string: str = ''):
        """ Find length of string."""
        await ctx.send('Message length:``' + str(len(str(string))) + '``')

def setup(client):
    client.add_cog(Misc(client))