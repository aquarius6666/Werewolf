import tkinter as tk
from Game_board import Game_board

DEAD = "Dead"
ALIVE = "Alive"

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Game: WereWolf")
        self.inNumPlayer()


    def inNumPlayer(self):
        
        self.inNumPlayerFrame = tk.Frame(self)
        self.inNumPlayerFrame.pack()

        self.entryLabel = tk.Label(self.inNumPlayerFrame, text = "Nhập số lượng người chơi:")
        self.entryLabel.pack(side = tk.LEFT)

        self.entry = tk.Entry(self.inNumPlayerFrame, width = 5)
        self.entry.focus()
        self.entry.pack(side = tk.LEFT)
        self.entry.bind("<Return>", self.inNumPlayerCF)


    def inNamePlayer(self):
        self.inNamePlayerFrame = tk.Frame(self)
        self.inNamePlayerFrame.pack()

        self.entryNameLabel = tk.Label(self.inNamePlayerFrame, text = "Nhập tên người chơi:")
        self.entryNameLabel.pack(side = tk.LEFT)

        self.entryName = tk.Entry(self.inNamePlayerFrame, width = 7)
        self.entryName.focus()
        self.entryName.pack(side = tk.LEFT)
        self.entryName.bind("<Return>", self.inNamePlayerCF)
        self.entryNameLoop = 0



        
    def inNamePlayerCF(self, event):
        namePlayer = self.entryName.get()
        self.gb.initPlayer(namePlayer, self.entryNameLoop)
        cardPlayer = self.gb.p[self.entryNameLoop].card_name
        self.entryNameLoop = self.entryNameLoop + 1
        self.printCardLabel = tk.Label(self.inNamePlayerFrame, text = cardPlayer)
        self.printCardLabel.pack(side = tk.LEFT)
        
        self.newEntryNameButton = tk.Button(self.inNamePlayerFrame, text = "Tiếp tục", command = self.newEntryNameButtonEvent)
        self.newEntryNameButton.pack(side = tk.BOTTOM)


    def StartGame(self):

        self.startGameFrame = tk.Frame(self)
        self.startGameFrame.pack()

        self.startButton = tk.Button(self.startGameFrame, text = "Bắt đầu trò chơi", command = self.startGameEvent)
        self.startButton.pack(side = tk.BOTTOM)

    def Board(self):
        self.boardFrame = tk.Frame(self)
        self.boardFrame.pack()
        self.playerFrame = [None] * self.numPlayer
        self.playerFrameLoop = 0
        self.analyzeNumPlayer()
        self.nameLabel = [None] * self.numPlayer
        self.cardLabel = [None] * self.numPlayer
        self.statusLabel = [None] * self.numPlayer
        self.playerFrames = [None] * self.numPlayer
        self.timeFrame = tk.Frame(self)
        self.timeFrame.pack()
        self.textTimeLabel = "Current: "
        self.timeLabel = tk.Label(self.timeFrame, text = self.textTimeLabel + "Daytime")
        self.timeLabel.pack(side = tk.LEFT)

        loop = 0
        for i in range(0,self.horizontal):
            if (loop < self.numPlayer):
                self.initPlayerFrame(i, 0, loop)
                loop += 1

        for i in range(0, self.vertical):
            if (loop < self.numPlayer):
                self.initPlayerFrame(self.horizontal - 1, i + 1, loop)
                loop += 1
    
        for i in range(self.horizontal - 1, -1 , -1):            
            if (loop < self.numPlayer):
                self.initPlayerFrame(i, self.vertical + 1, loop)
                loop += 1

        for i in range(self.vertical - 1, -1 , -1):
            if (loop < self.numPlayer):
                self.initPlayerFrame(0, i + 1, loop)
                loop += 1
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.pack(side = tk.BOTTOM)
        self.DayTimeButton = tk.Button(self.buttonFrame, text = "Daytime", command = self.DayTime)
        self.DayTimeButton.pack()
    

        
    def initPlayerFrame(self, col, row, index, fg_name = "green"):
        _player = self.gb.p[index]

        _frame = tk.Frame(self.boardFrame, borderwidth=3, relief = tk.RAISED)
        self.playerFrames[index] = _frame
        nameText = str(index+1) + ". " + _player.name
        _nameLabel = tk.Label(_frame, text = nameText, fg = fg_name, font = ("bold", 11), width = 9)
        _nameLabel.pack(side = tk.TOP)
        self.nameLabel[index] = _nameLabel

        _cardLabel = tk.Label(_frame, width = 9)
        _cardLabel.pack(side = tk.TOP)
        self.cardLabel[index] = _cardLabel

        _statusLabel = tk.Label(_frame, width = 9)
        _statusLabel.pack(side = tk.TOP)
        self.statusLabel[index] = _statusLabel

        _frame.grid(column = col, row = row)
        self.playerFrame[index] = _frame

    def dead_man_cant_talk(self):

        for i in range (0, self.numPlayer):
            if (self.gb.p[i].status == DEAD):
                self.statusLabel[i].config(fg = "red", text = DEAD)
                self.nameLabel[i].config(fg = "red")

    def DayTime(self):
        self.timeLabel.config(text = self.textTimeLabel + "Daytime")
        self.dead_man_cant_talk()
        self.voteButton = tk.Button(self.buttonFrame, text = "VOTE", command = self.Vote)
        self.voteButton.pack()

    def Vote(self):
        self.entryVote = tk.Entry(self.buttonFrame, width = 3)
        self.entryVote.pack()
        self.entryVote.bind("<Return>", self.VoteEvent)
    
    def VoteEvent(self, event):
        playerIndex = int(self.entryVote.get())
        playerIndex -= 1
        self.gb.p[playerIndex].status = DEAD
        self.entryVote.destroy()
        self.voteButton.destroy()
        self.Nighttime()

    def Nighttime(self):
        self.timeLabel.config(text = self.textTimeLabel + "Nighttime")
        self.dead_man_cant_talk()

        

    def analyzeNumPlayer(self):

        temp = (self.numPlayer - 4) / 4
        if temp > int(temp):
            temp = int(temp) + 1 
        self.horizontal = int(temp) + 3
        self.vertical = int(temp) - 1

    def startGameEvent(self):
        self.startGameFrame.destroy()
        self.Board()


    def newEntryNameButtonEvent(self):
        self.entryName.delete(0,len(self.entryName.get()))
        self.newEntryNameButton.destroy()
        self.printCardLabel.destroy()
        if self.entryNameLoop == self.numPlayer:
            self.inNamePlayerFrame.destroy()
            self.StartGame()

    def inNumPlayerCF(self, event):
        self.numPlayer = int(self.entry.get())
        self.inNumPlayerFrame.destroy()
        self.gb = Game_board(self.numPlayer)
        self.inNamePlayer()


app = Application()
app.mainloop()