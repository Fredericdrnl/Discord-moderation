import discord
from discord.ext import commands
from time import sleep

class ClearCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot
        
    @commands.command()
    async def clear(self, ctx, number_of_message : int):
        messages = ctx.channel.history(limit=number_of_message + 1)
        async for each_message in messages:
            await each_message.delete()

        if number_of_message == 1 or number_of_message == 0:
            text = " message a été supprimé"
        else:
            text = " messages ont été supprimé"
        embedclear = discord.Embed(title = str(number_of_message) + text, colour = discord.Colour.from_rgb(0, 127, 255))
        embedclear.set_footer(text="By WarFlay#8465",
                    icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed=embedclear)
        sleep(5)
        embedsuppr = ctx.channel.history(limit=1)
        async for message in embedsuppr:
            await message.delete()

def setup(bot):
    bot.add_cog(ClearCommand(bot))
