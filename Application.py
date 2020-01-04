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

        self.entry = tk.Entry(self.inNumPlayerFrame, width = 5, takefocus = True)
        self.entry.pack(side = tk.LEFT)
        self.entry.bind("<Return>", self.inNumPlayerCF)


    def inNamePlayer(self):
        self.inNamePlayerFrame = tk.Frame(self)
        self.inNamePlayerFrame.pack()

        self.entryNameLabel = tk.Label(self.inNamePlayerFrame, text = "Nhập tên người chơi:")
        self.entryNameLabel.pack(side = tk.LEFT)

        self.entryName = tk.Entry(self.inNamePlayerFrame, width = 7, takefocus = True)
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

        self.playerFrame = [None]
        self.playerFrameLoop = 0
        self.analyzeNumPlayer()
    
        print(self.horizontal)
        print(self.vertical)

    def initPlayerFrame(self, col, row):

        temp = tk.Frame(self)
        label = tk.Label(temp, text = "Nothing")
        label.pack()
        temp.grid(column = col, row = row)
        self.playerFrame.append(temp)


    def analyzeNumPlayer(self):

        temp = (self.numPlayer - 4) // 4 
        self.horizontal = temp + 1 + 2
        self.vertical = temp - 1 - 2

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