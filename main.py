import discord
import os
import requests
import json
import random
from stayalive import keep_alive

client = discord.Client()


#############################   greets    #####################################
greets = [
  "$hey","$hi","$Hey","$Hi","$hello","$Hello","$Hru","$How are you","$Hey there","$Ola",
  "$Ahoy","$Salam","$Hi Mariyana","$hi Mariyana"
  ]
respondGreets = [
  "Hey There buddy","Hi dude","Hello Sir","Hi there","Hey Cutie","Ahoy Seniorita","Hey Nigga"
]
################################################################################

############################   startingConvo   #################################
startup = [
  "$sup","$Sup","$whats up","$Whatsup","$Hru","$How are you?","$how are you","$Hows life","$Hows Life",
]
respondStartup = [
  "Hey there","Doin good","Nothing Special! What about you?","Great","I'm good","Fine, How are you?"
]

################################################################################

#############################   whatsnew   #####################################
whatsnew = [
  "$tell me something new","$Tell me something new","$whats new","$Whats new","$Anything new?","$anything new?","$anything new?"
]
                 #######  NEWS API  START ######
def get_news():
  api_key = "3801ab413561482db352ea18fd48edf4"
  url = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(api_key)
  responce = requests.get(url)
  json_news = json.loads(responce.text)
  count = 2
  for news in json_news['articles']:
    if count>0:
      count-=1
      return(str(news['title']))
                 #########  NEWS API END  ###### 

################################################################################




def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "  ~" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Logged in as DaBot')

@client.event
async def on_message(message):
  quote = get_quote()
  news = get_news()
  
  if message.author == client.user:
    return

  if any(word in message.content for word in greets):
    await message.channel.send(random.choice(respondGreets))


  if message.content.startswith('$quote'):
    await message.channel.send(quote)

  if any(word in message.content for word in startup):
    await message.channel.send(random.choice(respondStartup))

  if any(word in message.content for word in whatsnew):
    await message.channel.send(news)    

  if message.content.startswith('$your creater'):
    await message.channel.send('Ocama')
       

keep_alive()
client.run(os.getenv('token'))    
