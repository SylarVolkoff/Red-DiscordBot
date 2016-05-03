import discord
from discord.ext import commands
from .utils.dataIO import fileIO

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.player_names = fileIO("data/namess/log.json", "load")

    @commands.command()
    async def mycom(self, fName: str, lName: str, lv: str):
        """This does stuff!"""
        doge = fName + " " + lName + " " + lv
        #Your code will go here
        await self.bot.say("Your information will be recorded as: " + doge)
        fileIO("data/namess/log.json", "save", doge)

def setup(bot):
    bot.add_cog(Mycog(bot))