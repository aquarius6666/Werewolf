
ALIVE = "Alive"
DEAD  = "Dead"
ATTACKED = "Attacked"
PROTECTED = "Protected"

def Bodyguard():
    return "Bodyguard"

def Wolf():
    return "Wolf"

def Villager():
    return "Villager"

def Wizzard():
    return "Wizzard"


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
            if (self.status == PROTECTED and sth == ATTACKED) or (self.status == ATTACKED and sth == PROTECTED):
                self.status = PROTECTED
            
            else:
                self.status = sth

        elif type(sth) == type(self.card):
            self.card = sth
            self.card_name = self.card()

    def isSth(self, sth):

        if type(sth) == type(self.card):
            if sth == self.card and self.status == ALIVE:
                return True
            else:
                return False

        elif type(sth) == type(self.status):
            if sth == self.status:
                return True
            else:
                return False

        
    



