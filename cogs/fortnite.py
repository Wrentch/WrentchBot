import discord
from discord.ext import commands
from discord import User
import random
import requests

class Fortnite(commands.Cog):
    def __init__(self, client):
        self.client = client

#broken/work in progress

    @commands.command()
    async def fortnite (self, ctx):
        URL = "https://api.fortnitetracker.com/v1/profile/pc/Twitch_Svennoss"
        header = {'TRN-Api-key' : 'key'}
        r = requests.get(URL, headers=header)
        data = r.json()
        print(data)

        

def setup(client):
    client.add_cog(Fortnite(client))