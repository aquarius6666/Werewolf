from PIL import ImageTk, Image
import tkinter as tk
a = tk.Tk()
load = Image.open("C:\\Users\\Anhtu\\Desktop\\Project\\pic\\bg.jpg")
load = load.resize((300,600),Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = tk.Label(a, image = render)
img.place(x= 0, y = 0, relwidth = 1, relheight = 1)
lbl = tk.Label(a, text = "a")
lbl.place(x = 1, y = 1)
a.mainloop()
