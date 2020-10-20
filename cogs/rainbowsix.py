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

class RainbowSix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def r6s(self, ctx, acc: str):
        async with ctx.typing():
            search_url = 'https://r6.apitab.com/search/uplay/{}?cid=id'.format(acc)
            res = requests.get(search_url)
            data = res.json()
            player_id = next(iter(data["players"]))
            
            id_url = 'https://r6.apitab.com/player/{}?cid=id'.format(player_id)
            plr = requests.get(id_url)
            plrData = plr.json()
            Name = plrData['player']['p_name']
            level = plrData['stats']['level']
            GeneralKD = plrData['stats']['generalpvp_kd']
            Kills =plrData['stats']['generalpvp_kills']
            Deaths = plrData['stats']['generalpvp_death']
            Assists = plrData['stats']['generalpvp_killassists']
            WinRate = plrData['stats']['generalpvp_wl']
            Wins = plrData['stats']['generalpvp_matchwon']
            Losses = plrData['stats']['generalpvp_matchlost']
            HoursPlayed = plrData['stats']['generalpvp_hoursplayed']
            Headshots = plrData['stats']['generalpvp_headshot']
            HSAccuracy = plrData['stats']['generalpvp_hsrate']
            MeleeKills = plrData['stats']['generalpvp_meleekills']
            SeasonalRank = plrData['ranked']['rank']
            SeasonalChamp = plrData['ranked']['champ']

        embed = discord.Embed(name="R6 siege overall statistics", color=0x2718c9)
        embed.set_author(name="{}'s statistics".format(Name), icon_url= f"https://ubisoft-avatars.akamaized.net/{player_id}/default_146_146.png")
        embed.add_field(name="**General KD: **", value=GeneralKD)
        embed.add_field(name="**Kills: **", value=Kills)
        embed.add_field(name="**Deaths: **", value=Deaths)
        embed.add_field(name="**Assists: **", value=Assists)
        embed.add_field(name="**Wins: **", value=Wins)
        embed.add_field(name="**Losses: **", value=Losses)
        embed.add_field(name="**Win rate: **", value=WinRate)
        embed.add_field(name="**Headshots: **", value=Headshots)
        embed.add_field(name="**HS accuracy: **", value=HSAccuracy)
        embed.add_field(name="**Melee kills: **", value=MeleeKills)
        embed.add_field(name="**Level: **", value=level)
        embed.add_field(name="**Hours played: **", value=HoursPlayed)
        embed.set_thumbnail(url='https://tabstats.com/images/r6/ranks/?rank={}&champ={}'.format(SeasonalRank, SeasonalChamp))

        await ctx.send(embed=embed)

    @r6s.error
    async def r6s_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify an accout name")
        pass

    @commands.command(aliases=['r6scasual'])
    async def r6sCasual(self, ctx, acc: str):
        async with ctx.typing():
            search_url = 'https://r6.apitab.com/search/uplay/{}?cid=id'.format(acc)
            res = requests.get(search_url)
            data = res.json()
            player_id = next(iter(data["players"]))

            id_url = 'https://r6.apitab.com/player/{}?cid=id'.format(player_id)
            plr = requests.get(id_url)
            plrData = plr.json()
            Name = plrData['player']['p_name']
            CasualKills = plrData['stats']['casualpvp_kills']
            CasualDeaths = plrData['stats']['casualpvp_death']
            CasualKD = plrData['stats']['casualpvp_kd']
            CasualHours = plrData['stats']['casualpvp_hoursplayed']
            CasualWins = plrData['stats']['casualpvp_matchwon']
            CasualLosses = plrData['stats']['casualpvp_matchlost']
            CasualWR = plrData['stats']['casualpvp_wl']
            CasualMatches = plrData['stats']['casualpvp_matches']

        embed = discord.Embed(name="R6 overall casual statistics", color=0x2718c9)
        embed.set_author(name="{}'s casual statistics".format(Name), icon_url= f"https://ubisoft-avatars.akamaized.net/{player_id}/default_146_146.png")
        embed.add_field(name="**Kills: **", value=CasualKills)
        embed.add_field(name="**Deaths: **", value=CasualDeaths)
        embed.add_field(name="**Casual KD: **", value=CasualKD)
        embed.add_field(name="**Wins: **", value=CasualWins)
        embed.add_field(name="**Losses: **", value=CasualLosses)
        embed.add_field(name="**Casual win rate: **", value=CasualWR)
        embed.add_field(name="**Hours played: **", value=CasualHours)
        embed.add_field(name="**Matches played: **", value=CasualMatches)
        embed.set_thumbnail(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/05100836-b28d-4395-a29d-2f17b751c23f/dcenrbz-667b492e-2ff6-4433-8308-873fd3adba67.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMDUxMDA4MzYtYjI4ZC00Mzk1LWEyOWQtMmYxN2I3NTFjMjNmXC9kY2VucmJ6LTY2N2I0OTJlLTJmZjYtNDQzMy04MzA4LTg3M2ZkM2FkYmE2Ny5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.LN4YVqsXxE6G2y8OhDYLz4YFjkNifQINQZQEwwAZHCM')

        await ctx.send(embed=embed)

    @r6sCasual.error
    async def r6sCasual_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify an accout name")
        pass

    @commands.command(aliases = ['r6sthunt'])
    async def r6sTHunt(self, ctx, acc: str):
        async with ctx.typing():
            search_url = 'https://r6.apitab.com/search/uplay/{}?cid=id'.format(acc)
            res = requests.get(search_url)
            data = res.json()
            player_id = next(iter(data["players"]))

            id_url = 'https://r6.apitab.com/player/{}?cid=id'.format(player_id)
            plr = requests.get(id_url)
            plrData = plr.json()
            Name = plrData['player']['p_name']
            THKills = plrData['stats']['generalpve_kills']
            THDeaths = plrData['stats']['generalpve_death']
            THKD = plrData['stats']['generalpve_kd']
            THWins = plrData['stats']['generalpve_matchwon']
            THLosses = plrData['stats']['generalpve_matchlost']
            THWR = plrData['stats']['generalpve_wl']
            THHeadshots = plrData['stats']['generalpve_headshot']
            THHSAccuracy = plrData['stats']['generalpve_hsrate']
            THHours = plrData['stats']['generalpve_hoursplayed']

        embed = discord.Embed(name="R6 THunt siege statistics", color=0x2718c9)
        embed.set_author(name="{}'s overall THunt statistics".format(Name), icon_url= f"https://ubisoft-avatars.akamaized.net/{player_id}/default_146_146.png")
        embed.add_field(name="**Kills: **", value=THKills)
        embed.add_field(name="**Deaths: **", value=THDeaths)
        embed.add_field(name="**THunt KD: **", value=THKD)
        embed.add_field(name="**Wins: **", value=THWins)
        embed.add_field(name="**Losses: **", value=THLosses)
        embed.add_field(name="**THunt win rate: **", value=THWR)
        embed.add_field(name="**Headshots: **", value=THHeadshots)
        embed.add_field(name="**Headshot rate: **", value=THHSAccuracy)
        embed.add_field(name="**Hours played: **", value=THHours)
        embed.set_thumbnail(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/05100836-b28d-4395-a29d-2f17b751c23f/dcenrbz-667b492e-2ff6-4433-8308-873fd3adba67.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMDUxMDA4MzYtYjI4ZC00Mzk1LWEyOWQtMmYxN2I3NTFjMjNmXC9kY2VucmJ6LTY2N2I0OTJlLTJmZjYtNDQzMy04MzA4LTg3M2ZkM2FkYmE2Ny5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.LN4YVqsXxE6G2y8OhDYLz4YFjkNifQINQZQEwwAZHCM')

        await ctx.send(embed=embed)

    @r6sTHunt.error
    async def r6sTHunt_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify an accout name")
        pass

    @commands.command(aliases = ['r6sranked'])
    async def r6sRanked(self, ctx, acc: str):
        async with ctx.typing():
            search_url = 'https://r6.apitab.com/search/uplay/{}?cid=id'.format(acc)
            res = requests.get(search_url)
            data = res.json()
            player_id = next(iter(data["players"]))

            id_url = 'https://r6.apitab.com/player/{}?cid=id'.format(player_id)
            plr = requests.get(id_url)
            plrData = plr.json()
            Name = plrData['player']['p_name']
            RankedKills = plrData['stats']['rankedpvp_kills']
            RankedDeaths = plrData['stats']['rankedpvp_death']
            RankedKD = plrData['stats']['rankedpvp_kd']
            RankedWins = plrData['stats']['rankedpvp_matchwon']
            RankedLosses = plrData['stats']['rankedpvp_matchlost']
            RankedWR = plrData['stats']['rankedpvp_wl']
            RankedHours = plrData['stats']['rankedpvp_hoursplayed']
            RankedMatches = plrData['stats']['rankedpvp_matches']
            SeasonalRank = plrData['ranked']['rank']
            SeasonalChamp = plrData['ranked']['champ']
            SesRankedMMR = plrData['ranked']['mmr']

        embed = discord.Embed(name="R6 overall ranked statistics", color=0x2718c9)
        embed.set_author(name="{}'s ranked statistics".format(Name), icon_url= f"https://ubisoft-avatars.akamaized.net/{player_id}/default_146_146.png")
        embed.add_field(name="**Kills: **", value=RankedKills)
        embed.add_field(name="**Deaths: **", value=RankedDeaths)
        embed.add_field(name="**Ranked KD: **", value=RankedKD)
        embed.add_field(name="**Wins: **", value=RankedWins)
        embed.add_field(name="**Losses: **", value=RankedLosses)
        embed.add_field(name="**Ranked win rate: **", value=RankedWR)
        embed.add_field(name="**Hours played: **", value=RankedHours)
        embed.add_field(name="**Matches played: **", value=RankedMatches)
        embed.add_field(name="**Current MMR: **", value=SesRankedMMR)
        embed.set_thumbnail(url='https://tabstats.com/images/r6/ranks/?rank={}&champ={}'.format(SeasonalRank, SeasonalChamp))

        await ctx.send(embed=embed)

    @r6sRanked.error
    async def r6sRanked_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify an accout name")
        pass

    @commands.command(aliases = ['r6sseasonalranked', 'r6sSeRanked', 'r6sseranked'])
    async def r6sSeasonalRanked(self, ctx, acc: str):
        async with ctx.typing():
            search_url = 'https://r6.apitab.com/search/uplay/{}?cid=id'.format(acc)
            res = requests.get(search_url)
            data = res.json()
            player_id = next(iter(data["players"]))

            id_url = 'https://r6.apitab.com/player/{}?cid=id'.format(player_id)
            plr = requests.get(id_url)
            plrData = plr.json()
            Name = plrData['player']['p_name']
            SeasonalRank = plrData['ranked']['rank']
            SeasonalChamp = plrData['ranked']['champ']

            SesRankedKills = plrData['ranked']['allkills']
            SesRankedDeaths = plrData['ranked']['alldeaths']
            SesRankedKD = plrData['ranked']['allkd']
            SesRankedWin = plrData['ranked']['allwins']
            SesRankedLoss = plrData['ranked']['alllosses']
            SesRankedAbandons = plrData['ranked']['allabandons']
            SesRankedWR = plrData['ranked']['allwl']
            SesRankedKM = plrData['ranked']['killpermatch']
            SesRankedMatches = plrData['ranked']['allmatches']
            SesRankedMMR = plrData['ranked']['mmr']
            SesRankedMaxMMR = plrData['ranked']['maxmmr']
            SesRankedTopRegion = plrData['ranked']['topregion']
        
        embed = discord.Embed(name="R6 seasonal ranked statistics", color=0x2718c9)
        embed.set_author(name="{}'s seasonal ranked statistics".format(Name), icon_url= f"https://ubisoft-avatars.akamaized.net/{player_id}/default_146_146.png")
        embed.add_field(name="**Kills: **", value=SesRankedKills)
        embed.add_field(name="**Deaths: **", value=SesRankedDeaths)
        embed.add_field(name="**Seasonal KD: **", value=SesRankedKD)
        embed.add_field(name="**Wins: **", value=SesRankedWin)
        embed.add_field(name="**Losses: **", value=SesRankedLoss)
        embed.add_field(name="**Abandons: **", value=SesRankedAbandons)
        embed.add_field(name="**Kills per match: **", value=SesRankedKM)
        embed.add_field(name="**Seasonal win rate: **", value=SesRankedWR)
        embed.add_field(name="**Matches played: **", value=SesRankedMatches)
        embed.add_field(name="**MMR: **", value=SesRankedMMR)
        embed.add_field(name="**Max MMR: **", value=SesRankedMaxMMR)
        embed.add_field(name="**Top region: **", value=SesRankedTopRegion)
        embed.set_thumbnail(url='https://tabstats.com/images/r6/ranks/?rank={}&champ={}'.format(SeasonalRank, SeasonalChamp))
        
        await ctx.send(embed=embed)

    @r6sSeasonalRanked.error
    async def r6sSeasonalRanked_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify an accout name")
        pass

    @commands.command(aliases = ['r6savatar'])
    async def r6sAvatar(self, ctx, acc: str):
        async with ctx.typing():
            search_url = 'https://r6.apitab.com/search/uplay/{}?cid=id'.format(acc)
            res = requests.get(search_url)
            data = res.json()
            player_id = next(iter(data["players"]))

            id_url = 'https://r6.apitab.com/player/{}?cid=id'.format(player_id)
            plr = requests.get(id_url)
            plrData = plr.json()
            Name = plrData['player']['p_name']
        
        embed = discord.Embed(name="r6s avtar", color=0x2718c9)
        embed.set_author(name=f"{Name}'s avatar")
        embed.set_image(url=f"https://ubisoft-avatars.akamaized.net/{player_id}/default_256_256.png")
        await ctx.send(embed=embed)

    @r6sAvatar.error
    async def r6sAvatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify an accout name")
        pass


def setup(client):
    client.add_cog(RainbowSix(client))