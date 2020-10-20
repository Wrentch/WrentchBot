import discord
from discord.ext import commands
from discord import User
import random

All_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def mockify(normalText):
    mockText = ''

    for index, letter in enumerate(normalText.lower(), start=0):
        if index % 2 == 0:
            mockText += letter
        else:
            mockText += letter.upper()
    return mockText

def emotext(normalText):
    emoText = ''

    for letter in normalText.lower():
        if letter in All_letters:
            emoText += letter.replace(letter, f':regional_indicator_{letter}: ' )
        else: 
            emoText += letter

    return emoText

class Text(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mock(self, ctx, *, message: str):
        await ctx.send("**{}**".format(mockify(message)))
        await ctx.send('https://imgflip.com/s/meme/Mocking-Spongebob.jpg')

    @mock.error
    async def mock_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to give me some text to mock")
        pass

    @commands.command(aliases = ['EmojiText'])
    async def emojitext(self, ctx, *, message: str):
        await ctx.send(emotext(message))

    @emojitext.error
    async def emojitext_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` : No input given")


def setup(client):
    client.add_cog(Text(client))