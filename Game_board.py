from Player import *
from random import choice

class Game_board(): 

    def __init__(self, num):
        
        self.numPlayer = num
        self.nWolf = self.numPlayer // 3

        self.nBodyquard = 1
        self.nWizzard = 1

        self.nVillager = self.numPlayer - self.nWolf - self.nBodyquard - self.nWizzard

        self.list = [Wolf] * self.nWolf + [Villager] * self.nVillager + [Bodyguard] * self.nBodyquard + [Wizzard] * self.nWizzard
        self.p = []

    def initPlayer(self, player):
        tempCard = choice(self.list)
        self.list.remove(tempCard)
        player.drawCard(tempCard)
        self.p.append(player)

    def count(self, card):
        c = 0
        for p in self.p:
            if p.isSth(card):
                c += 1

        return c

    def isEndGame(self):
        nAlive = self.count(ALIVE)
        nWolfAlive = self.count(Wolf)
        nNonWolfAlive = nAlive - nWolfAlive

        if nWolfAlive == 0:
            self.winner = Villager()
            return True

        if nNonWolfAlive <= nWolfAlive:
            self.winner = Wolf()
            return True
        
        
        return False
