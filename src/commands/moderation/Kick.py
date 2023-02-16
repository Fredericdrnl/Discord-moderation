import discord
from discord.ext import commands

class KickCommands(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.command()
    async def kick(self, ctx, member : discord.Member, reason : str = ""):
        messages = ctx.channel.history(limit = 1)
        try:
            await member.kick(reason=reason)
            embedkick = discord.Embed(title = str(member.name) + " a été kick du serveur par " + str(ctx.author.name) + ".", colour = discord.Colour.from_rgb(0, 127, 255))
            if reason != "":
                embedkick.add_field(name="raison : " + reason, value="")
            embedkick.set_footer(text="By WarFlay#8465",
                            icon_url="https://i.goopics.net/encbhm.png")
            messages = ctx.channel.history(limit = 1)
            async for message in messages:
                await message.delete()
            await ctx.send(embed=embedkick)
            await ctx.send(content= "(" + member.mention + ")")
        except:
            embedkick = discord.Embed(title = str(member.name) + "n'est pas sur le serveur.", colour = discord.Colour.from_rgb(0, 127, 255))
            return await ctx.send(embed=embedkick)
        
def setup(bot):
    bot.add_cog(KickCommands(bot))