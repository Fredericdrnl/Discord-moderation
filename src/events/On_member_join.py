import discord
from discord.ext import commands

class On_Member_JoinEvent(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        channel : discord.TextChannel = self.bot.get_channel(1074701940069502976)
        print(member.guild.roles)
        role = discord.utils.get(member.guild.roles, id=1074697517234651217, name="Visiteur")
        print(role)
        await member.add_roles(role)

        embedarrived = discord.Embed(title = "Bienvenue " + str(member.name) + " sur le serveur !")

        if member.avatar != None:
            embedarrived.set_image(url=member.avatar)
            embedarrived.set_footer(text="By WarFlay#8465",
                            icon_url="https://i.goopics.net/encbhm.png")

        await channel.send(content=member.mention + " 👋")
        await channel.send(embed=embedarrived)


def setup(bot):
    bot.add_cog(On_Member_JoinEvent(bot))