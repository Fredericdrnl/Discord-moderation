from discord.ext import commands
import os

print("[INFO] Launching bot...")

class Moderation(commands.Bot):
    def __init__(self, intents, prefix = "!"):
        commands.Bot.__init__(self, command_prefix=prefix, intents = intents)

        print("====== EVENTS ======")
        for fils in os.listdir("./src/events"):
            if fils.endswith(".py"):
                self.load_extension("events." + fils[:-3])
                print(fils[:-3] + " event is UP !")

        print("====== MODERATION COMMANDS ======")

        for fils in os.listdir("./src/commands/moderation"):
            if fils.endswith(".py"):
                self.load_extension("commands.moderation." + fils[:-3])
                print(fils[:-3] + " command is UP !")

        print("====== SC COMMANDS ======")
        for fils in os.listdir("./src/commands/slashcommands"):
            if fils.endswith(".py"):
                self.load_extension("commands.slashcommands." + fils[:-3])
                print(fils[:-3] + " command is UP !")

        print("====== HELP COMMANDS ======")
        for fils in os.listdir("./src/commands/help"):
            if fils.endswith(".py"):
                self.load_extension("commands.help." + fils[:-3])
                print(fils[:-3] + " command is UP !")


