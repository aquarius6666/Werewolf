from Player import *
from random import choice

class Game_board(): 

    def __init__(self, num):
        
        self.numPlayer = num
        self.nBodyguard = 0
        self.nSeer = 0
        self.nWizzard = 0
        
        self.nWolf = self.numPlayer // 3
        if self.numPlayer >= 6:
            self.nBodyguard = 1
        if self.numPlayer >= 7:
            self.nSeer = 1
        if self.numPlayer >= 8:
            self.nWizzard = 1
        self.nVillager = self.numPlayer - self.nWolf - self.nBodyguard - self.nWizzard - self.nSeer

        self.list = [Wolf] * self.nWolf + [Villager] * self.nVillager + [Bodyguard] * self.nBodyguard + [Wizzard] * self.nWizzard + [Seer] * self.nSeer
        self.p = []
        print(self.list)

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
