import discord
from discord.ext import commands

class UnbanCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.command()
    async def unban(self, ctx, member : str):
        messages = ctx.channel.history(limit = 1)
        banned_users = ctx.guild.bans()
        print(banned_users)
        member_name, member_discriminator = member.split('#')

        async for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embedban = discord.Embed(title = str(user.name) + " a été unban du serveur.", colour = discord.Colour.from_rgb(0, 127, 255))
                embedban.set_footer(text="By WarFlay#8465",
                                icon_url="https://i.goopics.net/encbhm.png")
            else:
                embedban = discord.Embed(title = "L'utilisateur saisi n'est pas banni du serveur.", colour = discord.Colour.from_rgb(196, 43, 28))
                embedban.set_footer(text="By WarFlay#8465",
                                icon_url="https://i.goopics.net/encbhm.png")
        async for message in messages:
            await message.delete()
        await ctx.send(embed=embedban)

def setup(bot):
    bot.add_cog(UnbanCommand(bot))