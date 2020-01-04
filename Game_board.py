
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

