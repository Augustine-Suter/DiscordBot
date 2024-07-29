import discord
from discord.ext import commands
import random

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # echo command
    @commands.command(name='echo', help='Echoes the input message.')
    async def echo(self, ctx, *, content:str):
        await ctx.send(content)

    # rock paper scissors game
    @commands.command(name='rps', help='Play rock-paper-scissors with the bot.')
    async def rock_paper_scissors(self, ctx, choice):
        valid_choices = ['rock', 'paper', 'scissors']
        if choice.lower() not in valid_choices:
            await ctx.send(f"Please choose either 'rock', 'paper', or 'scissors'.")
            return

        bot_choice = random.choice(valid_choices)
        if choice.lower() == bot_choice:
            await ctx.send(f"It's a tie! We both chose {bot_choice}.")
        elif (choice.lower() == 'rock' and bot_choice == 'scissors') or \
             (choice.lower() == 'paper' and bot_choice == 'rock') or \
             (choice.lower() == 'scissors' and bot_choice == 'paper'):
            await ctx.send(f"You win! {choice.capitalize()} beats {bot_choice}.")
        else:
            await ctx.send(f"You lose! {bot_choice.capitalize()} beats {choice}.")


async def setup(bot):
    await bot.add_cog(General(bot))