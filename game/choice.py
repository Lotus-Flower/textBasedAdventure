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

    for i in range(0, len(choiceIndex)):
        rooms[i+1].choices = choiceIndex[i]
    return rooms

    
