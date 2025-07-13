from tkinter import *
import subprocess
import sys
import pygame
pygame.mixer.init()

def start_two_player(difficulty):
    menuclick.play()
    main.after(500, main.destroy)    
    pygame.mixer.music.stop()
    subprocess.Popen(["python","tictactoe.py",difficulty])

def start_single_player():
    menuclick.play()
    main.destroy()
    subprocess.run([sys.executable,"difficultymenu.py"])
def exit():
    menuclick.play()
    main.after(500,lambda: main.destroy())

menuclick=pygame.mixer.Sound("Sounds/menu_click.mp3")
pygame.mixer.music.load("Sounds/menu_soundtrack.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

main=Tk()
main.title("Tic-Tac-Toe!")

mainlabel=Label(text="Tic-Tac-Toe!",font=("Helvetica",50),bg="#1e1e1e", fg="#f0f0f0")
mainlabel.pack(side="top")

mainframe=Frame(main,bg="#1e1e1e")
mainframe.pack(pady=50)
main.configure(bg="#1e1e1e")

two=Button(mainframe,text="  Two  Player  ",font=('Helvetica',20), bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444", 
           activeforeground="#ffffff",command=lambda: start_two_player("2p"))
two.pack(pady=2)

single=Button(mainframe,text=" Single Player ",font=('Helvetica',20), bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444", 
              activeforeground="#ffffff",command=start_single_player)
single.pack(pady=2)

exit=Button(mainframe,text="        Quit\t       ",font=('Helvetica',20), bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444",
             activeforeground="#ffffff",command=exit)
exit.pack(pady=2)


main.mainloop()