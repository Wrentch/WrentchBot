import discord
from discord.ext import commands
from discord import User
import random

class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['officalserver'])
    async def OfficalServer(self, ctx):
        embed = discord.Embed(name="OfficalServer", title = "⭐️Ofiical server link",  color=0x2718c9)
        embed.add_field(name="Offical server where Wrentch Bot is being developed", value= "👉[click me](https://discord.gg/9W4PPWm)👈")
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(name="invite", title = "🤖Add Wrentch Bot to your server",  color=0x2718c9)
        embed.add_field(name="Wrentch Bot invite link", value= "👉[click me](https://discord.com/api/oauth2/authorize?client_id=704072889342885938&permissions=8&scope=bot)👈")
        await ctx.send(embed=embed)

    @commands.command(aliases = ['developer', 'Developer'])
    async def dev(self, ctx):
        embed = discord.Embed(name="dev", title = "🛠 Wrentch Bot developer:",  color=0x2718c9)
        embed.add_field(name="Feel free to add me", value= "Wrentch#9294")
        await ctx.send(embed=embed)

    @commands.command(aliases = ['servers', 'Guilds'])
    async def guilds(self, ctx):
        g = len(self.client.guilds)
        embed = discord.Embed(name="guilds", title = "⛓ Servers:",  color=0x2718c9)
        embed.add_field(name = "***Wrentch Bot is currently serving:***", value= f"`{g} servers`")
        embed.add_field(name = "***With a total sum of:***", value= f"`{str(len(set(self.client.get_all_members())))} members`", inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = discord.Embed(name="join msg", title = f"Thanks for adding Wrentch Bot to {guild.name}",  color=0x2718c9)
                embed.add_field(name = "Keep in mind that this bot is still in heavy development and lots of features are coming in the future", value= "Wrentch bot is general multiuse discord bot 🧰 \n The default prefix is `;`. You can get the list of all commands with the command `help`. If you have any suggestions, problems or bug reports you can join the offical server (get the link with the `OfficalServer` command), or you can contact the main developer (command `dev`). \n If you want to add it to an another server use the command `invite`")
                embed.set_thumbnail(url= self.client.user.avatar_url)
                embed.set_footer(text = "Version: 1.5.0")
                await channel.send(embed=embed)
                break


def setup(client):
    client.add_cog(Bot(client))