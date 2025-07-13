from tkinter import *
import subprocess
import sys

import pygame
pygame.mixer.init()


def launch_game(difficulty):
    subprocess.Popen([sys.executable, "tictactoe.py", difficulty])
    dif.destroy()

dif=Tk()
dif.title("Tic-Tac-Toe!")

dif.configure(bg="#1e1e1e")

diflabel=Label(text="Chose Your Difficulty",font=("Helvetica",30),bg="#1e1e1e", fg="#f0f0f0")
diflabel.pack(side="top",padx=50)

difframe=Frame(dif,bg="#1e1e1e")
difframe.pack(pady=50)

easy=Button(difframe,text="     Easy     ",font=('Helvetica',20), bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444", 
           activeforeground="#ffffff",command=lambda: launch_game("Easy"))
hard=Button(difframe,text="     Hard     ",font=('Helvetica',20), bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444", 
           activeforeground="#ffffff",command=lambda: launch_game("Hard"))
unbeatable=Button(difframe,text="Unbeatable",font=('Helvetica',20), bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444", 
           activeforeground="#ffffff",command=lambda: launch_game("Unbeatable"))
easy.pack(pady=2)
hard.pack(pady=2)
unbeatable.pack(pady=2)


dif.mainloop()

