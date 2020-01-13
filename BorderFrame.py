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

    def update(self):

        self.cardNameText = self.player.name
        self.cardNameLbl.config(text = self.cardNameText)

        self.statusText = self.player.status
        self.statusLbl.config(text = self.statusText)

        self.cardNameText = self.player.card_name
        self.cardNameLbl.config(text = self.cardNameText)
        
        if self.statusText == DEAD:
            self.statusLbl.config(fg = "red")
            self.cardNameLbl.config(fg = "red")

    def show(self, sth):

        self.update()
        if sth == self.player.card:
            self.cardNameLbl.grid()
        elif sth == self.player.status:
            self.statusLbl.grid()

    def hide(self):

        self.cardNameLbl.grid_remove()
        self.statusLbl.grid_remove()
