import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import randint
from copy import deepcopy
from .utils import checks
from __main__ import send_cmd_help
import os
import time
import logging

class doge:
    """I'm getting tired of this dammit."""

    def __int__(self, bot):
        self.bot = bot
        self.player_data = fileIO("data/log.json", "load")

        @commands.group(name="poop", pass_context=True)
        async def _poop(self, ctx):
            """Poop operations?"""
            if ctx.invoked_subcommand is None:
                await send_cmd_help(ctx)

        @_poop.command(pass_context=True, no_pm=True)
        async def cate(self, ctx, fname: str):
            """lksdfj"""
            user = ctx.message.author
            if user.id not in self.player_data:
                self.player_data[user.id] = {"name": user.name, "First Name": fname}
                fileIO("data/log.json", "save", self.player_data)
                await self.bot.say("Logged as " + fname)
            else:
                await self.bot.say("Something fucked up bro.")

def setup(bot):
    bot.add_cog(doge(bot))
