import discord
from discord.ext import commands
from discord import User
import random
import requests
from pprint import pprint
import json

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vote(self, ctx, *, votequestion: str):
        embed = discord.Embed(name="vote", color=0x2718c9)
        embed.add_field(name="**Vote question: **", value=votequestion)
        embed.set_footer(text= f"{ctx.author}")
        votemsg = await ctx.send(embed=embed)
        await votemsg.add_reaction("✅")
        await votemsg.add_reaction("❌")

    @vote.error
    async def vote_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to give me some text")
        pass

    @commands.command()
    async def echo(self, ctx, *, message: str):
        await ctx.send(f"{ctx.author} : {message}")

    @commands.command()
    async def latency(self, ctx):
        await ctx.send(f"**Latency: ** {round(self.client.latency * 1000)}ms")

    @commands.command(aliases = ['EmbedEcho', 'Embedecho'])
    async def embedecho (self, ctx, *, message: str = ''):
        embed = discord.Embed(name="Embed echo",description = f'{message}', color=0x2718c9)
        embed.set_author(name=f'{ctx.author}:')
        await ctx.send(embed=embed)

    @commands.command(aliases = ['TinyUrl', 'shorturl', ])
    async def tinyurl(self, ctx, *, link: str):
        #await ctx.message.delete()
        tiny_url = f'http://tinyurl.com/api-create.php?url={link}'
        #async with self.client.session.get(url) as resp:
            #new = await resp.text()
        res = requests.get(tiny_url) 
        new = res.text
        emb = discord.Embed(color=0x2718c9)
        emb.add_field(name="Original Link", value=link, inline=False)
        emb.add_field(name="Shortened Link", value=new, inline=False)
        emb.set_footer(text='Powered by tinyurl.com', icon_url='http://cr-api.com/static/img/branding/cr-api-logo.png')
        await ctx.send(embed=emb)

    @tinyurl.error
    async def tinyurl_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :No link given")

def setup(client):
    client.add_cog(Utility(client))