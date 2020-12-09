# Libraries
import discord
import threading
from discord.ext import commands

# Files
import level_visualiser
import mongo
import bot_token
import bad_joke
import wikipedia_search
import Google_search

# Version of The BOT
cookie_version = '1.3.2 Alpha'

# Version of Python
python_version = '3.8.3rc1'

# Author name
author = "@Abhi अभि"

# Number of Commands
numberOfCommands = 8

# Command prefix
cookie = commands.Bot(command_prefix='_')

# LIST OF COMMANDS/HELP (idk why but using Help was not allowed)
@cookie.command()
async def commands(context):
    embed = discord.Embed(title=f'COOKIE BOT {cookie_version}',color=0xffcc00)
    embed.add_field(name='_commands', value='Open The command list for Cookie Bot', inline=False)
    embed.add_field(name='_info', value='View the System Detalis', inline=False)
    embed.add_field(name='_givecookie', value='Ask Cookie for a :cookie:', inline=False)
    embed.add_field(name='_hi', value='Say Hi to Cookie', inline=False)
    embed.add_field(name='_google *Search Term*', value='Search for the "Search Term" on google', inline=False)
    embed.add_field(name='_youtube *Search Term*', value='Search for the "Search Term" on google', inline=False)
    embed.add_field(name='_rank', value='View your Rank on this server', inline=False)
    embed.add_field(name='_wiki *Search Term*', value='Search for the "Search Term" on Wikipedia\nThis command is still in development, It can throw errors', inline=False)
    embed.add_field(name='_lamejoke', value="Lame Joke", inline=False)
    embed.set_footer(text=f"Author -> {author}")

    await context.message.author.send(embed=embed)

@cookie.command()
async def rank(context):
    userid = str(context.message.author.id)
    serverid = str(context.message.guild.id)
    pfp = context.author.avatar_url
    data = mongo.retrive_data(userid=userid, serverid=serverid)
    level = data['level']
    xp = data['xp']
    next_level = data['next_level']
    emoji_visualise = level_visualiser.showlvl(xp, next_level)
    embed = discord.Embed(title=f'{context.message.author.name}',description=f"{emoji_visualise}", color=0xffcc00)
    embed.add_field(name='Level', value=f'{level}', inline=False)
    embed.add_field(name='XP', value=f'{xp}', inline=False)
    embed.add_field(name='Next Level', value=f'{next_level}', inline=False)
    # embed.add_field(name='', value=f'{emoji_visualise}', inline=False)
    embed.set_thumbnail(url=pfp)

    await context.message.channel.send(embed=embed)

# SAY HI TO COOKIE
@cookie.command()
async def hi(context):
    await context.message.channel.send(f'Hi {context.message.author.mention}')

# ASK COOKIE FOR A COOKIE
@cookie.command()
async def givecookie(context):
    embed = discord.Embed(title='COOKIE ?', description='Here\'s Your Cookie :cookie:', color=0xaeea79)
    await context.message.channel.send(embed=embed)

@cookie.command()
async def info(context):
    embed = discord.Embed(title='COOKIE BOT' + cookie_version, color=0xe07b39)
    embed.add_field(name='Python version', value=f'Python {python_version} 64bit', inline=False)
    embed.add_field(name='Number of Commands', value=f'{numberOfCommands}', inline=False)

    await context.message.channel.send(embed=embed)

# YOUTUBE SEARCH
@cookie.command()
async def youtube(context):
    query = context.message.content.lower().strip().replace('_youtube', '')
    try:
        result = Google_search.search_on_youtube(query)
        await context.message.channel.send(result)

    except Exception as e:
        print(e)
        embed = discord.Embed(title='No Results Were Found', description='Either the Connection to the Server was lost or No results were found', color=0xaeea79)
        await context.message.channel.send(embed= embed)

# GOOGLE SEARCH
@cookie.command()
async def google(context):
    query = context.message.content.lower().strip().replace('_google', '')
    try:
        result = Google_search.search_on_google(query)
        await context.message.channel.send(result)
    except Exception as error:
        embed = discord.Embed(title='No Results Were Found', description='Either the Connection to the Server was lost or No results were found', color=0xaeea79)
        await context.message.channel.send(embed=embed)

# WIKIPEDIA SEARCH
@cookie.command()
async def wiki(context):
    query = context.message.content.lower().strip().replace('_wiki', '')
    try:
        result = wikipedia_search.wiki_summary_short(query=query)
        title = wikipedia_search.wiki_full_page(query=query).title
        embed = discord.Embed(title=f"{title}", description=f"{result}", color=0x489AF7)
        await context.message.channel.send(embed=embed)

    except Exception as error:
        embed = discord.Embed(title="ERROR", description="Either no results were found\nOr the connection to the server was interrupted", color=0xe3430e)
        await context.message.channel.send(embed=embed)

# RANDOM BAD JOKE
@cookie.command()
async def lamejoke(context):
    try:
        joke = bad_joke.getJoke()
        embed = discord.Embed(title="Dad Jokes", description = f"{joke}", color=0xa25cb8)
        embed.set_thumbnail(url="https://avatars.slack-edge.com/2016-08-13/69162711190_9ce4a3707b47d2a5a8d4_512.png")
        embed.set_footer(text="https://icanhazdadjoke.com/")
        await context.message.channel.send(embed=embed)
    except Exception as e:
        print(e)

# WHEN THE BOT STARTS AND IS READY TO SEND MESSAGES
@cookie.event
async def on_ready():
    print('Cookie Bot version: ' + cookie_version)
    print('Bot started sucessfully')

    await cookie.change_presence(status=discord.Status.online , activity=discord.Game(name='Listening for _commands'))

@cookie.event
async def on_message(message):
    if message.author == cookie.user:
        return

    else:
        userid = str(message.author.id)
        serverid = str(message.guild.id)
        mongo.update_user(userid=userid, serverid=serverid)
        lvl_passed = mongo.level_passed(userid=userid, serverid=serverid)
        if lvl_passed:
            lst = mongo.retrive_data(userid=userid, serverid=serverid)
            level = lst['level']
            await message.channel.send(f'CONGRATULATIONS!, {message.author.mention} You reached Level {level}')

    await cookie.process_commands(message)

cookie.run(bot_token.getToken())