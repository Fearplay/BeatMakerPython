import tkinter as tk
from pygame import mixer
import random

mixer.init()

win = tk.Tk()
win.title("BeatMaker")
win.geometry("450x50")

def load_song():
    id = random.randrange(1,6)
    mixer.music.load(f"songs/beat{id}.mp3")
    mixer.music.play()

colors = ['blue2','green2','red2','yellow2','gray2','purple2']
color = random.choices(colors)

button = list()
for i in range(3):
    for j in range(2):
        button.append(tk.Button(win, bg=color,width = 20, command = load_song))
        button[-1].grid(row=j,column=i)

win.mainloop()