import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does shit"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, cat : str):
        """This does stuff"""

        print(cat)

    def setup(bot):
        bot.add_cog(Mycog(bot))