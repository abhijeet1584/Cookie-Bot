# Discord
import discord
from discord.ext import commands
import Google_search
import database_controller

# Version of The BOT
cookie_version = '1.0.0 Alpha'

# Version of Python
python_version = '3.8.3rc1'

# Command prefix
cookie = commands.Bot(command_prefix='_')

# LIST OF COMMANDS/HELP (idk why but using Help was not allowed)
@cookie.command()
async def commands(context):
    embed = discord.Embed(title=f'COOKIE BOT {cookie_version}',color=0xffcc00)
    embed.add_field(name='_commands', value='Open The command list for Cookie Bot', inline=False)
    embed.add_field(name='_info', value='View the System Detalis', inline=False)
    embed.add_field(name='_givcookie', value='Ask Cookie for a :cookie:', inline=False)
    embed.add_field(name='_hi', value='Say Hi to Cookie', inline=False)
    embed.add_field(name='_google *Search Term*', value='Search for the "Search Term" on google', inline=False)
    embed.add_field(name='_youtube *Search Term*', value='Search for the "Search Term" on google', inline=False)
    embed.add_field(name='_rank', value='View your Rank on this server', inline=False)

    await context.message.author.send(embed=embed)


# SAY HI TO COOKIE
@cookie.command()
async def hi(context):
    await context.message.channel.send(f'Hi {context.message.author.mention}')

# ASK COOKIE FOR A COOKIE
@cookie.command()
async def givcookie(context):
    embed = discord.Embed(title='COOKIE ?', description='Here\'s Your Cookie :cookie:', color=0xaeea79)
    await context.message.channel.send(embed=embed)

@cookie.command()
async def info(context):
    embed = discord.Embed(title='COOKIE BOT' + cookie_version, color=0xe07b39)
    embed.add_field(name='Python version', value=f'Python {python_version} 64bit', inline=False)
    embed.add_field(name='Number of Commands', value='6', inline=False)

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
    except Exception as e:
        embed = discord.Embed(title='No Results Were Found', description='Either the Connection to the Server was lost or No results were found', color=0xaeea79)
        await context.message.channel.send(embed=embed)

# XP OF THE MEMBER
@cookie.command()
async def rank(context):
    serverid = str(context.message.guild.id)
    userid = str(context.message.author.id)
    xp_lst = database_controller.fetch_data(serverID=serverid, userID=userid)
    xp = xp_lst[2]
    lvl = xp_lst[3]
    next_lvl = xp_lst[4]
    embed = discord.Embed(title=f'{context.message.author.name}', color=0x79c7ea)
    embed.add_field(name='XP', value=f'{xp}', inline=False)
    embed.add_field(name='Level', value=f'{lvl}', inline=False)
    embed.add_field(name='XP for Next Level', value=f'{next_lvl}', inline=False)

    await context.message.channel.send(embed=embed)

# NEW MEMBER JOIN
@cookie.event
async def on_member_join(context):
    serverid = str(context.message.guild.id)
    userid = str(context.message.author.id)
    fullid = userid + serverid
    print('New member joined')
    await context.message.channel.send(f'Hi, {context.message.author.mention}\nWelcome to {context.message.guild.name}\nHope You will have Fun here')
    database_controller.new_entry(fullid)

# WHEN THE BOT STARTS AND IS READY TO SEND MESSAGES
@cookie.event
async def on_ready():
    database_controller.create_table() # This method creates table if it doesn't exist
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
        reached_new_level = database_controller.update_rank(serverID=serverid, userID=userid)

        # The function return true if the level has been incrementeed
        if reached_new_level == True:
            lst = database_controller.fetch_data(serverID=serverid, userID=userid)
            level = lst[3]
            await message.channel.send(f'CONGRATULATIONS! {message.author.mention}, You reached Level {level}')


    await cookie.process_commands(message)

cookie.run('BOT TOKEN')