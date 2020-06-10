'''
HootBot v1.2

Developed for personal use by Vithraldor.
This is a basic bot that mimics an owl.

Past Versions:
v1.0 (6/9/2020): initial release of bot.
v1.1 (6/9/2020): minor bug fixes to F event, altered probability value for default case.
v1.2 (6/9/2020): Reworked F event: now increments instead of randomly generating numbers
v1.3 (6/10/2020): basic commands added
'''

import discord
from discord.ext import commands
import asyncio
import random
from random import seed

client = commands.Bot(command_prefix = 'h!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Game(name = "hoot hoot | h!hoot"))
    global respectCounter
    respectCounter = 0

# Commands
@client.command()
async def ping(ctx):
    await ctx.send(f"Hoot! {round(client.latency * 1000)} ms")

@client.command()
async def hoot(ctx, message):
    username = str(message)

    if '@' in username:
        await ctx.send("{} HOOT HOOT HOOT HOOT".format(username))
    else:
        await ctx.send("Hoot?\n*I need a username to use this command. Please try again.*")

# Automatic interactions done by the bot:
@client.event
async def on_message(message):
    
    # Allows the bot to both process commands and actively read input.
    await client.process_commands(message)

    # Checks if the message was sent by an actual user so the bot won't respond to itself
    if message.author == client.user:
        return

    # If user types F to pay respects. Now counts the total amount of respects given.
    elif message.content == 'F' or message.content == 'f':
        global respectCounter
        respectCounter += 1
        await message.channel.send('Hoot hoot!\n*Respects have been paid. Total respects paid: {}*'.format(respectCounter))

    # Adapability for Twitch emotes
    elif message.content == 'WHOMEGALUL' or message.content == 'whomegalul':
        await message.channel.send("HOOTMEGALUL")

    # If messages contain 'who' or 'WHO'
    elif 'who' in message.content:
        await message.channel.send('Hoooooo... **WHO?!**')

    elif 'WHO' in message.content:
        await message.channel.send('***HOOT HOOT***')

    elif 'Who' in message.content:
        await message.channel.send('Hoot hoot.')

    # If user hoots at the bot
    elif 'hoot' in message.content or 'Hoot' in message.content:
        if 'h!hoot' in message.content:
            return
        else:
            await message.channel.send('Hoot?')

    elif 'HOOT' in message.content:
        await message.channel.send('***HoOt HOoT***')

    # Default case. Will only send messages 33% of the time to reduce annoyance.
    else:
        seed()
        probabilityValue = int(random.random() * 100)

        elif probabilityValue >= 66:
            await message.channel.send('Hoot hoot')

client.run('Your bot token here')
