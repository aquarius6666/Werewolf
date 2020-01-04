from Game_board import Game_board, Wolf, Villager
import tkinter as tk

class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(*args, **kwargs)

        #Frame
        self.mainFrame = tk.Frame(self)
        self.mainFrame.pack()

        self.entryLabel = tk.Label(self.mainFrame, text="Nhập số player")
        self.entryLabel.pack(side=tk.LEFT)

        self.entryBox=tk.Entry(self.mainFrame)
        self.entryBox.pack(side=tk.LEFT)

        self.entryButton=tk.Button(self.mainFrame, text="Enter", command=##)
        self.entryButton.pack(side=tk.LEFT)


app = Application()
app.mainloop()



