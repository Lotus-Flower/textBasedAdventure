# Game Object for Text-Based Game
# Matthew Meehan
# September 9, 2016
# A Game Object will have a name, a list of rooms, a current room, and a current room number.
# The Game is set up, and will keep track of a player's progression.

from game import room
from game import choice

class game:
    def __init__(self, name, rooms, startRoom):
        self.name = name
        self.rooms = rooms
        self.currRoom = startRoom

def setup():
    name = "Nick's Tinder"
    rooms = []
    startRoom = None

    ##Create Room Information##
    
    roomIndex = []
    
    #Room 0
    name = "at the Starting Room"
    desc = "It is boring, there is not much for you to do here."

    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 1
    name = "in a Desert"
    desc = "It is hot and sandy, but lovely for the more serious sunbathers."

    roomInfo = (name, desc)
    roomIndex.append(roomInfo)

    #Room 2
    name = "in an Igloo"
    desc = "It is surprisingly warm, but smells like raw fish and eskimo."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 3
    name = "in a Swamp"
    desc = "It reminds you of the movie shrek, and of your own home."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 4
    name = "at a River"
    desc = "The current moves quickly and purposefully. Should've brought your water wings."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)

    #Room 5
    name = "on a Beach"
    desc = "Luckily there are no nude patrons in sight."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 6
    name = "in a Forest"
    desc = "A sign warning visitors of bear sightings has been ironically torn in half by long claw marks."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 7
    name = "at a Volcano"
    desc = "Heat emanates from the crater. You realize you haven't brought any marshmallows."
    
    roomInfo = (name, desc)
    roomIndex.append(roomInfo)
    
    #Room 8
    name = "at Nick's House"
    desc = "Congratulations!"

    roomInfo = (name, desc)
    roomIndex.append(roomInfo)

    ##Creating Room Objects##
    
    rooms = room.roomSetup(roomIndex)

    ##Assign Left and Right Paths##
    
    rooms = room.roomRouting(rooms)

    ##Choices##

    choiceIndex = []
    
    #Room 1    
    choice1 = "Dance with the cactus"
    choice2 = "Hug cactus"
    choice3 = "Drink cactus juice, it'll quench ya"

    choices = [choice1, choice2, choice3]
    choiceIndex.append(choices)

    #Room 2
    choice1 = "Overthrow the eskimo chief"
    choice2 = "Pretend to be one of them"
    choice3 = "Barter"

    choices = [choice1, choice2, choice3]
    choiceIndex.append(choices)

    #Room 3
    choice1 = "Compliment him on his fly new look"
    choice2 = "Insult his look"
    choice3 = "Insult his mother"

    choices = [choice1, choice2, choice3]
    choiceIndex.append(choices)

    #Room 4
    choice1 = "Reply with '@%$&^%('"
    choice2 = "Cook the fish"
    choice3 = "Fish can't talk idiot"

    choices = [choice1, choice2, choice3]
    choiceIndex.append(choices)

    #Room 5
    choice1 = "Attempt to outrun the quicksand - you are much quicker"
    choice2 = "You don't really understand what's happening"
    choice3 = "Begin shoveling quicksand into your mouth as quickly as possible"

    choices = [choice1, choice2, choice3]
    choiceIndex.append(choices)

    #Room 6
    choice1 = "Make yourself look big"
    choice2 = "Make yourself look small"
    choice3 = "Make yourself look medium"

    choices = [choice1, choice2, choice3]
    choiceIndex.append(choices)

    #Room 7
    choice1 = "Pose, so when they find your body, you'll be put in a museum"
    choice2 = "Get naked"
    choice3 = "Stop, drop, and role at the highest rate possible"

    choices = [choice1, choice2, choice3]
    choiceIndex.append(choices)
    
    rooms = choice.choicesSetup(rooms, choiceIndex)

    ##Test Rooms##

    #for i in range(0, len(rooms)-1):
        #print("\n\n" + rooms[i].name)
        #print("\n" + rooms[i].desc)
        
        #for j in range(0, len(rooms[i].choices)):
            #print("\n" + rooms[i].choices[j])            
        
        #print("\n" + rooms[i].left.name)
        #print("\n" + rooms[i].right.name)

    #print("\n\n" + rooms[len(rooms)-1].name)
    #print("\n" + rooms[len(rooms)-1].desc)
        
    #for i in range(0, len(rooms[len(rooms)-1].choices)):
        #print("\n" + rooms[len(rooms)-1].choices[i]) 
    
    ##Assign Start Room##

    startRoom = rooms[0]
    
    ##Creating the Game##
    
    newGame = game(name, rooms, startRoom)
    print("\nGame created!")

    return newGame


def gameLoop(newGame):

    loopCount = 0
    
    while newGame.currRoom.left != None:
        
        print("\nYou find yourself " + newGame.currRoom.name + ". " + newGame.currRoom.desc)

        #for i in range(0,3):
            
        
        #print("\n\nWhat do you do? (a,b, or c)")
        
        if loopCount == 0:
            print("\nLeaving the starting room, you arrive at a fork in the road (a crossroads, not a piece of silverwear). You can proceed left or right.")
        else:
            print("\nFollowing your success you arrive at a fork in the road (a crossroads, not a piece of silverwear). You can proceed left or right.")
        
        direction = " "
        
        while direction.lower() not in ["right", "left"]:  
            direction = input("\nWhich way? ('left' or 'right')\n")

        if direction.lower() == "left":
            newGame.currRoom = newGame.currRoom.left
        elif direction.lower() == "right":
            newGame.currRoom = newGame.currRoom.right

        loopCount = loopCount + 1
            
    print("\n\nYou find yourself " + newGame.currRoom.name + ". " + newGame.currRoom.desc)

