import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('WELCOME_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(str(client.user) + 'has connected to the following server: ' + str(client.guilds[0]))

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel.name == 'welcome':
            await channel.send('Welcome ' + str(member))


client.run(TOKEN)