import tkinter as tk
from PIL import Image, ImageTk

class app(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.img = ImageTk.PhotoImage(Image.open("bg.jpg"))

        self.ca = tk.Canvas(self, height = 400, width = 400)
        self.ca.create_image(0,0,image = self.img)
        self.ca.pack()


        self.lbl = tk.Label(self, image = self.img)
        self.lbl.pack()





a = app()
a.mainloop()