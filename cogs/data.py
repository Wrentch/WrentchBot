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
from discord.ext.commands.errors import CommandInvokeError
from discord import HTTPException




class Data(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, *, city: str):
        weatherurl = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=key&units=metric'.format(city)
        res = requests.get(weatherurl)
        data = res.json()
        temp = data['main']['temp']
        windspeed = data['wind']['speed']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        desc = data['weather'][0]['description']
        if 'visibility' in data: 
            visibility = (data['visibility'])/1000
        else:
            visibility = ("Not avalible")
        country = data['sys']['country']
        co_lon = data['coord']['lon']
        co_lat = data['coord']['lat']

        embed = discord.Embed(name="Weather", color=0x2718c9)
        embed.set_author(name="🌤 Weather in {}: ".format(city))
        embed.add_field(name="**Temperature: **", value="{} °C".format(temp))
        embed.add_field(name="**Pressure: **", value="{} hpa".format(pressure))
        embed.add_field(name="**Humidity: **", value="{} %".format(humidity))
        embed.add_field(name="**Wind speed: **", value="{} m/s".format(windspeed))
        embed.add_field(name="**Min temperature: **", value="{} °C".format(temp_min))
        embed.add_field(name="**Max temperature: **", value="{} °C".format(temp_max))
        embed.add_field(name="**Cloudiness: **", value="{} ".format(desc))
        embed.add_field(name="**Visibility: **", value="{} km".format(visibility))
        embed.add_field(name="**Country: **", value="**{}**".format(country))
        embed.add_field(name="**Geo coords: **", value="{}, {} ".format(co_lat, co_lon))
        embed.set_thumbnail(url='https://i.dlpng.com/static/png/1768844-weather-targeting-weather-png-350_350_preview.webp')
        await ctx.send(embed=embed)

    @weather.error
    async def weather_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :You need to specify a place")
        pass

    @commands.command(aliases = ['covid19'])
    async def COVID19(self, ctx):
        c_url = ('https://corona.lmao.ninja/v2/all')
        res = requests.get(c_url)
        data = res.json()
        cases = data['cases']
        deaths = data['deaths']
        recovered = data['recovered']
        todayCases = data['todayCases']
        todayDeaths = data['todayDeaths']
        tests = data['tests']
        active = data['active']
        critical = data['critical']
        affectedCountries = data['affectedCountries']
        casesPerOneMillion = data['casesPerOneMillion']
        deathsPerOneMillion = data['deathsPerOneMillion']
        testsPerOneMillion = data['testsPerOneMillion']

        embed = discord.Embed(name="Corona statistics", color=0x2718c9)
        embed.set_author(name="COVID19 statistics")
        embed.add_field(name="**Cases: **", value=cases)
        embed.add_field(name="**Deaths: **", value=deaths)
        embed.add_field(name="**Recovered: **", value=recovered)
        embed.add_field(name="**Cases today: **", value=todayCases)
        embed.add_field(name="**Deaths today: **", value=todayDeaths)
        embed.add_field(name="**Tests: **", value=tests)
        embed.add_field(name="**Active: **", value=active)
        embed.add_field(name="**Critical: **", value=critical)
        embed.add_field(name="**Number of countries affected: **", value=affectedCountries)
        embed.add_field(name="**Cases per milion: **", value=casesPerOneMillion)
        embed.add_field(name="**Deaths per milion: **", value=deathsPerOneMillion)
        embed.add_field(name="**Tests per milion: **", value=testsPerOneMillion)
        embed.set_thumbnail(url='https://cdn3.iconfinder.com/data/icons/virus-transmission-flat/48/Virus_Corona-512.png')
        await ctx.send(embed=embed)

    @commands.command(aliases = ['lyric'])
    async def lyrics (self, ctx, *, name: str):
        async with ctx.typing():
            api_url = 'https://api.ksoft.si/lyrics/search'
            r = requests.get(api_url, headers={"Authorization": "key"}, params={'q': f"{name}", 'limit': 1})
            data = r.json()
            artist = data['data'][0]['artist']
            name = data['data'][0]['name']
            lyrics = data['data'][0]['lyrics']
            album_art = data ['data'][0]['album_art']
            lyrics_url = data['data'][0]['url']

        embed = discord.Embed(title= f'"{name}" by {artist}', color=0x2718c9)
        embed.set_thumbnail(url=f'{album_art}')
        embed.set_footer(text=f'{lyrics_url} | powerd by:  api.ksoft.si', icon_url= ctx.author.avatar_url)

        for l in lyrics.split('\n\n'): 
            
            embed.add_field(name= "\u200b" , value= l, inline=False)
        
        try:
            if len(embed) > 6000:
                await ctx.send(f'This songs has too many characters for a discord message, you can get the lyrics here: \n {lyrics_url}')
            else:
                await ctx.send(embed=embed)
        except (CommandInvokeError, HTTPException):
            await ctx.send(f'Looks like something went wrong, you can try to get the lyrics here: \n {lyrics_url}')
        
    @lyrics.error
    async def lyrics_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("`❌Error` :No input given")
        #if isinstance(error, commands.BadArgument):
            #await ctx.send("`❌Error` :Bad input given")
        #if isinstance(error, commands.CommandInvokeError):
            #await ctx.send(f'Looks like something went wrong, you can try whit an another song')
        
def setup(client):
    client.add_cog(Data(client))