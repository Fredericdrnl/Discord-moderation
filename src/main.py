import os
import discord
from bot import Moderation

# * This is my main method
# ! this can be aonly static
# ? Do I need to check for exception in this
# todo : we need to call some method from this
# @param args   
# @throws Exception

class Main():
    @staticmethod
    def run():
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        try:
            token = open(os.path.join(__location__, "token.txt"), "r").read().strip("\n")
        except FileNotFoundError:
            quit("Please create a token.txt file and place your token in it!")
        if token is None:
            quit("Please create a token.txt file and place your token in it!")
        else:
            intent = discord.Intents.all()
            intent.members = True
            intent.message_content = True
            bot = Moderation(intent)
            bot.run(open("./src/token.txt", "r").readline())

if __name__ == '__main__':
    Main.run()



    
            



    