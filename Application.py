import tkinter as tk 
from Game_board import Game_board
from Player import Player, Wolf, Villager
from BorderFrame import BorderFrame
from math import sqrt, floor, ceil

ALIVE = "Alive"
DEAD  = "Dead"





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

        self.borderFrames = []

        index = 0
        self.findHozVer()
 
        for i in range (0, self.horizontal):
            self.borderPlayer(i, 0, index)
            index += 1
        
        for i in range (1, self.vertical - 1):
            self.borderPlayer(self.horizontal - 1, i, index)
            index += 1

        for i in range(self.horizontal - 1, -1, -1):
            self.borderPlayer(i, self.vertical - 1, index)
            index += 1
        
        for i in range (self.vertical - 2, 0, -1):
            self.borderPlayer(0, i, index)
            index += 1

        self.currTime()
   
    def currTime(self):

        self.currTimeFrame = tk.Frame(self)
        self.currTimeFrame.pack()

        self.currTimeText = "Current: "
        self.currTimeLbl = tk.Label(self.currTimeFrame, text = self.currTimeText)
        self.currTimeLbl.pack()

        self.nightTime()


    def nightTime(self):
        
        self.currTimeLbl.config(text = self.currTimeText + "Night")

        self.nightFrame = tk.Frame(self)
        self.nightFrame.pack()

        self.wolfButton = tk.Button(self.nightFrame, text = "Wolf", command = self.WolfTime)
        self.wolfButton.grid(row = 1, column = 1)


    def dayTime(self):

        self.currTimeLbl.config(text = self.currTimeText + "Day")

        self.dayFrame = tk.Frame(self)
        self.dayFrame.pack()

        self.voteButton = tk.Button(self.dayFrame, text = "Vote", command = self.Vote)
        self.voteButton.grid(row = 1, column = 1)

    def Vote(self):

        self.voteLbl = tk.Label(self.dayFrame, text = "Chọn treo cổ 1 người")
        self.voteLbl.grid(row = 2, column = 1)

        self.voteEntry = tk.Entry(self.dayFrame, width = 2)
        self.voteEntry.grid(row = 2, column = 2)
        self.voteEntry.bind("<Return>", self.voteEntryEvent)

    def voteEntryEvent(self):

        target = int(self.voteEntry.get())
        target -= 1
        self.gb.p[target].update(DEAD)
        
        self.dayFrame.destroy()
        self.nightTime()

    def WolfTime(self):
        
        self.show(Wolf)

        self.wolfFrame = tk.Frame(self.nightFrame)
        self.wolfFrame.pack()

        self.wolfLbl = tk.Label(self.wolfFrame, text = "Sói chọn người để cắn")
        self.wolfLbl.grid(row = 2, column = 1)

        self.wolfEntry = tk.Entry(self.wolfFrame, width = 2)
        self.wolfEntry.grid(row = 2, column = 2)
        self.wolfEntry.bind("<Return>", self.wolfEntryEvent)

    def wolfEntryEvent(self, event):

        target = int(self.wolfEntry.get())
        target -= 1
        self.gb.p[target].update(DEAD)
        
        self.wolfFrame.destroy()



    def show(self, sth):

        for i in range(0, self.numPlayer):
            self.borderFrames[i].show(sth)

    def findHozVer(self):

        temp = self.numPlayer + 4
        divTemp = ceil(temp/4)

        self.vertical = divTemp
        self.horizontal = ceil(temp/2) - divTemp
        
    
    def borderPlayer(self, col, row, index):

        borderFrame = BorderFrame(self.boardFrame, col, row, self.gb.p[index])

        self.borderFrames.append(borderFrame)

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
        else:
            self.board()



    def numPlayerEvent(self, event):

        self.numPlayer = int(self.numPlayerEntry.get())
        self.gb = Game_board(self.numPlayer)

        self.welcomeFrame.destroy()
        self.readNamePlayer()



app = Application()

app.mainloop()