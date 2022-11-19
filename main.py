from client import MyClient
import os

import discord

TOKEN = os.environ['DISCORD_TOKEN']
print(TOKEN)
intents = discord.Intents.default()

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

