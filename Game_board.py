
from Player import Player, Wolf, Villager
from random import choice
class Game_board():

    def __init__(self, num):
        self.numPlayer = num
        self.p = [None] * self.numPlayer
        self.nWolfCard = num // 3
        self.nVillagerCard = num - self.nWolfCard
        self.listCard = [Wolf] * self.nWolfCard + [Villager] * self.nVillagerCard

    def initPlayer(self, name, index):
        tempPlayer = Player(name, index)
        temp = choice(self.listCard)
        tempPlayer.draw_card(temp)
        self.listCard.remove(temp)
        self.p[index] = tempPlayer

    def getNameIndex(self, index):
        return self.p[index].name
    
    def getCardNameIndex(self, index):
        if self.p[index].card == Wolf:
            self.p[index].card_name = "Wolf"
        if self.p[index].card == Villager:
            self.p[index].card_name = "Villager"
        return self.p[index].card_name
    