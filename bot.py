# Bot.py is where we create the bots instance! What we are going to achive in this code is,
# We will be abled to define a bot instance and enable intents.
# First we will start off by importing what we need!

import discord # We will need this to enable intents, as needed in discord.py 2.2.0+
from discord.ext import commands # Commands is used to create the bots commands.

intents = discord.Intents.all() # Here we define our intents, it is not reccomended to use all, but for the sake of this we will

bot = commands.Bot(command_prefix='!', intents=intents) # Here we define our bots instance + You can change the prefix

# Our bot instance comes with a built in (prefix)help command, we can change this either by using pretty_help or removing the command.

# Next we want to know when our bot comes online, now we will define a on ready event.

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator}') # When we start our bot, it will print Logged in as Tutorial#1234

# Next we will define a command, keep in mind you may change this how ever way you would like.

@bot.command(name='COMMAND-NAME')
async def COMMAND-NAME(ctx):
    await ctx.send('BOT RESPONSE')

# We have defined a command successfully! Now we can create a system to log in!

bot.run('BOT-TOKEN-HERE')

# Alright! We have created a bot!
