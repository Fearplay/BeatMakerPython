import tkinter as tk
from pygame import mixer
mixer.init()

win = tk.Tk()
win.title("BeatMaker")
win.geometry("450x50")

def song1():
    mixer.music.load("songs/beat1.mp3")
    mixer.music.play()

def song2():
    mixer.music.load("songs/beat3.mp3")
    mixer.music.play()

def song3():
    mixer.music.load("songs/beat2.mp3")
    mixer.music.play()

def song4():
    mixer.music.load("songs/beat4.mp3")
    mixer.music.play()

def song5():
    mixer.music.load("songs/beat5.mp3")
    mixer.music.play()

def song6():
    mixer.music.load("songs/beat6.mp3")
    mixer.music.play()


song1 = tk.Button(win, bg='blue2',width = 20, command = song1)
song1.grid(row = 1, column = 1)

song2 = tk.Button(win, bg='green2',width = 20, command = song2)
song2.grid(row = 1, column = 2)

song3 = tk.Button(win, bg='red2',width = 20, command = song3)
song3.grid(row = 1, column = 3)

song4 = tk.Button(win, bg='yellow2',width = 20, command = song4)
song4.grid(row = 2, column = 1)

song5 = tk.Button(win, bg='gray2',width = 20, command = song5)
song5.grid(row = 2, column = 2)

song6 = tk.Button(win, bg='purple2',width = 20, command = song6)
song6.grid(row = 2, column = 3)



win.mainloop()