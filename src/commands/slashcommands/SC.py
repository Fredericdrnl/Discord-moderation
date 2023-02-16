import discord
from discord.ext import commands

class SlashCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.slash_command()
    async def sc(self, ctx):
        embedSC : discord.Embed = discord.Embed(title="SC", colour=discord.Colour.from_rgb(46, 169, 103))
        embedSC.set_footer(text="By WarFlay#8465",
            icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed=embedSC)

def setup(bot):
    bot.add_cog(SlashCommand(bot))