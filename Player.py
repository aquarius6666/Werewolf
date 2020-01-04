
def Wolf():
    pass

def Villager():
    pass

## status

ALIVE = "Alive"
DEAD = "Dead"

class Player:

    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.status = ALIVE
    
    def draw_card(self, card):
        self.card = card
        if self.card == Villager:
            self.card_name = "Villager"
        if self.card == Wolf:
            self.card_name = "Wolf"
        
    

