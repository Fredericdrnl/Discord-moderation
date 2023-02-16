import discord
from discord.ext import commands

class RoleCommands(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.command()
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        giveRoleEmbed : discord.Embed = discord.Embed(title=f"Le rôle {role.name} a été ajouté pour le joueur {user.name}")
        giveRoleEmbed.set_footer(text="By WarFlay#8465",
                    icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed = giveRoleEmbed)

    @commands.command()
    async def removerole(self, ctx, user: discord.Member, role: discord.Role):
        await user.remove_roles(role)
        removeRoleEmbed : discord.Embed = discord.Embed(title=f"Le rôle {role.name} a été enlevé pour le joueur {user.name}")
        removeRoleEmbed.set_footer(text="By WarFlay#8465",
                    icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed = removeRoleEmbed)

def setup(bot):
    bot.add_cog(RoleCommands(bot))