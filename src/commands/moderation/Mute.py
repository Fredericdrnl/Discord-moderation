import discord
from discord.ext import commands

class MuteCommands(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def mute(self, ctx, member : discord.Member):
            print(member.guild.roles)
            role = discord.utils.get(member.guild.roles, id=1075774748346302504, name='Mute')
            print(role)
            await member.add_roles(role)
            embed=discord.Embed(title=f"**{member}** à été mute par **{ctx.message.author}**!", colour=discord.Colour.from_rgb(0, 127, 255))
            await ctx.send(embed=embed)

    @commands.command()
    async def unmute(self, ctx, member : discord.Member):
        print(member.guild.roles)
        role = discord.utils.get(member.guild.roles, id=1075774748346302504, name='Mute')
        print(role)
        await member.remove_roles(role)
        embed=discord.Embed(title=f"**{member}** à été démute par **{ctx.message.author}**!", colour=discord.Colour.from_rgb(0, 127, 255))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MuteCommands(bot))