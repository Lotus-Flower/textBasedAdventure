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
    print ("Hello, would you play a text based adventure?")

    while True:
        resp = input("(reply to this with 'y' or 'n') \n")

        if resp.lower() == "y":
            return
        elif resp.lower() == "n":
            #Exits python, may need to be edited if integrated on mobile
            sys.exit()

        
if __name__ == "__main__":
    main()
