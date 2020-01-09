from Player import Player, Wolf, Villager
from random import choice
class Game_board(): 

    def __init__(self, num):
        
        self.numPlayer = num
        self.nWolf = self.numPlayer // 3
        self.nVillager = self.numPlayer - self.nWolf
        self.list = [Wolf] * self.nWolf + [Villager] * self.nVillager
        self.p = []

    def initPlayer(self, player):
        tempCard = choice(self.list)
        self.list.remove(tempCard)
        player.drawCard(tempCard)
        self.p.append(player)