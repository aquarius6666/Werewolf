
ALIVE = "Alive"
DEAD  = "Dead"
ATTACKED = "Attacked"
PROTECTED = "Protected"

def Bodyguard():
    return "Bodyquard"

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

    def update(self, sth):

        if type(sth) == type(self.status):
            if self.status == PROTECTED and sth == ATTACKED:
                return 
            self.status = sth

        elif type(sth) == type(self.card):
            self.card = sth
            self.card_name = self.card()
        
    



