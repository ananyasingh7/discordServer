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
        if channel.name == 'c3po-testing':
            await channel.send('Welcome ' + member.mention)
    role = discord.utils.get(member.guild.roles, name="human-beings")
    await member.add_roles(role)


client.run(TOKEN)