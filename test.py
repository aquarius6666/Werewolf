from tkinter import *
from PIL import Image, ImageTk
# create the canvas, size in pixels
canvas = Canvas(width=300, height=200, bg='black')

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

# load the .gif image file
gif1 = ImageTk.PhotoImage(Image.open("C:\\Users\\Anhtu\\Desktop\\Project\\pic\\bg.jpg"))

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image=gif1, anchor = NW)
label = Label(canvas, text = "test", width = 300, height = 200)
label.pack()

# run it ...
mainloop()