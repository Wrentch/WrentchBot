import discord
from discord.ext import commands
from discord import User
from discord import Spotify
import random
import datetime
import io

d = datetime.date.today()

async def etb(emb):
    emb_str = "```md\n"
    emb_list = []
    if emb.author:
        emb_str += f"<{emb.author.name}>\n\n"
    if emb.title:
        emb_str += f"<{emb.title}>\n"
    if emb.description:
        if len(f"{emb_str}{emb.description}\n```")>2000:
            emb_str += "```"
            emb_list.append(emb_str)
            emb_str = "```md\n"
        emb_str += f"{emb.description}\n"
    if emb.fields:
        for field in emb.fields:
            if len(f"{emb_str}#{field.name}\n{field.value}\n```")>2000:
                emb_str += "```"
                emb_list.append(emb_str)
                emb_str = "```md\n"
            emb_str += f"#{field.name}\n{field.value}\n"
    if emb.footer:
        if len(f"{emb_str}\n{emb.footer.text}\n```")>2000:
            emb_str += "```"
            emb_list.append(emb_str)
            emb_str = "```md\n"
        emb_str += f"\n{emb.footer.text}\n"
    if emb.timestamp:
        if len("{}\n{}\n```".format(emb_str, str(emb.timestamp)))>2000:
            emb_str += "```"
            emb_list.append(emb_str)
            emb_str = "```md\n"
        emb_str += "\n{}".format(str(emb.timestamp))
    emb_str += "```"
    if emb_str != "```md\n```":
        emb_list.append(emb_str)
    return emb_list


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def date(self, ctx):
        embed = discord.Embed(name="Today's date", color=0x2718c9)
        embed.add_field(name="Today's date", value= d)
        await ctx.send(embed=embed)

    @commands.command(aliases=['userInfo'])
    async def userinfo(self, ctx, user: discord.Member):
        embed = discord.Embed(title="{}'s info".format(user.name), description="Users info.", color=0x2718c9)
        embed.add_field(name="NAME", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="STATUS", value=user.status, inline=True)
        embed.add_field(name="HIGHEST ROLE", value=user.top_role)
        embed.add_field(name="JOINED", value=user.joined_at)
        embed.add_field(name="IS BOT", value=user.bot)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to specify the user")
        if isinstance(error, commands.BadArgument):
            await ctx.send("Sorry, coulndn't find that user")
        pass

    @commands.command(aliases=['serverInfo'])
    async def serverinfo(self, ctx):
        embed = discord.Embed(name="{}'s info".format(ctx.message.guild.name), description="Servers info.", color=0x2718c9)
        embed.add_field(name="Name", value=ctx.message.guild.name, inline=True)
        embed.add_field(name="ID", value=ctx.message.guild.id, inline=True)
        embed.add_field(name="Members", value=len(ctx.message.guild.members))
        embed.add_field(name="Roles", value=len(ctx.message.guild.roles), inline=True)
        embed.add_field(name="Was created:", value=ctx.message.guild.created_at)
        embed.add_field(name="Region:", value=ctx.message.guild.region)
        embed.add_field(name="verification level:", value=ctx.message.guild.verification_level)
        embed.add_field(name="Nitro level:", value=ctx.message.guild.premium_tier)
        emoji_string = ""
        for e in ctx.message.guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
        if len(emoji_string) > 1023:
            emoji_string = "Error: too many emojies" 
        embed.add_field(name="Custom Emojies:", value=emoji_string or "No emojis available", inline=False)


        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['useravatar', 'userAvatar'])
    async def UserAvatar(self, ctx, user: discord.Member):
        embed = discord.Embed (name = "User avatar", color=0x2718c9)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @UserAvatar.error
    async def UserAvatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to specify the user")
        if isinstance(error, commands.BadArgument):
            await ctx.send("Sorry, coulndn't find that user")
        pass

    @commands.command()
    async def activity(self, ctx, user: discord.Member):
        embed = discord.Embed(name="Game", color=0x2718c9)
        embed.add_field(name="{}'s activity: ".format(user), value=user.activity)
        await ctx.send(embed=embed)

    @activity.error
    async def activity_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to specify the user")
        if isinstance(error, commands.BadArgument):
            await ctx.send("Sorry, coulndn't find that user")
        pass

    @commands.command(aliases = ['Spotify'])
    async def spotify(self, ctx, user: discord.Member=None):
        user = user or ctx.author
        spo = user.activities
        for activity in spo: 
            if isinstance(activity, Spotify):
                embed = discord.Embed(title="{}'s spotify info".format(user.name), color=0x1DB954)
                embed.add_field(name="***Song:***", value=f"{activity.title}", inline=False)
                embed.add_field(name="***Artist:***", value=f"{activity.artist}", inline=False)
                embed.add_field(name="***Album:***", value=f"{activity.album} \n 👉 [Open song in spotify](https://open.spotify.com/track/{activity.track_id}) 👈 ", inline=False)
                embed.set_thumbnail(url=activity.album_cover_url)
                await ctx.send(embed=embed)
                break
            
    @commands.guild_only()
    @commands.command()
    async def roles(self, ctx, *, member: discord.Member = None):
        if member is None:
            roles = ", ".join([role.name.strip('@') for role in ctx.guild.roles])
            await ctx.send(f"Roles for `{ctx.guild.name}`:")
            await ctx.send(f"```ini\n[{roles}]```") 
        else:
            roles = ", ".join([role.name.strip('@') for role in member.roles])
            await ctx.send(f"Roles for `{member.display_name}`:")
            await ctx.send(f"```ini\n[{roles}]```")
            
    @commands.command()
    async def bans(self, ctx):
        '''See a list of banned users in the guild'''
        try:
            bans = await ctx.guild.bans()
        except:
            return await ctx.send('You dont have the perms to see bans.')

        em = discord.Embed(title=f'List of Banned Members ({len(bans)}):', color=0x2718c9)
        em.description = ', '.join([str(b.user) for b in bans])

        await ctx.send(embed=em)

    @commands.command(aliases=['servericon'])
    async def serverlogo(self, ctx):
        embed = discord.Embed(title="{}'s logo".format(ctx.message.guild.name), color=0x2718c9)
        embed.set_image(url=ctx.message.guild.icon_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))