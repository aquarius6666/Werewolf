from tkinter import Tk, Label, Entry, Button


class Application:

    def __init__(self,root):

        self.root = root
        self.root.title("Board game: WereWolf")
        self.root.geometry('400x300')

    def Welcome(self):
        ## Welcome label
        self.wel_lb = Label(self.root, text = "Welcome to my App", \
                                    font = ("Arial Bold", 20))
        self.wel_lb.grid(column = 0, row = 0)

    def inNumPlayer(self):
        ##input number player
        self.num = Entry(self.root, width = 6)
        self.num.grid(column = 1, row = 1)
        stm = Label(self.root, text = "Nhập số lượng người chơi: ")
        stm.grid(column = 0, row = 1)
        self.numPlayer = 0
        btn = Button(self.root, text = "Enter", command = \
                                self.inNumPlayerButton_clicked)
        btn.grid(column = 2, row = 1)
        btn.destroy()
        stm.destroy()
        self.num.destroy()

    def init_game_board(self):

        self.name = ""
        stm = Label(self.root, text = "Nhập tên player: ")
        stm.grid(column = 0, row = 1)
        self.entryName = Entry(self.root, width = 12)
        self.entryName.grid(column = 1, row = 1)
        btn = Button(self.root, text = "Enter", command = self.inName_clicked)
        btn.grid(column = 2, row = 1)
        self.gb = Game_board(self.numPlayer)
        for i in range(0,self.numPlayer):
            lbl = self.gb.init_player(self.name, i)
            lbl = "You are " + lbl
            stmCard = Label(self.root,text = lbl)
            stmCard.grid(column = 0, row = 2)
            stmCard.destroy()


    def inName_clicked(self):
        self.name = self.entryName.get()
    def inNumPlayerButton_clicked(self):
        self.numPlayer = self.num.get()





root = Tk()
app = Application(root)
app.Welcome()
app.inNumPlayer()
##app.init_game_board()
app.root.mainloop()
