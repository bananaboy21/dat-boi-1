import discord
from discord.ext import commands
import aiohttp
import random

class Nsfw:
    '''
    xd
    '''
    def __init__(self, bot):
        self.bot = bot
        self.hentai = [
 'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'meow', 'tickle', 'lewd', 'feed', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'pussy_jpg', 'pwankg', 'classic', 'femdom', 'neko', 'cuddle', 'erok', 'fox_girl', 'boobs', 'Random_hentai_gif', 'smallboobs']


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def boobs(self, ctx):
        '''Get boobs off the internet'''
        if not ctx.channel.is_nsfw():
          await ctx.send("Why do you want to show NSFW in a non-nsfw channel? **hMMM?** :face_palm:")
          return
        """Random"""
        api_base = 'http://api.oboobs.ru/boobs/'
        number = random.randint(1, 10303)
        url_api = api_base + str(number)
        async with aiohttp.ClientSession() as session:
           async with session.get(url_api) as data:
                data = await data.json()
                data = data[0]
        image_url = 'http://media.oboobs.ru/' + data['preview']
        em = discord.Embed(color=0x11f95e)
        em.set_author(name="Boob Image")
        em.set_image(url=image_url)
        await ctx.send(embed=em)
        
        
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hentai(self, ctx):
        if not ctx.channel.nsfw:
            return await ctx.send("Honestly, do you want to kill people with hentai right now? :face_palm:")
        category = random.choice(self.hentai)
        async with self.bot.http._session.get(f"https://nekos.life/api/v2/img/{category}") as resp:
            data = await resp.json()
            em = discord.Embed()
            em.color = 0x11f95e
            em.set_image(url=data["url"])
            em.title = "Hentai"
            em.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=em)


def setup(bot): 
    bot.add_cog(Nsfw(bot)) 
