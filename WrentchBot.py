import discord
from discord.ext import commands
from discord.ext.commands import Bot, Greedy
from discord import User
import random
import string
import datetime
import requests
from pprint import pprint
import io
import traceback
import sys
import math
import json
import os 


client = commands.Bot(command_prefix = ";")
client.remove_command('help')
version = "1.5.0"


@client.event
async def on_ready():
    print("bot loaded!")
    print(f"logged as {client.user.name}!")
    print(f"serving {str(len(set(client.get_all_members())))} users")
    await client.change_presence(activity=discord.Game(name=f';help| ;invite | Ver: {version}'))

@client.command()
async def RT(ctx, users: Greedy[User]):
    random.shuffle(users)
    for num, user in enumerate(users, start=0):
        if num < 5:
            await ctx.send("**🔷Team1:** {}".format(user.name, num))
        else:
            await ctx.send("**🔶Team2:** {}".format(user.name, num))  

#p_id = "eu38383b" #grabbed it from user input coz it's search
#data["players"][p_id][...]

extensions = ['cogs.template', 'cogs.help', 'cogs.info', 'cogs.rainbowsix', 'cogs.data', 'cogs.math', 'cogs.fun', 'cogs.text', 'cogs.utility', 'cogs.misc', 'cogs.bot', 'cogs.mod', 'cogs.games']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

client.run("TOKEN")