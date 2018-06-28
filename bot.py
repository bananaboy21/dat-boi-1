import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import random
import textwrap
import inspect
from contextlib import redirect_stdout
from discord.ext import commands
import json
import idioticapi
import youtube_dl
bot = commands.Bot(command_prefix=commands.when_mentioned_or('+'), description="A bot made by L3NNY#4519\n\nHelp Commands", owner_id=411683912729755649)
bot.remove_command("help")
bot._last_result = None
bot.load_extension("cogs.Usefull")
bot.load_extension("cogs.help")
bot.load_extension("cogs.Mod")
bot.load_extension("cogs.Math")
bot.load_extension("cogs.Idiotic")
bot.load_extension("cogs.Nsfw")
bot.load_extension("cogs.Fortnite")
bot.load_extension("cogs.Economy")
bot.load_extension("cogs.Holidays")
bot.load_extension("cogs.Music")
bot.load_extension("cogs.Info")
bot.load_extension("cogs.Devs")


def cleanup_code(content):
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    while True:
        await bot.change_presence(activity=discord.Game(name=f"+help"), status='dnd')
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name=f"V 0.0.4"), status='dnd')
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name=f"with {len(bot.guilds)} servers boi!"), status='dnd')
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name=f"on discord."), status='dnd')
        await asyncio.sleep(15)

        
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)
        

def dev_check(id):
    with open('data/devs.json') as f:
        devs = json.load(f)
    if id in devs:
        return True
    return False
        
             
bot.api = idioticapi.Client((os.environ.get("IDIOTICAPI")), dev=True)

        
@bot.event
async def on_guild_join(guild):
    lol = bot.get_channel(438526627824271362)
    em = discord.Embed(color=discord.Color(value=0x11f95e))
    em.title = "I have joined new server!"
    em.description = f"Server: {guild}"
    em.set_footer(text=f"ID: {guild.id}")
    em.set_thumbnail(url=guild.icon_url)
    await lol.send(embed=em)
    try:
        await guild.channels[0].send(f"Hello my peeps. Im a discord bot created by L3NNY#4519. Try me out by doing ``+help``!")
    except discord.Forbidden:
        pass

      
@bot.event
async def on_guild_remove(guild):
    lol = bot.get_channel(438526627824271362)
    em = discord.Embed(color=discord.Color(value=0xf44242))
    em.title = "I have left a server."
    em.description = f"Server: {guild}"
    em.set_footer(text=f"ID: {guild.id}")
    await lol.send(embed=em)   
        
        
@bot.event
async def on_command(ctx):
    lol = bot.get_channel(445256970786701314)
    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(title = "Command Executed!", colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Server", value = ctx.guild, inline = True)
    embed.add_field(name="Server ID", value=ctx.guild.id)
    embed.add_field(name = "Channel", value = ctx.message.channel.name, inline = True)
    embed.add_field(name = "Author", value = ctx.message.author.name)
    embed.add_field(name="User ID", value=ctx.author.id)
    embed.add_field(name = "Content", value = "```{}```".format(ctx.message.clean_content))
    await lol.send(embed = embed)
        
        
@bot.command()
async def ping(ctx):
    """Get the bot's Websocket latency."""
    color = discord.Color(value=0x11f95e)
    em = discord.Embed(color=color, title='Pong! Websocket Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)

    
@bot.command()
async def invite(ctx):
    """lemme join dat c00l club""" 
    await ctx.send("lemme join that c00l kidz club: https://discordapp.com/api/oauth2/authorize?client_id=438487038032085025&permissions=8&scope=bot") 

    
@bot.command()
async def say(ctx, *, message: commands.clean_content()):
    '''Speak as me!'''
    await ctx.message.delete()
    await ctx.send(message)
    
    
@bot.command()
async def support(ctx):
    """join my lit support server""" 
    await ctx.send("time to join! https://discord.gg/FEPNu3A")      
    
        
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def emojify(ctx, *, msg):
        """Turn your text into emojis"""
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

        if msg:
            out = msg.lower()
            text = out.replace(' ', '    ').replace('10', '\u200B:keycap_ten:')\
                      .replace('ab', '\u200B🆎').replace('cl', '\u200B🆑')\
                      .replace('0', '\u200B:zero:').replace('1', '\u200B:one:')\
                      .replace('2', '\u200B:two:').replace('3', '\u200B:three:')\
                      .replace('4', '\u200B:four:').replace('5', '\u200B:five:')\
                      .replace('6', '\u200B:six:').replace('7', '\u200B:seven:')\
                      .replace('8', '\u200B:eight:').replace('9', '\u200B:nine:')\
                      .replace('!', '\u200B❗').replace('?', '\u200B❓')\
                      .replace('vs', '\u200B🆚').replace('.', '\u200B🔸')\
                      .replace(',', '🔻').replace('a', '\u200B🅰')\
                      .replace('b', '\u200B🅱').replace('c', '\u200B🇨')\
                      .replace('d', '\u200B🇩').replace('e', '\u200B🇪')\
                      .replace('f', '\u200B🇫').replace('g', '\u200B🇬')\
                      .replace('h', '\u200B🇭').replace('i', '\u200B🇮')\
                      .replace('j', '\u200B🇯').replace('k', '\u200B🇰')\
                      .replace('l', '\u200B🇱').replace('m', '\u200B🇲')\
                      .replace('n', '\u200B🇳').replace('ñ', '\u200B🇳')\
                      .replace('o', '\u200B🅾').replace('p', '\u200B🅿')\
                      .replace('q', '\u200B🇶').replace('r', '\u200B🇷')\
                      .replace('s', '\u200B🇸').replace('t', '\u200B🇹')\
                      .replace('u', '\u200B🇺').replace('v', '\u200B🇻')\
                      .replace('w', '\u200B🇼').replace('x', '\u200B🇽')\
                      .replace('y', '\u200B🇾').replace('z', '\u200B🇿')
            try:
                await ctx.send(text)
            except Exception as e:
                await ctx.send(f'```{e}```')
        else:
            await ctx.send('Write something, reee!', delete_after=3.0)

        
        
@bot.command(name='eval')
async def _eval(ctx, *, body):
    """Evaluates python code"""
    if not dev_check(ctx.author.id):
        return await ctx.send("You cannot use this because you are not a developer.")
    env = {
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        '_': bot._last_result,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text) - 1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))

    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:

                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            bot._last_result = ret
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')
    
    
if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
