# Main Program for Text-Based Game
# Matthew Meehan
# September 9, 2016

import sys
from game import game

def main():
    hello()

    newGame = game.setup()

    print("\nThe Beginning of your journey . . .")

    game.gameLoop(newGame)

def hello():
    name = "Matthew"
    print ("Hello " + name + "! I'm glad we matched. However, to know if we are really a match, will you play a game with me? The only rule is you can only respond to the prompts while you are playing the game; I cannot talk to you once you are inside. So how about it?")

    while True:
        resp = input("(reply to this with 'y' or 'n') \n")

        if resp.lower() == "y":
            return
        elif resp.lower() == "n":
            #Exits python, may need to be edited if integrated on mobile
            sys.exit()

        
if __name__ == "__main__":
    main()
