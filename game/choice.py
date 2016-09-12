# Choice Class for Text-Based Game
# Matthew Meehan
# September 9, 2016
# Each Choice object will have content, a response, and a value for whether or not it was the correct choice.
# Choices are associated with each Room object.

class choice:
    def __init__(self, content, response, correct):
        self.content = content
        self.response = response
        self.correct = correct

def choicesSetup(rooms, choiceIndex):
    #Takes a list of room objects and a list of tuples of the information for three choices (ordered as desired)
    #Returns a list of rooms with choices assigned
    
    for i in range(0, len(choiceIndex)):
        
        choices = []
        
        for j in range(0, len(choiceIndex[i])):
            
            choices.append(choice(choiceIndex[i][j][0], choiceIndex[i][j][1], False))
            
        rooms[i+1].choices = choices
        
    return rooms

def correctSetup(rooms, correctList):
    for i in range(0, len(correctList)):
        if (i+1) == len(rooms):
            print(rooms[i+1].name)
        else:
            if correctList[i] == "a":
                rooms[i+1].choices[0].correct = True
            elif correctList[i] == "b":
                rooms[i+1].choices[1].correct = True
            elif correctList[i] == "c":
                rooms[i+1].choices[2].correct = True

    return rooms

    
