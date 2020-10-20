import discord
from discord.ext import commands
from discord import User
import random

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['help'])
    async def _help(self, ctx):
        embed = discord.Embed(title="Help", color=0x2718c9)
        embed.set_author(name="Help categories")
        embed.add_field(name='`helpMod`', value='Moderation commands')
        embed.add_field(name='`helpFun`', value='Fun commands')
        embed.add_field(name='`helpInfo`', value='Information commands')
        embed.add_field(name='`helpData`', value='Data fetching commands')
        embed.add_field(name='`helpGames`', value='In chat games')
        embed.add_field(name='`helpGameStats`', value='Game stats')
        embed.add_field(name='`helpMani`', value='Photo and text manipulation')
        embed.add_field(name='`Settings`', value='Coming soon')
        embed.add_field(name='`helpBot`', value='Bot related commands')
        embed.add_field(name='`helpUtility`', value='Utility commands')
        embed.add_field(name='`helpMath`', value='Math commands')
        embed.add_field(name='`helpMisc`', value='Miscellaneous commands')
        embed.set_thumbnail(url='https://cdn4.iconfinder.com/data/icons/alphabet-3/500/Help_mark_query_question_support-512.png')
        embed.set_footer(text = "[] - required fields | <> - optional fields")
        await ctx.send(embed=embed)
        #await ctx.send('{}, check your DM'.format(author.mention))

    @commands.command(aliases=['helpdata'])
    async def helpData(self, ctx):
        embed = discord.Embed(title="Help Data", color=0x2718c9)
        embed.set_author(name="List of data commands")
        embed.add_field(name='lyrics [song]', value='Get lyrics of a song', inline=False)
        embed.add_field(name='weather [city]', value='Sends weather inforamtion about the specified city', inline=False)
        embed.add_field(name='COVID19', value='Sends updated COVID19 statistics', inline=False)
        embed.set_thumbnail(url='https://icons.iconarchive.com/icons/graphicloads/100-flat/256/home-icon.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['helpfun'])
    async def helpFun(self, ctx):
        embed = discord.Embed(title="Help Fun", color=0x2718c9)
        embed.set_author(name="List of commands for fun")
        embed.add_field(name='pun', value='Sends a random pun', inline=False)
        embed.add_field(name='roast', value='Sends a random roast', inline=False)
        embed.add_field(name='fact', value='Get a random useless fact', inline=False)
        embed.add_field(name='meme', value='Get a random meme', inline=False)
        embed.add_field(name='aww', value='Get random cute pictures, mostly animals', inline=False)
        embed.add_field(name='cat', value='Get random cat picture', inline=False)
        embed.add_field(name='hugs [@user]', value='Sends a virtual hug', inline=False)
        embed.add_field(name='8ball [message]', value='Sends a random answer to your questions', inline=False)
        embed.set_thumbnail(url='https://cdn.iconscout.com/icon/free/png-256/game-puzzle-fun-organization-seo-structure-6-17854.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['helpinfo'])
    async def helpInfo(self, ctx):
        embed = discord.Embed(title="Help Info", color=0x2718c9)
        embed.set_author(name="List of commands for getting information")
        embed.add_field(name='serverinfo', value='shows info about the server', inline=False)
        embed.add_field(name='serverlogo', value='Get the guild/server image in an embed', inline=False)
        embed.add_field(name='userinfo [@user]', value='shows info about the specified user', inline=False)
        embed.add_field(name='activity [@user]', value='Sends the users activity at the moment', inline=False)
        embed.add_field(name='UserAvatar [@user]', value='Sends a embeded image of a users avatar in higer scale', inline=False)
        embed.add_field(name='roles <@user>', value='Sends all the roles the user has. If none are specified it will show a list of every role in the server', inline=False)
        embed.add_field(name='bans', value='See a list of banned users in the server', inline=False)
        embed.add_field(name='date', value='Sends todays date', inline=False)
        embed.add_field(name="Spotify <@user>", value="Shows what the user is listening to, if you dont tag anyone it will show your spotify info")
        embed.set_thumbnail(url='https://icons.iconarchive.com/icons/graphicloads/100-flat/256/info-icon.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['helputility'])
    async def helpUtility(self, ctx):
        embed = discord.Embed(title="Help Utility", color=0x2718c9)
        embed.set_author(name="List of utility commands")
        embed.add_field(name='vote [message]', value='Sends a embeded message you specified then adds "✅" and "❌" as reactions for people to vote easily ', inline=False)
        embed.add_field(name='tinyurl [link]', value='Makes a link shorter using the tinyurl api', inline=False)
        embed.add_field(name='echo [message]', value='The bot repeats your specified message', inline=False)
        embed.add_field(name='Embedecho [message]', value='Same as echo but it puts it in an embed', inline=False)
        embed.add_field(name='Latency', value='Test the latency in ms', inline=False)
        embed.add_field(name='RT [@user] x 10', value='Random teams, tag 10 users and the bot will randomly shuffle them and create two teams.', inline=False)
        embed.set_thumbnail(url='https://icons.iconarchive.com/icons/ccard3dev/dynamic-yosemite/1024/Utilities-Activity-Monitor-icon.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['helpmath'])
    async def helpMath(self, ctx):
        embed = discord.Embed(title="Help Math", color=0x2718c9)
        embed.set_author(name="List of math commands")
        embed.add_field(name='sqrt [number]', value='Square root of the number', inline=False)
        embed.add_field(name='pi', value='First 300 digits of pi', inline=False)
        embed.add_field(name='log [number], [base]', value='log function', inline=False)
        embed.set_thumbnail(url='https://getdrawings.com/free-icon/calculator-icon-png-52.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['helpmisc'])
    async def helpMisc(self, ctx):
        embed = discord.Embed(title="Help Misc", color=0x2718c9)
        embed.set_author(name="List of Miscellaneous commands")
        embed.add_field(name='coinflip', value='bot flips a virtual coin', inline=False)
        embed.add_field(name='dice', value='Roll a virtual dice and get a random number between 1 and 6', inline=False)
        embed.add_field(name='RandomPass [lenght]', value='Generates a random password. You can specify the lenght, default is set to 16.', inline=False)
        embed.add_field(name='drama', value='returns popcorn emoji', inline=False)
        embed.add_field(name='id', value='Shows you how to get the User/Server/Message ID', inline=False)
        embed.add_field(name='length [message]', value='Get the length of the message', inline=False)
        embed.set_thumbnail(url='https://i.ya-webdesign.com/images/transparent-clipboard-flat-1.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['helpr6'])
    async def helpR6(self,ctx):
        embed = discord.Embed(title="Help R6", color=0x2718c9)
        embed.set_author(name="List of Rainbow Six Siege commands")
        embed.add_field(name='r6s [Accout name]', value='General player statistics', inline=False)
        embed.add_field(name='r6sCasual [Accout name]', value='General casual player statistics', inline=False)
        embed.add_field(name='r6sRanked [Accout name]', value='General ranked player statistics', inline=False)
        embed.add_field(name='r6sSeasonalRanked [Accout name]', value='Seasonal ranked player statistics', inline=False)
        embed.add_field(name='r6sTHunt [Accout name]', value='General THunt player statistics', inline=False)
        embed.add_field(name='r6sAvatar [Accout name]', value='Zoomed in profile picture', inline=False)
        embed.set_thumbnail(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/05100836-b28d-4395-a29d-2f17b751c23f/dcenrbz-667b492e-2ff6-4433-8308-873fd3adba67.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMDUxMDA4MzYtYjI4ZC00Mzk1LWEyOWQtMmYxN2I3NTFjMjNmXC9kY2VucmJ6LTY2N2I0OTJlLTJmZjYtNDQzMy04MzA4LTg3M2ZkM2FkYmE2Ny5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.LN4YVqsXxE6G2y8OhDYLz4YFjkNifQINQZQEwwAZHCM')
        await ctx.send(embed=embed)

    @commands.command(aliases = ['helpbot', 'helpbotinfo'])
    async def helpBot(self, ctx):
        embed = discord.Embed(title="Help Bot", color=0x2718c9)
        embed.set_author(name="List of bot info commands")
        embed.add_field(name='OfficalServer', value='If you have any suggestions, problems or bug reports feel free to ask here', inline=False)
        embed.add_field(name='dev', value='Developer of Wrentch Bot. If you have any suggestions, problems or bug reports feel free to add me', inline=False)
        embed.add_field(name='Guilds', value='Number of servers Wrentch Bot is in', inline=False)
        embed.add_field(name='invite', value='invite Wrentch Bot to your server')
        embed.set_thumbnail(url= self.client.user.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command(aliases = ['helpmod', 'helpModeration'])
    async def helpMod(self, ctx):
        embed = discord.Embed(title="Help Mod", color=0x2718c9)
        embed.set_author(name="List of moderation commands")
        embed.add_field(name='Kick [@user] <reason>', value='Kicks the user', inline=False)
        embed.add_field(name='Ban [@user] <reason>', value='Bans the user', inline=False)
        embed.add_field(name='Unban [name#tag] <reason>', value='Unbans the user', inline=False)
        embed.add_field(name='Softban [@user] <reason>', value='Kicks the user and deletes their messages', inline=False)
        embed.add_field(name='Hackban [id] <reason>', value='Bans a user that is currently not in the server. Only accepts user IDs. You can learn how to get the users id with the `id` command', inline=False)
        embed.add_field(name='Clear [number of messages]', value='Deletes the specified amount of messages. Limit per command is 150', inline=False)
        embed.add_field(name='nickname [user/s] [nickname]', value='Change someones nickname, can be used on multiple users', inline=False)
        embed.set_thumbnail(url="https://freeiconshop.com/wp-content/uploads/edd/wrench-flat.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=['helpgames', 'helpgame', 'helpGame'])
    async def helpGames(self, ctx):
        embed = discord.Embed(title="Help games", color=0x2718c9)
        embed.set_author(name="In chat games")
        embed.add_field(name='rps [rock/paper/scissors]', value='Play a game of rock paper scissors against the bot', inline=False)
        embed.add_field(name='minesweeper <columns> <rows> <bombs>', value='Generates a minesweeper field with spoiler tags based on user input or random.', inline=False)
        embed.set_thumbnail(url="https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/gamepad-icon.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=['helpgamestats', 'helpStats', 'helpstats'])
    async def helpGameStats(self, ctx):
        embed = discord.Embed(title="Help game stats", color=0x2718c9)
        embed.set_author(name="Game stats")
        embed.add_field(name='`helpR6` (category)', value='Rainbow six siege commands', inline=False)
        embed.set_thumbnail(url="https://icons.iconarchive.com/icons/martz90/hex/256/stats-icon.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=['helpmani', 'helpManipulation', 'helpmanipulation'])
    async def helpMani(self, ctx):
        embed = discord.Embed(title="Manipulation help", color=0x2718c9)
        embed.set_author(name="Photo and text manipulation")
        embed.add_field(name='mock [message]', value='Spongebob mocking meme', inline=False)
        embed.add_field(name='emojitext [message]', value='Turn normal text into emoji', inline=False)
        embed.set_thumbnail(url="https://freeiconshop.com/wp-content/uploads/edd/edit-flat.png")
        await ctx.send(embed=embed)

    @commands.command(aliases = ['settings'])
    async def Settings(self, ctx):
        await ctx.send("Comning soon")

def setup(client):
    client.add_cog(Help(client))