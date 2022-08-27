import discord                            #asynchronous library (use callbacks)

import os                                 #for getting the environmental variable  

import requests                           #allows the bot to send http requests

import json                               #makes it eaiser to work with the data that is returned from the request

import random                             #for romdomisation

from discord.ext import commands          #for the  commands of the bot

#making the commands case insensitive

bot = commands.Bot(command_prefix=";", case_insensitive=True)

#random greeting text for the ;hello command

def greet_text():
  greet=['Hey there!','Millenials say this to greet each other- Whasssuup','Leave me alone, Im tring to           sleep here','Hi','Moshi Moshi','Hello!','Right here', 'Im all ears','Gimme a sec...ummmmmm...yep,tell me :)','Whoa, what does a good looking human want with a bot like me?','Beep Boop Beep-Human Detected-Instant Kill mode=on']
  return(random.choice(greet))

#getting randomised quotes from the zenquotes.io api

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  #convert the quote to json
  json_data = json.loads(response.text)
  #getting the quote out of it
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#getting randomised news websites

def get_news():
 news={'Vice India': 'https://www.vice.com/en/topic/india','BBC News':'https://www.bbc.com/news/world/asia/india','Google News':'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en','The Economic Times':'https://economictimes.indiatimes.com/'}
  k, v=random.choice(list(news.items()))
  return(k,v)


#creating a connection (instance of a client)

client=discord.Client()

#register an event

@client.event 

#this event will be called when the bot is ready to be used  
        
async def on_ready():

  print(f"We have logged in as {client.user}")

#register an event

@client.event

#this event is occurs when the message is recieved, if message is from the bot the event is not triggered

async def on_message(message):
  if message.author == client.user:
    return 

  #curses
  
  curses=[#insert the curse words that are inappropriate for a member of your server to use in the form of a strings#]

  if any(word in message.content.lower() for word in curses):
    await message.channel.send("Please refrain from using curses in this server, you will be BANNED indefinitely if the actions are continued")

  #assume that our commands starts with ;,therefore bot checks if its a command

  #if the command is ;inspire, the bot replies with a quote and the author that has said it

  if message.content.lower()==';inspire':
    quote=get_quote()
    await message.channel.send(quote)

  #if the command is ;hello, the bot replies with a hello

  if message.content.lower()==';hello':
    greet=greet_text()
    await message.channel.send(greet)
    await message.channel.send(message.author.mention)

  #link to google

  if message.content.lower()==';google':
     await message.channel.send("https://www.google.co.in/")
  
  #songs

  if message.content.lower()==';music':
    await message.channel.send("Youtube Music:")
    await message.channel.send("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")

  #news

  if message.content.lower()==';news':
    k,v=get_news()
    await message.channel.send("News right out of the oven:")
    await message.channel.send(f"{k} : {v}")
  
#run the bot with the environment variable token

client.run(os.getenv('token'))
#my_secret = os.environ['token']

