import tkinter as tk
from Player import Player, Wolf, Villager

class BorderFrame(tk.Frame):

    def __init__(self, root, column, row):

        self = tk.Frame(root, relief = tk.RAISED, borderwidth = 3)
       # self.grid(column = column, row = row, padx = 3, pady = 3)
        self.pack(side = tk.LEFT)
        
    def print(self, tempPlayer):

        nameText = str(tempPlayer.index + 1) + ". " + tempPlayer.name
        self.nameLbl = tk.Label(self, text = nameText, width = 9, fg = "blue")
        self.nameLbl.pack(side = tk.TOP)

        statusText = tempPlayer.status
        self.statusLbl = tk.Label(self, text = statusText)
        self.statusLbl.pack(side = tk.TOP)


        cardNameText = tempPlayer.card_name
        self.cardNameLbl = tk.Label(self, text = cardNameText)
        self.cardNameLbl.pack(side = tk.TOP)


