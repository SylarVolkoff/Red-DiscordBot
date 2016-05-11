import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
import os
import time
import aiohttp
import asyncio
from copy import deepcopy
import logging

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.player_data = fileIO("data/log.json", "load")

        #I mean. This is annoying but it works. for starters.
    @commands.command()
    async def mycom(self, ctx, fname: str, lname: str, lv: str):
        """This does stuff!"""
        user = ctx.message.author
        doge = fname + " " + lname + " " + lv
        #Your code will go here

        if user.id not in self.player_data:
            self.player_data[user.id] = {"pKey" : user.id, "name" : user.name,"cat" : doge}
            fileIO("data/log.json", "save", self.player_data)
        else:
            await self.bot.say("You gucci")

        await self.bot.say("Your information will be recorded as: " + "`" + doge + "`")

def setup(bot):
    bot.add_cog(Mycog(bot))