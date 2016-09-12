# Room Class for Text-Based Game
# Matthew Meehan
# September 9, 2016
# Each Room object will have a name, a description, a left and right path, and several choices.

class room:
    def __init__(self, name, desc, choices, left, right):
        self.name = name
        self.desc = desc
        self.choices = choices
        self.left = left
        self.right = right
        
def roomSetup(roomIndex):
    #Takes a list of room information tuples in their desired order
    
    rooms = []
    choices = []

    for roomInfo in roomIndex:
        rooms.append(room(roomInfo[0], roomInfo[1], choices, None, None))
        
    return rooms

def roomRouting(rooms):
    #Takes the list of rooms, assigns left and right for each room.
    #Could possibly create a pattern for routing the rooms if expansion is desired.
    
    rooms[0].left = rooms[1]
    rooms[0].right = rooms[2]
    
    rooms[1].left = rooms[3]
    rooms[1].right = rooms[4]

    rooms[2].left = rooms[4]
    rooms[2].right = rooms[5]

    rooms[3].left = rooms[7]
    rooms[3].right = rooms[6]

    rooms[4].left = rooms[6]
    rooms[4].right = rooms[7]

    rooms[5].left = rooms[7]
    rooms[5].right = rooms[6]

    rooms[6].left = rooms[8]
    rooms[6].right = rooms[8]

    rooms[7].left = rooms[8]
    rooms[7].right = rooms[8]

    rooms[8].left = None
    rooms[8].right = None

    return rooms
