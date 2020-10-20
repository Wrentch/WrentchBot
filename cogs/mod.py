import discord
from discord.ext import commands
from discord import User
import random
from discord.ext.commands import Bot, Greedy


class BannedMember(commands.Converter):
    async def convert(self, ctx, argument):
        ban_list = await ctx.guild.bans()
        try:
            member_id = int(argument, base=10)
            entity = discord.utils.find(lambda u: u.user.id == member_id, ban_list)
        except ValueError:
            entity = discord.utils.find(lambda u: str(u.user) == argument, ban_list)

        if entity is None:
            raise commands.BadArgument("Not a valid previously-banned member.")
        return entity

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['Kick', 'k'])
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason = None):
        if user.top_role > ctx.author.top_role:
            await ctx.send("`❌Error` : You cant kick someone that has a role above your top role")
        else:
            await ctx.guild.kick(user, reason=reason)
            embed = discord.Embed(title=f"{user} was kicked by {ctx.author.name}", color=0x2718c9)
            embed.add_field(name="***Reason:***", value=reason)
            await ctx.send(embed=embed)

    @kick.error 
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("`❌Error` :You are missing `Kick Members` permission to run this command")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("`❌Error` :I dont have the permission to kick or the person you are trying to kick has a top role above mine")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify the user")

    @commands.command(aliases = ['Ban', 'b'])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason = None):
        if user.top_role > ctx.author.top_role:
            await ctx.send("`❌Error` : You cant ban someone that has a role above your top role")
        else:
            await ctx.guild.ban(user, reason=reason)
            embed = discord.Embed(title=f"{user} was banned by {ctx.author.name}", color=0x2718c9)
            embed.add_field(name="***Reason:***", value=reason)
            await ctx.send(embed=embed)

    @ban.error 
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("`❌Error` :You are missing `Ban Members` permission to run this command")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("`❌Error` :I dont have the permission to ban members or the person you are trying to kick has a top role above mine")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify the user")
        
    @commands.command(aliases = ['Softban'])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def softban(self, ctx, user: discord.Member, *, reason = None):
        if user.top_role > ctx.author.top_role:
            await ctx.send("`❌Error` : You cant softban someone that has a role above your top role")
        else:
            await ctx.guild.ban(user, reason=reason)
            await ctx.guild.unban(user, reason="softban")
            embed = discord.Embed(title=f"{user} was soft banned by {ctx.author.name}", color=0x2718c9)
            embed.add_field(name="***Reason:***", value=reason)
            await ctx.send(embed=embed)

    @softban.error 
    async def softban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("`❌Error` :You are missing `Ban Members` permission to run this command")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("`❌Error` :I dont have the permission to ban members or the person you are trying to kick has a top role above mine")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify the user")

    @commands.command(aliases = ['Hackban'])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def hackban(self, ctx, user_id: int, reason = None):
        try:
            await ctx.guild.ban(user = discord.Object(id=user_id), reason=reason)
            embed = discord.Embed(title=f"The id you specified was banned, {ctx.author.name}", color=0x2718c9)
            embed.add_field(name="***Reason:***", value=reason)
            await ctx.send(embed=embed)
        except:
            await ctx.send("`❌Error` :Could not find user")

    @hackban.error 
    async def hackban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("`❌Error` :You are missing `Ban Members` permission to run this command")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("`❌Error` :I dont have the permission to ban members ")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify an id")

    @commands.command(aliases = ['Unban'])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, user: BannedMember, *, reason=None):
        await ctx.guild.unban(user.user, reason=reason)
        embed = discord.Embed(title=f"{user.user.name} was unbanned by {ctx.author.name}", color=0x2718c9)
        embed.add_field(name="***Reason:***", value=reason)
        await ctx.send(embed=embed)

    @unban.error 
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("`❌Error` :You are missing `Ban Members` permission to run this command")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("`❌Error` : Sorry, an error ")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify the user")

    @commands.command(aliases = ['purge', 'clean', 'Clear'])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx, messages: int):
        if messages > 149:
            messages = 149
        await ctx.channel.purge(limit=messages + 1)
        embed = discord.Embed(title = f"🗑 {ctx.author} deleted `{messages}` messages", color=0x2718c9)
        await ctx.send(embed=embed, delete_after=5)

    @clear.error 
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("`❌Error` :You are missing `manage messages` permission to run this command")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify an amout of messages to delete")

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, users: Greedy[discord.Member] = None, *, nick: str,):
        if users== None:
            await ctx.send("`❌Error` :You didnt spefic the user(s)")
        for user in users:
            await user.edit(nick=nick)
        await ctx.send("Changed nickname(s)")

    @nickname.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("`❌Error` :You are missing `manage_nicknames` permission to run this command")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("`❌Error` : Sorry, an error has occurred")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You didnt spefic the nickname")    


def setup(client):
    client.add_cog(Mod(client))