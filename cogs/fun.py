import discord
from discord.ext import commands
from discord import User
import random
import requests
from pprint import pprint
import json

class Template(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pun(self, ctx):
        pun = random.choice(['A horse is a very stable kind of animal.', 'Corduroy pillows make headlines.', 'Santa’s helpers are subordinate Clauses.', 'I can’t believe I got fired by the calendar factory. All I did was take a day off.', 'I’m glad I know sign language; it’s pretty handy.', 'Let’s talk about rights and lefts. You’re right, so I left.', 'Two fish are in a tank. One says to the other, “Err...so how do you drive this thing?”', 'I went to buy some camouflage trousers yesterday but couldnt find any.', 'Ive been to the dentist many times so I know the drill.', 'Being struck by lightning is a shocking experience!', 'Without geometry, life is pointless.', 'The roundest knight at King Arthur’s table was Sir Cumference. He acquired his size from far too much pi.', 'Im going to recolor this fabric, or dye trying!', 'Hair stylists are truly a braid a part.', 'The legalizing of marijuana in many states has been a big hit.', 'This year in the toy department, drones are a big hit. They are literally flying off the shelves.'])
        await ctx.send("**{}**".format(pun))

    @commands.command()
    async def roast(self, ctx):
        roast = random.choice(['My phone battery lasts longer than your relationships.', 'Too bad you can’t count jumping to conclusions and running your mouth as exercise. ', 'It’s a shame you can’t Photoshop your personality.', 'The smartest thing that ever came out of your mouth was a penis.', 'Calm down. Take a deep breath and then hold it for about twenty minutes.', 'Whoever told you to be yourself gave you really bad advice.', ' Where’s your off button?', 'If I had a face like yours I’d sue my parents.', 'I’m jealous of people who don’t know you.', 'Aww, it’s so cute when you try to talk about things you don’t understand.', 'I’m visualizing duck tape over your mouth.', 'Some people should use a glue stick instead of chapstick.', 'My hair straightener is hotter than you.', 'I’d smack you, but that would be animal abuse.', 'I’m not an astronomer but I am pretty sure the earth revolves around the sun and not you.', 'You’re the reason God created the middle finger.', 'You’re a grey sprinkle on a rainbow cupcake.', 'You have so many gaps in your teeth it looks like your tongue is in jail.', 'Your face makes onions cry.', 'You bring everyone so much joy, when you leave the room.', 'You are like a cloud. When you disappear it’s a beautiful day.', 'Don’t worry, the first 40 years of childhood are always the hardest.', 'I love what you’ve done with your hair. How do you get it to come out of your nostrils like that?', 'You are so full of shit, the toilet’s jealous.', 'If laughter is the best medicine, your face must be curing the world.'])
        await ctx.send("**{}**".format(roast))

    @commands.command()
    async def hugs(self, ctx, user: discord.Member):
        await ctx.send("{} is sending a big hug for {}".format(ctx.message.author.name, user.mention))
        await ctx.send("https://media1.tenor.com/images/b89ac07a1a3d3a34dbb52f1db69c6887/tenor.gif?itemid=3550852")

    @hugs.error
    async def hugs_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to tell me who are you sending a hug to")
        pass
    
    @commands.command(aliases = ['8ball'])
    async def eightball(self, ctx, *, question: str):
        ball = random.choice([ "Maybe", "Without a doubt", "Yes, definitely", "As I see it, yes", "Most likely", "Signs point to yes", "Ask again later", "Cannot predict now", "My reply is no", "My sources say no", "Very doubtful"])
        embed = discord.Embed(name="FLIP", color=0x2718c9)
        embed.set_author(name="Question:")
        embed.add_field(name= "**{}**".format(question), value= ball)
        await ctx.send(embed=embed)

    @eightball.error
    async def eightball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to ask me a question first")
        pass
    
    @commands.command()
    async def fact(self, ctx):
        fact_url = "https://uselessfacts.jsph.pl/random.json?language=en"
        res = requests.get(fact_url)
        data = res.json()
        fact = data['text']
        await ctx.send(f"***{fact}***")

    @commands.command()
    async def meme(self, ctx):
        async with ctx.typing():
            meme_url = 'https://api.ksoft.si/images/random-meme'

            r = requests.get(meme_url, headers={"Authorization": "id"})
            data = r.json()
            title = data['title']
            image_url = data['image_url']
            sorce = data['source']
            sub = data['subreddit']
            author = data['author']

        embed = discord.Embed(name="meme",description = f'[{title}]({sorce})', color=0x2718c9)
        embed.set_image(url=image_url)
        embed.set_footer(text=f'{sub} | {author}', icon_url= ctx.author.avatar_url )

        await ctx.send(embed=embed)

    @commands.command()
    async def aww(self, ctx):
        async with ctx.typing():
            meme_url = 'https://api.ksoft.si/images/random-aww'
            r = requests.get(meme_url, headers={"Authorization": "id"})
            data = r.json()
            title = data['title']
            image_url = data['image_url']
            sorce = data['source']
            sub = data['subreddit']
            author = data['author']

        embed = discord.Embed(name="aww",description = f'[{title}]({sorce})', color=0x2718c9)
        embed.set_image(url=image_url)
        embed.set_footer(text=f'{sub} | {author}', icon_url= ctx.author.avatar_url )

        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self,ctx):
        async with ctx.typing():
            cat_url = 'http://aws.random.cat/meow'
            req = requests.get(cat_url)
            data = req.json()

        embed = discord.Embed(title= 'Meow', color=0x2718c9)
        embed.set_image(url=data['file'])
        embed.set_footer(text='http://random.cat/', icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Template(client))