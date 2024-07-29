# Augustine Suter
# CSE485 Capstone

import discord
from discord.ext import commands
import json
import os

# Load the configuration from config.json
if not os.path.isfile("config.json"):
    print("config.json was not found and is required for the bot to run")
    exit()
else:
    with open("config.json") as file:
        config = json.load(file)

# Setup bot with required intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Define bot class
class SimpleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config['prefix'], intents=intents)
    
    async def on_ready(self):
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')
        print('------')

# Initialize  bot instance
bot = SimpleBot()

# Run the bot
bot.run(config['token'])