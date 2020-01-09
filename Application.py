import tkinter as tk 
from Game_board import Game_board
from Player import Player


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title("GameBoard: WereWolf")
        
        self.welcome()
#-----------------------------------------------------------------
    def welcome(self):

        self.welcomeFrame = tk.Frame(self)
        self.welcomeFrame.pack()

        self.welcomeLbl = tk.Label(self.welcomeFrame, text = "Welcome to game")
        self.welcomeLbl.pack(side = tk.TOP)

        self.numPlayerLbl = tk.Label(self.welcomeFrame, text = "Nhập số người chơi")
        self.numPlayerLbl.pack(side = tk.LEFT)

        self.numPlayerEntry = tk.Entry(self.welcomeFrame, width = 3)
        self.numPlayerEntry.pack(side = tk.LEFT)
        self.numPlayerEntry.bind("<Return>", self.numPlayerEvent)
        self.numPlayerEntry.focus()
    

    def readNamePlayer(self):

        self.readNamePlayerLoop = 0
        self.readName()

    def board(self):

        self.boardFrame = tk.Frame(self)
        self.boardFrame.pack()

        self.listBorderFrame = [None] * self.numPlayer

        index = 0

        self.borderPlayer(1,1,index)

        

    


    def borderPlayer(self, col, row, index):
        tempPlayer = self.gb.p[index]

        borderFrame = tk.Frame(self.boardFrame)
        borderFrame.grid(column = col, row = row)

        nameLbl = tk.Label(borderFrame, text = tempPlayer.name, width = 9)
        nameLbl.pack(side = tk.TOP)
        cardNameLbl = tk.Label(borderFrame, text = tempPlayer.card_name, width = 9)
        cardNameLbl.pack(side = tk.TOP)

        self.listBorderFrame[index] = borderFrame





    def readName(self):

        self.readNamePlayerFrame = tk.Frame(self)
        self.readNamePlayerFrame.pack()

        self.readNameLbl = tk.Label(self.readNamePlayerFrame, text = "Nhập tên người chơi")
        self.readNameLbl.pack(side = tk.LEFT)

        self.readNameEntry = tk.Entry(self.readNamePlayerFrame, width = 10)
        self.readNameEntry.pack(side = tk.LEFT)
        self.readNameEntry.bind("<Return>", self.readNameEvent)
        self.readNameEntry.focus()



    def readNameEvent(self, event):

        name = self.readNameEntry.get()
        player = Player(name, self.readNamePlayerLoop)
        self.readNameEntry.configure(state = tk.DISABLED)

        self.gb.initPlayer(player)
        self.cardPrintLbl = tk.Label(self.readNamePlayerFrame, text = self.gb.p[self.readNamePlayerLoop].card_name)
        self.cardPrintLbl.pack(side = tk.LEFT)

        self.readNamePlayerLoop += 1
        self.readNameBtn = tk.Button(self.readNamePlayerFrame, text = "Tiếp tục", command = self.readNameBtnEvent)
        self.readNameBtn.pack(side = tk.LEFT)

    
    def readNameBtnEvent(self):

        self.readNamePlayerFrame.destroy()
        
        if (self.readNamePlayerLoop < self.numPlayer):
            self.readName()

        self.board()



    def numPlayerEvent(self, event):

        self.numPlayer = int(self.numPlayerEntry.get())
        self.gb = Game_board(self.numPlayer)

        self.welcomeFrame.destroy()
        self.readNamePlayer()



app = Application()

app.mainloop()