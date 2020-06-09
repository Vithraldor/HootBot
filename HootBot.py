import discord
import random
from random import seed

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    # Checks if the message was sent by an actual user so the bot won't respond to itself
    if message.author == client.user:
        return

    # If user types F to pay respects. A number is randomly generated between 0 and 100 to represent the 'total' amount of respects given.
    elif message.content.startswith('F'):
        seed()
        respectCounter = int(random.random() * 100)
        await message.channel.send('Hoot hoot!\n*Respects have been paid. Total respects paid: {}*'.format(respectCounter))

    # If messages contain 'who' or 'WHO'
    elif 'who' in message.content:
        await message.channel.send('Hoooooo... **WHO?!**')

    elif 'WHO' in message.content:
        await message.channel.send('***HOOT HOOT***')

    # Default case - there is a 50% chance that the bot will respond with hoot hoot to reduce annoyance
    else:
        seed()
        probabilityValue = int(random.random() * 100)
        
        if probabilityValue >= 50:
            await message.channel.send('Hoot hoot')

client.run('')