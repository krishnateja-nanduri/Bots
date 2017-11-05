import discord
import asyncio
import datetime


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print('------')


@client.event

async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'Hello, World!')
          

client.run('Token Here')
