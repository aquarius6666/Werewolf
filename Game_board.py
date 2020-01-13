from Player import *
from random import choice

class Game_board(): 

    def __init__(self, num):
        
        self.numPlayer = num
        self.nWolf = self.numPlayer // 3
        self.nBodyquard = 1
        self.nVillager = self.numPlayer - self.nWolf - self.nBodyquard
        self.list = [Wolf] * self.nWolf + [Villager] * self.nVillager + [Bodyguard] * self.nBodyquard
        self.p = []

    def initPlayer(self, player):
        tempCard = choice(self.list)
        self.list.remove(tempCard)
        player.drawCard(tempCard)
        self.p.append(player)