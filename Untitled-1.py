from tkinter import *

a = Tk()


lbl = Label(a, text = "1")
lbl.pack()

def clicked():
    lbl.pack_forget()

btn = Button(a, text = "12", command = clicked)
btn.pack()


a.mainloop()