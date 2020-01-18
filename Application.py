import tkinter as tk 
from Game_board import Game_board
from Player import *
from PIL import Image, ImageTk
from BorderFrame import BorderFrame
from math import sqrt, floor, ceil




class Application(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title("GameBoard: WereWolf")
        self.geometry('+600+200')
        self.welcome()
#-----------------------------------------------------------------
    def welcome(self):

        self.image = ImageTk.PhotoImage(Image.open("bg.jpg"))
        self.WelCanvas = tk.Canvas(self, height = 170, width = 225)
        self.WelCanvas.create_image(0, 0, image = self.image, anchor = tk.NW)
        self.WelCanvas.pack()



        self.welcomeFrame = tk.Frame(self)
        self.welcomeFrame.pack()

    #    self.welcomeLbl = tk.Label(self.welcomeFrame, text = "Welcome to game", font = ('40'), fg = "red")
    #   self.welcomeLbl.pack(side = tk.TOP, padx = 5, pady = 5)

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
            if index >= self.numPlayer:
                break
            index += 1
        
        for i in range (self.vertical - 2, 0, -1):
            if index >= self.numPlayer:
                break
            self.borderPlayer(0, i, index)
            index += 1

        self.currTime()
        self.dayFrame = tk.Frame(self)
   
    def currTime(self):

        self.currTimeFrame = tk.Frame(self)
        self.currTimeFrame.pack()

        self.currTimeText = "Current: "
        self.currTimeLbl = tk.Label(self.currTimeFrame, text = self.currTimeText)
        self.currTimeLbl.pack()

        self.nightTime()

    def nightTime(self):

        self.currTimeLbl.config(text = self.currTimeText + "Night")

        self.show(DEAD)
        self.nightFrame = tk.Frame(self)
        self.nightFrame.pack()

        self.nightBtns = tk.Frame(self.nightFrame)
        self.nightBtns.pack(side = tk.TOP)

        self.wolfButton = tk.Button(self.nightBtns, text = "Wolf", command = self.WolfTime)
        self.wolfButton.bind("<Return>", self.WolfTime)
        self.wolfButton.pack(side = tk.LEFT)

        self.bodyquardButton = tk.Button(self.nightBtns, text = "Bodyquard", command = self.BodyQuardTime)
        self.bodyquardButton.bind("<Return>", self.BodyQuardTime)
        self.bodyquardButton.pack(side = tk.LEFT)

        self.dayButton = tk.Button(self.nightBtns, text = "DayTime", command = self.dayTime)
        self.dayButton.bind("<Return>", self.dayTime)
        self.dayButton.pack(side = tk.LEFT)



    def dayTime(self, event = None):

        self.nightFrame.destroy()
        self.currTimeLbl.config(text = self.currTimeText + "Day")

        self.preday()
        self.show(DEAD)
        self.dayFrame = tk.Frame(self)
        self.dayFrame.pack()

        self.dayBtns = tk.Frame(self.dayFrame)
        self.dayBtns.pack()
        
        self.voteButton = tk.Button(self.dayBtns, text = "Vote", command = self.Vote)
        self.voteButton.bind("<Return>", self.Vote)
        self.voteButton.pack()
        
        self.dayMsg = tk.Frame(self.dayFrame)
        self.dayMsg.pack()

    def Vote(self, event = None):

        self.voteButton.config(state = tk.DISABLED)

        self.voteLbl = tk.Label(self.dayMsg, text = "Chọn treo cổ 1 người")
        self.voteLbl.pack(side = tk.LEFT)

        self.voteEntry = tk.Entry(self.dayMsg, width = 2)
        self.voteEntry.focus()
        self.voteEntry.pack(side = tk.LEFT)
        self.voteEntry.bind("<Return>", self.voteEntryEvent)

    def voteEntryEvent(self, event):

        target = int(self.voteEntry.get())
        target -= 1
        self.gb.p[target].update(DEAD)
        
        
        self.dayFrame.destroy()
        self.nightTime()


    def BodyQuardTime(self, event = None):

        self.show(Bodyguard)
        self.bodyquardButton.config(state = tk.DISABLED)

        self.bodyquardFrame = tk.Frame(self.nightFrame)
        self.bodyquardFrame.pack(side = tk.TOP, padx = 2, pady = 2)

        self.bodyquardLbl = tk.Label(self.bodyquardFrame, text = "Bảo vệ chọn 1 người để bảo vệ")
        self.bodyquardLbl.grid(row = 2, column = 1)

        self.bodyquardEntry = tk.Entry(self.bodyquardFrame, width = 2)
        self.bodyquardEntry.focus()
        self.bodyquardEntry.grid(row = 2, column = 2)
        self.bodyquardEntry.bind("<Return>", self.bodyquardEntryEvent)

    def bodyquardEntryEvent(self, event):
        if self.gb.count(Bodyguard):
            target = int(self.bodyquardEntry.get())
            target -= 1
            self.gb.p[target].update(PROTECTED)

        self.bodyquardFrame.destroy()

        self.unshow()
        self.show(DEAD)

    def WolfTime(self, event = None):
        
        self.show(Wolf)
        self.wolfButton.config(state = tk.DISABLED)

        self.wolfFrame = tk.Frame(self.nightFrame)
        self.wolfFrame.pack(side = tk.TOP, padx = 2, pady = 2)

        self.wolfLbl = tk.Label(self.wolfFrame, text = "Sói chọn người để cắn")
        self.wolfLbl.pack(side = tk.LEFT)

        self.wolfEntry = tk.Entry(self.wolfFrame, width = 2)
        self.wolfEntry.focus()
        self.wolfEntry.pack(side = tk.LEFT)
        self.wolfEntry.bind("<Return>", self.wolfEntryEvent)

    def wolfEntryEvent(self, event):

        if self.gb.count(Wolf):
            target = int(self.wolfEntry.get())
            target -= 1
            self.gb.p[target].update(ATTACKED)
            
        self.wolfFrame.destroy()

        self.unshow()
        self.show(DEAD)


    def preday(self):
        for i in range(0, self.numPlayer):
            if self.gb.p[i].status == ATTACKED:
                self.gb.p[i].status = DEAD

    def unshow(self):
        for i in range(0, self.numPlayer):
            self.borderFrames[i].hide()
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

        self.readNameLoad = Image.open("draw_card.gif")
        self.readNameCanvas = tk.Canvas(self.readNamePlayerFrame, width = self.readNameLoad.width, height = self.readNameLoad.height)
        self.readNameImg = ImageTk.PhotoImage(self.readNameLoad)
        self.readNameCanvas.create_image(0,0, image = self.readNameImg, anchor = tk.NW)
        self.readNameCanvas.pack()

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
        self.readNameBtn.bind("<Return>", self.readNameBtnEvent)
        self.readNameBtn.pack(side = tk.LEFT)

    
    def readNameBtnEvent(self, event = None):

        self.readNamePlayerFrame.destroy()

        if (self.readNamePlayerLoop < self.numPlayer):
            self.readName()
        else:
            self.board()



    def numPlayerEvent(self, event):
        self.WelCanvas.destroy()
        self.numPlayer = int(self.numPlayerEntry.get())
        self.gb = Game_board(self.numPlayer)

        self.welcomeFrame.destroy()
        self.readNamePlayer()

