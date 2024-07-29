# Augustine Suter
# CSE485 Capstone

import discord
from datetime import datetime
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
intents.message_content = True
intents.members = True

# Define bot class
class SimpleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config['prefix'], intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')
        print('------')
        await self.load_cogs()

    async def load_cogs(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')

                
# Initialize  bot instance
bot = SimpleBot()

# Startup message
@bot.event
async def on_ready():
    status_channel_id = 1267317067753984116
    status_channel = bot.get_channel(status_channel_id)
    if status_channel:
        startup_embed = discord.Embed(title=f"Capstone Bot is now online", 
                                        description=f"This bot has started properly", 
                                        timestamp=datetime.now()
                                        )
        startup_embed.set_author(name="CapstoneBot")
        await status_channel.send(embed=startup_embed)

# Run the bot
bot.run(config['token'])