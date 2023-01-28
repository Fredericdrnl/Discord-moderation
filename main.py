import discord
from discord.ext import commands
from time import sleep
import asyncio
import selectors

# Author : WarFlay#8465 on discord

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ INIT BOT ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

# For async/await
selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

print("[INFO] Launching bot...")
# Init for commands

# Init for Bot
intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix="!", intents=intent)


# Message when bot is ready
@bot.event
async def on_ready():
  print("[INFO] Bot is ready !")


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■ COMMANDS ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

@bot.command(pass_context = True)
async def kick(ctx, member : discord.Member, reason : str = ""):
  await member.kick(reason=reason)
  embedkick = discord.Embed(title = str(member.name) + " a été kick du serveur.", colour = discord.Colour.from_rgb(0, 127, 255))
  if reason != "":
    embedkick.add_field(name="raison : " + reason, value="")
  embedkick.set_footer(text="By WarFlay#8465",
                  icon_url="https://i.goopics.net/encbhm.png")
  await ctx.send(embed=embedkick)

@bot.command(pass_context = True)
async def ban(ctx, member: discord.Member, reason : str = ""):
  await member.ban(reason=reason)
  embedban = discord.Embed(title = str(member.name) + " a été banni du serveur.", colour = discord.Colour.from_rgb(0, 127, 255))
  if reason != "":
    embedban.add_field(name="raison : " + reason, value="")  
  embedban.set_footer(text="By WarFlay#8465",
                  icon_url="https://i.goopics.net/encbhm.png")
  await ctx.send(embed=embedban)
   
@bot.command(pass_context = True)  
async def unban(ctx, member):
    banned_users = ctx.guild.bans()
    print(banned_users)
    member_name, member_discriminator = member.split('#')

    async for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
          print("coucou")
          await ctx.guild.unban(user)
          embedban = discord.Embed(title = str(user.name) + " a été unban du serveur.", colour = discord.Colour.from_rgb(0, 127, 255))
          embedban.set_footer(text="By WarFlay#8465",
                          icon_url="https://i.goopics.net/encbhm.png")
        else:
          print("coucou2")
          embedban = discord.Embed(title = "L'utilisateur saisi n'est pas banni du serveur.", colour = discord.Colour.from_rgb(196, 43, 28))
          embedban.set_footer(text="By WarFlay#8465",
                          icon_url="https://i.goopics.net/encbhm.png")
    await ctx.send(embed=embedban)

@bot.command(pass_context = True)  
async def clear(ctx, number_of_message : int):
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



# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■ RUN ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

bot.run(open("token.txt", "r").readline())
