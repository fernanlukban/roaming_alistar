from discord.ext import commands

class GameCreator(commands.Cog):
    """
    Creates a game using the tournament API from Riot Games
    """
    def __init__(self, bot):
        self.bot = bot