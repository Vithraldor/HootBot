'''
HootBot v1.2

Developed for personal use by Vithraldor.
This is a basic bot that mimics an owl.

Past Versions:
v1.0 (6/9/2020): initial release of bot.
v1.1 (6/9/2020): minor bug fixes to F event, altered probability value for default case.
v1.2 (6/9/2020): Reworked F event: now increments instead of randomly generating numbers
'''

import discord
import asyncio
import random
from random import seed

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Game(name = "hoot hoot"))
    global respectCounter
    respectCounter = 0

@client.event
async def on_message(message):
    # Checks if the message was sent by an actual user so the bot won't respond to itself
    if message.author == client.user:
        return

    # If user types F to pay respects. Counts amount of respects given across ALL servers the bot is active in.
    elif message.content == 'F' or message.content == 'f':
        global respectCounter
        respectCounter += 1
        await message.channel.send('Hoot hoot!\n*Respects have been paid. Total respects paid: {}*'.format(respectCounter))

    # If messages contain 'who' or 'WHO'
    elif 'who' in message.content:
        await message.channel.send('Hoooooo... **WHO?!**')

    elif 'WHO' in message.content:
        await message.channel.send('***HOOT HOOT***')

    # Default case. Will only send messages 33% of the time to reduce annoyance.
    else:
        seed()
        probabilityValue = int(random.random() * 100)
        
        if probabilityValue >= 66:
            await message.channel.send('Hoot hoot')

client.run('Your bot token here')
