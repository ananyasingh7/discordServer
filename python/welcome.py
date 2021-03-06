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
            await channel.send('Hello ' + member.mention + '. I do not believe we have been introduced. I am C-3PO, Human-Cyborg Relations. ' 
            + 'I would like to welcome you to the AnanyaTech Server! ' + 'I have currently identified you as a human-being. ' +
            'If you also wish to be part of the beta testing team, react on this message with a :thumbsup: . ')

    role = discord.utils.get(member.guild.roles, name="human-beings")
    await member.add_roles(role)

@client.event
async def on_reaction_add(reaction, member):
    Channel = client.get_channel('713854349662486659')
    if reaction.emoji == '👍':
        role_developer = discord.utils.get(member.guild.roles, name="developers")
        await member.add_roles(role_developer)


client.run(TOKEN)