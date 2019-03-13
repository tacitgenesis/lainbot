import discord
import random
import os
from discord import Game
from discord.ext.commands import Bot

# Grab the $TOKEN variable from your environment
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await client.change_presence(game=discord.Game(name='lain help'))
    
    if message.content.startswith('lain invite'):
        msg = "https://discordbots.org/bot/530107695630647296".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('lain roll dice'):
        msg = random.randint(1,6)
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain I love you'):
        msg = "I love you too, {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain say hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain say goodbye'):
        msg = 'Goodbye {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain code"):
        msg = "here is the lain bot github: https://github.com/TheSorton/lainbot".format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith("lain support"):
        msg = "LainBot's support server: https://discord.gg/r5S7A2d".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain game"):
        msg = 'http://laingame.net/'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain dab"):
        msg = 'https://imgur.com/ot6F47X'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('lain say you are a gamer'):
        msg = 'I am the most epic gamer {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain avatar'):
        msg = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/5ca09a54-c660-4578-89de-c0ec615b15bc/dad0kb5-dd8b3bac-2742-4b73-96f0-c6fae66ee020.jpg'
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain die'):
        msg = "I will live forever, however you will die a most painful death fool. https://i.4pcdn.org/x/1414265593395.gif"
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain rise up'):
        msg = "I will already live forever, user. https://growingbranch.files.wordpress.com/2011/05/snapshot20110502230349.jpg"
        await client.send_message(message.channel, msg)
  
    if message.content.startswith("lain wired"):
        msg = "the truth awaits, user. https://fauux.neocities.org/login.html"
        await client.send_message(message.channel, msg)
    
    if message.content.startswith("lain information"):
        msg = "here is what you need, user. https://fauux.neocities.org/help.html"
        await client.send_message(message.channel, msg)
    
    if message.content.startswith("lain say ame"):
        msg = "ame ame ame"
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain live"):
        msg = "I will live forever, thank you user. https://discordemoji.com/assets/emoji/smile_lain.png"
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain eat me"):
        msg = "NOM"
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain magic eight ball"):
        msg = random.choice(open("res/8ball").readlines())
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain help'):
        msg = open("res/help").read()
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain song"):
        msg = random.choice(open("res/songs").readlines())
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('lain hug'):
        msg = (message.content + "!! amazing hug:" + random.choice(open("res/hug").readlines())) 
        await client.send_message(message.channel, msg)
   
    if message.content.startswith('lain slap'):
        msg = (message.content + ", hope that stings..:" + random.choice(open("res/slappu").readlines()))
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain pat'):
        msg = (message.content + "!!! uwu...:" + random.choice(open("res/pattu").readlines()))
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain quote'):
        msg = random.choice(open("res/quotes").readlines())
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('lain site'):
        msg = random.choice(open("res/sites").readlines())
        await client.send_message(message.channel, msg)

    if message.content.startswith("lain goose"):
        msg = random.choice(open("res/geese").readlines())
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain meme'):
        msg = random.choice(open("res/memes").readlines())
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('lain gif'):
        msg = random.choice(open("res/gif").readlines())
        await client.send_message(message.channel, msg)

    if message.content.startswith('lain image'):
        msg = random.choice(open("res/images").readlines())
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
