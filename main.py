from client import MyClient
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
intents = discord.Intents.default()

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("MTA0MzM1ODkwMzcxMjM2NjYxMg.GGfsEM.0OTeOReE_TtCRlbtvp2blHAv8_yp9ti_FW-HJQ")

