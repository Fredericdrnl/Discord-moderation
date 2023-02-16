import discord
from discord.ext import commands

class GiveRoleCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.command()
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        giveRoleEmbed : discord.Embed = discord.Embed(title=f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")
        giveRoleEmbed.set_footer(text="By WarFlay#8465",
                    icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed = giveRoleEmbed)

def setup(bot):
    bot.add_cog(GiveRoleCommand(bot))