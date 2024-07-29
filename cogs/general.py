import discord
from discord.ext import commands
import random

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='echo', help='Echoes the input message.')
    async def echo(self, ctx, *, content:str):
        await ctx.send(content)


async def setup(bot):
    await bot.add_cog(General(bot))