import tkinter as tk

from Game_board import Game_board

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
        cardPlayer = self.gb.getCardNameIndex(self.entryNameLoop)
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
        self.boardBgImage = tk.PhotoImage(file = r"C:\Users\Anhtu\Desktop\Project\pic\bg.jpg")
        self.boardBg = tk.Label(self.boardFrame, image = self.boardBgImage)
        self.boardFrame.pack()
        self.playerFrame = [None] * self.numPlayer
        self.playerFrameLoop = 0
        self.analyzeNumPlayer()
        self.nameLabel = [None] * self.numPlayer
        self.cardLabel = [None] * self.numPlayer
        self.statusLabel = [None] * self.numPlayer
        self.playerFrames = [None] * self.numPlayer

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
        
    def initPlayerFrame(self, col, row, index, fg_name = "red", fg_card = "blue", fg_status = "green"):
        _player = self.gb.p[index]

        _frame = tk.Frame(self.boardFrame, borderwidth=3, relief = tk.RAISED)
        self.playerFrames[index] = _frame

        _nameLabel = tk.Label(_frame, text = _player.name, fg = fg_name, font = ("bold", 11), width = 9)
        _nameLabel.pack(side = tk.TOP)
        self.nameLabel[index] = _nameLabel

        _cardLabel = tk.Label(_frame, text = _player.card_name, fg = fg_card, width = 9)
        _cardLabel.pack(side = tk.TOP)
        self.cardLabel[index] = _cardLabel

        _statusLabel = tk.Label(_frame, text = _player.status, fg = fg_status, width = 9)
        _statusLabel.pack(side = tk.TOP)
        self.statusLabel[index] = _statusLabel

        _frame.grid(column = col, row = row)
        self.playerFrame[index] = _frame


    def analyzeNumPlayer(self):

        temp = (self.numPlayer - 4) / 4
        if temp >int(temp):
            temp = int(temp) + 1 
        self.horizontal = temp + 1 + 2
        self.vertical = temp - 1

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