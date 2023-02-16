import discord
from discord.ext import commands

class BanCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.command()
    async def ban(self, ctx, member: discord.Member, reason : str = ""):
        messages = ctx.channel.history(limit = 1)
        await member.ban(reason=reason)
        embedban = discord.Embed(title = str(member.name) + " a été banni du serveur.", colour = discord.Colour.from_rgb(0, 127, 255))
        if reason != "":
            embedban.add_field(name="raison : " + reason, value="")  
        embedban.set_footer(text="By WarFlay#8465",
                        icon_url="https://i.goopics.net/encbhm.png")
        async for message in messages:
            await message.delete()
        await ctx.send(embed=embedban)

def setup(bot):
    bot.add_cog(BanCommand(bot))