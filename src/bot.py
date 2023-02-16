from discord.ext import commands
import os

print("[INFO] Launching bot...")

print("------------------")


class Moderation(commands.Bot):
    def __init__(self, intents, prefix = "!"):
        commands.Bot.__init__(self, command_prefix=prefix, intents = intents)

        for fils in os.listdir("./src/events"):
            if fils.endswith(".py"):
                self.load_extension("events." + fils[:-3])
                print(fils[:-3] + " event is UP !")

        print("------------------")

        for fils in os.listdir("./src/commands"):
            if fils.endswith(".py"):
                self.load_extension("commands." + fils[:-3])
                print(fils[:-3] + " command is UP !")

        print("------------------")

