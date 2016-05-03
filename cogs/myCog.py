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
    """My custom cog that does shit"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, cat: str):
        """This does stuff"""

        print(cat)

    def setup(bot):
        bot.add_cog(Mycog(bot))