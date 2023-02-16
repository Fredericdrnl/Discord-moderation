import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def helps(self, ctx):
        embed = discord.Embed(title="Help commands", description="Shows various help commands")
        embed.add_field(name="Show this help", value = "`/help`", inline = False)
        embed.add_field(name="Help random stuff", value="`/helprand`", inline=False)
        embed.add_field(name="Help economy", value="`/helpeco`", inline=False)
        embed.add_field(name="Help music", value = "`/helpmusic`", inline = False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommand(bot))