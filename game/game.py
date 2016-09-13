# Game Object for Text-Based Game
# Matthew Meehan
# September 9, 2016
# A Game Object will have a name, a list of rooms, a current room, and a current room number.
# The Game is set up, and will keep track of a player's progression.

import sys
from game import room
from game import choice

class game:
    def __init__(self, name, rooms, startRoom):
        self.name = name
        self.rooms = rooms
        self.currRoom = startRoom

def setup():
    #Sets up the game
    #Returns a new game
    
    name = "Nick's Tinder"
    rooms = []
    startRoom = None

    ##Create Room Information##
    
    roomIndex = []
    
    #Room 0
    #Room 0 is always the starting room, this room will never be assigned choices; simply a left and a right
    name = "at the Starting Room"
    desc = "It is boring, there is not much for you to do here."

    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 1
    name = "in a Desert"
    desc = "It is hot and sandy, but lovely for the more serious sunbathers. A dancing cactus approaches you."

    roomInfo = (name, desc)
    roomIndex.append(roomInfo)

    #Room 2
    name = "in an Igloo"
    desc = "It is surprisingly warm, but smells like raw fish and eskimo. Unfortunately, you have disturbed an important eskimo council meeting."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 3
    name = "in a Swamp"
    desc = "It reminds you of the movie shrek, and of your own home. A swamp monster emerges from the swampy depths, he dislikes you."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 4
    name = "at a River"
    desc = "The current moves quickly and purposefully. Should've brought your water wings. A fish hops from the water and speaks in a strange tongue, '*&#^^&#%*&^%&@*)@_@!!!'"
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)

    #Room 5
    name = "on a Beach"
    desc = "Luckily there are no nude patrons in sight. You let your guard down for a moment. Suddenly, quicksand approaches!!"
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 6
    name = "in a Forest"
    desc = "A sign warning visitors of bear sightings has been ironically torn in half by long claw marks. A polar bear reveals itself from among the trees."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 7
    name = "at a Volcano"
    desc = "Heat emanates from the crater. You realize you haven't brought any marshmallows. A low rumble can be heard before lava begins erupting from below. You only have minutes to react."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 8
    name = "at Nick's House"
    desc = "Congratulations! You answered every question the way Nick would have!"

    roomInfo = (name, desc)
    roomIndex.append(roomInfo)

    ##Creating Room Objects##
    
    rooms = room.roomSetup(roomIndex)

    ##Assign Left and Right Paths##
    
    rooms = room.roomRouting(rooms)

    ##Choices##

    choiceIndex = []
    correctList = []
    
    #Room 1    
    content1 = "Dance with the cactus"
    response1 = "You boogie down. Impressed, the cactus tells you that you are a better dancer than any cactus. What an achievement."
    content2 = "Hug cactus"
    response2 = "You die very quickly. What were you thinking?"
    content3 = "Drink cactus juice, it'll quench ya"
    response3 = "Your vision gets blurry and your judgement becomes lapsed. You're no longer in any state to be on Tinder."

    choices = [(content1, response1), (content2, response2), (content3, response3)]
    choiceIndex.append(choices)
    correctList.append("a")

    #Room 2
    content1 = "Overthrow the eskimo chief"
    response1 = "Attempting to overthrow the cheif gets you beat up by eskimos."
    content2 = "Pretend to be one of them"
    response2 = "You blend in with the tribe and they accept you as their own. You live a happy life among them for many years until one day you pull out your phone and notice you have not yet finished this Tinder game. You proceed."
    content3 = "Barter"
    response3 = "Eskimos don't barter. Everyone knows that."

    choices = [(content1, response1), (content2, response2), (content3, response3)]
    choiceIndex.append(choices)
    correctList.append("b")

    #Room 3
    content1 = "Compliment him on his fly new look"
    response1 = "The monster is flattered, but eats you anyway."
    content2 = "Insult his look"
    response2 = "The monster becomes upset. You console him. He explains that his mother thinks he is very handsome. You agree. He eats you."
    content3 = "Insult his mother"
    response3 = "The swamp monster runs away. Your strategy was rude, but effective."

    choices = [(content1, response1), (content2, response2), (content3, response3)]
    choiceIndex.append(choices)
    correctList.append("c")

    #Room 4
    content1 = "Reply with '@%$&^%('"
    response1 = "You talk good."
    content2 = "Cook the fish"
    response2 = "You attempt to cook the fish. You burn the fish."
    content3 = "Fish can't talk, idiot"
    response3 = "'Your have a poor imagination' the fish retorts."

    choices = [(content1, response1), (content2, response2), (content3, response3)]
    choiceIndex.append(choices)
    correctList.append("a")

    #Room 5
    content1 = "Attempt to outrun the quicksand - you are much quicker"
    response1 = "You can't outrun quicksand. Otherwise, they'd call it fatsand."
    content2 = "You don't really understand what's happening"
    response2 = "You drown anyway."
    content3 = "Begin shoveling quicksand into your mouth as quickly as possible"
    response3 = "The approaching sand is disturbed by your behavior, it quickly retreats. You pass, but you're a strange individual."

    choices = [(content1, response1), (content2, response2), (content3, response3)]
    choiceIndex.append(choices)
    correctList.append("c")

    #Room 6
    content1 = "Make yourself look big"
    response1 = "The bear mistakes you for its own cub, and you live the rest of your life as a smelly bear. How unfortunate."
    content2 = "Make yourself look small"
    response2 = "The bear feels empowered by your weak display, stands triumphantly on your small figure and poses, crushing you in the process."
    content3 = "Make yourself look medium"
    response3 = ".... The bear does nothing."

    choices = [(content1, response1), (content2, response2), (content3, response3)]
    choiceIndex.append(choices)
    correctList.append("c")

    #Room 7
    content1 = "Pose, so when they find your body, you'll be put in a museum"
    response1 = "You pose so grandly that rescue teams from all over the world come to save you. Hot stuff."
    content2 = "Get naked"
    response2 = "You're incinerated by the lava, nude. Is this how you make decisions in real life?"
    content3 = "Stop, drop, and roll at the highest rate possible"
    response3 = "You begin rolling. You continue rolling. You're rolling too fast. You're out of control. You roll so fast that time and space contort around you. You implode."

    choices = [(content1, response1), (content2, response2), (content3, response3)]
    choiceIndex.append(choices)
    correctList.append("a")

    #Room 8
    content1 = "I enjoyed it!"
    content2 = "I hated it!"
    content3 = "I feel dead inside!"
    response = "YOU WIN!! THANKS FOR THE FEEDBACK."

    choices = [(content1, response), (content2, response), (content3, response)]
    choiceIndex.append(choices)

    ##Create Choice Objects##
    rooms = choice.choicesSetup(rooms, choiceIndex)

    ##Assign Correct Answers##
    rooms = choice.correctSetup(rooms, correctList)


    ##Test Rooms##

    #for i in range(0, len(rooms)-1):
    #   print("\n\n" + rooms[i].name)
    #   print("\n" + rooms[i].desc)
        
    #   for j in range(0, len(rooms[i].choices)):
    #       print("\n" + rooms[i].choices[j])            
        
    #   print("\n" + rooms[i].left.name)
    #   print("\n" + rooms[i].right.name)

    #print("\n\n" + rooms[len(rooms)-1].name)
    #print("\n" + rooms[len(rooms)-1].desc)
        
    #for i in range(0, len(rooms[len(rooms)-1].choices)):
    #   print("\n" + rooms[len(rooms)-1].choices[i]) 
    
    ##Assign Start Room##

    startRoom = rooms[0]
    
    ##Creating the Game##
    
    newGame = game(name, rooms, startRoom)
    print("\nGame created!")

    return newGame


def gameLoop(newGame):

    #Takes a game object
    #Loops while you traverse through rooms, displays choices, responses, determines if choice was correct and whether or not it is a game over
    
    loopCount = 0
    abc = ["a","b","c"]
    
    while newGame.currRoom.left != None:
        
        print("\nYou find yourself " + newGame.currRoom.name + ". " + newGame.currRoom.desc)
        
        if loopCount == 0:
            print("\nLeaving the starting room, you arrive at a fork in the road (a crossroads, not a piece of silverwear). You can proceed left or right.")
        else:
            for char in abc:
                print("\n\n" + char + ") " + newGame.currRoom.choices[abc.index(char)].content)

            choice = ""

            while choice.lower() not in abc:            
                choice = input("\n\nWhat do you do? (a,b, or c)\n")

            print("\n" + newGame.currRoom.choices[abc.index(choice)].response + "\n")

            if newGame.currRoom.choices[abc.index(choice)].correct is False:
                gameOver = input("GAME OVER. Sorry, your adventure has concluded. (Reply with any letter)\n")
                sys.exit()
            
            
            print("\nFollowing your success you arrive at another fork in the road. You can proceed left or right.")
            
        direction = " "
        
        while direction.lower() not in ["right", "left"]:  
            direction = input("\nWhich way? ('left' or 'right')\n")

        if direction.lower() == "left":
            newGame.currRoom = newGame.currRoom.left
        elif direction.lower() == "right":
            newGame.currRoom = newGame.currRoom.right

        loopCount = loopCount + 1
            
    print("\n\nYou find yourself " + newGame.currRoom.name + ". " + newGame.currRoom.desc)

