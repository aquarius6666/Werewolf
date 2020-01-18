import pygame
from tkinter import *
root = Tk()

def play():
    pygame.mixer.music.load("wolf_sound.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
Button(root,text="Play",command=play).pack()
root.mainloop()