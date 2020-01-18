import tkinter as tk
from PIL import Image, ImageTk

class app(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.img = Image.open("bg.jpg")
        print (self.img.width)
       # self.lbl = tk.Label(self, image = self.img)
       # self.lbl.pack()





a = app()
a.mainloop()