import tkinter as tk
from Player import *



class BorderFrame(tk.Frame):

    def __init__(self, master, col, row, player):

        tk.Frame.__init__(self, master, relief = tk.RAISED, borderwidth = 3)
        self.grid(column = col, row = row, padx = 3, pady = 3)
        self.player = player

        self.print()

    def print(self):

        nameText = str(self.player.index + 1) + ". " + self.player.name
        self.nameLbl = tk.Label(self, text = nameText, width = 9, fg = "blue")
        self.nameLbl.grid(row = 1)

        self.statusText = self.player.status
        self.statusLbl = tk.Label(self, text = self.statusText)
        self.statusLbl.grid(row = 2)
        self.statusLbl.grid_remove()

        self.cardNameText = self.player.card_name
        self.cardNameLbl = tk.Label(self, text = self.cardNameText)
        self.cardNameLbl.grid(row = 3)
        self.cardNameLbl.grid_remove()
        self.card = self.player.card

    def update(self):

        self.nameText = str(self.player.index + 1) + ". " + self.player.name
        self.nameLbl.config(text = self.nameText)

        self.statusText = self.player.status
        self.statusLbl.config(text = self.statusText)

        self.cardNameText = self.player.card_name
        self.cardNameLbl.config(text = self.cardNameText)
        
        self.card = self.player.card

        if self.statusText == DEAD:
            self.statusLbl.config(fg = "red")
            self.cardNameLbl.config(fg = "red")

    def show(self, sth):

        self.update()
        if sth == None:
            self.cardNameLbl.grid()
            self.statusLbl.grid()
            return
        if sth == self.player.card:
            self.cardNameLbl.grid()
            return
        elif sth == self.player.status:
            self.statusLbl.grid()
            return
        


    def hide(self, sth = None):
        if sth:
            if sth == self.card:
                self.cardNameLbl.grid_remove()
        
            if sth == self.statusText:
                self.statusLbl.grid_remove()
        else:
            self.cardNameLbl.grid_remove()
            self.statusLbl.grid_remove()
            

        

