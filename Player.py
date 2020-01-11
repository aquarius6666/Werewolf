
ALIVE = "Alive"
DEAD  = "Dead"



def Wolf():
    return "Wolf"

def Villager():
    return "Villager"

class Player:

    def __init__(self, name, id):
        
        self.name = name
        self.index = id
        self.status = ALIVE
        
    def drawCard(self, card):

        self.card = card
        self.card_name = card()
    



