
def Wolf():
    return "Wolf"

def Villager():
    return "Villager"

class Player:

    def __init__(self, name, id):
        
        self.name = name
        self.index = id
        
    def drawCard(self, card):

        self.card_name = card()
        self.card = card
    



