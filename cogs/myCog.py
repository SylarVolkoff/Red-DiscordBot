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
        #self.player_names = fileIO("data/namess/log.json", "load")

    @commands.command()
    async def mycom(self, fname: str, lname: str, lv: str):
        """This does stuff!"""
        doge = fname + " " + lname + " " + lv
        #Your code will go here
        await self.bot.say("Your information will be recorded as: " + doge)
        #fileIO("data/namess/log.json", "save", doge)

def setup(bot):
    bot.add_cog(Mycog(bot))