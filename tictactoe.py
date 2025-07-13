from tkinter import *
from ai_easy import *

import sys

import pygame
pygame.mixer.init()

difficulty = sys.argv[1] if len(sys.argv) > 1 else "2p"
ai_enabled=(difficulty!="2p")
if difficulty=="Easy":
    import ai_easy as ai
if difficulty =="Hard":
    import ai_hard as ai
if difficulty=="Unbeatable":
    import ai_minimax as ai


def score_reset():
    menuclick.play()
    score0=0
    score1=0
    tiescore=0
    score_0.config(text=f"{players[0]}'s Score = {score0}")
    score_1.config(text=f"{players[1]}'s Score = {score1}")
    tie.config(text="Tie Score = "+str(tiescore))

def next_turn(row,column):
    global player,score0,score1,tiescore
    if buttons[row][column]["text"] == "" and check_winner() is False:
        click.play()
        if player == players[0]:
            buttons[row][column]['text']= player
            if  check_winner() is False:
                player = players[1]
                label.config(text=players[1]+"'s turn")
                if ai_enabled and player=="O":
                    window.after(400, lambda:(blip.play(), ai.ai_move(buttons,next_turn)))
            elif check_winner() is True:
                if ai_enabled:
                    score0+=1
                    label.config(text="You Win! 🔥")
                    pygame.mixer.music.pause()
                    win.play()
                else:
                    score0+=1
                    label.config(text=players[0]+" Wins 🔥")
                    pygame.mixer.music.pause()
                    win.play()
            elif check_winner() == 'Tie':
                tiescore+=1
                pygame.mixer.music.pause()
                tie_sound.play()
                label.config(text="Tied 🤝")
                tie.config(text="Tie Score = "+str(tiescore))
        else:
            buttons[row][column]['text']= player
            if  check_winner() is False:
                player = players[0]
                label.config(text=players[0]+"'s turn")
            elif check_winner() is True:
                if ai_enabled:
                    score1+=1
                    label.config(text="You Lose 💔")
                    pygame.mixer.music.pause()
                    lost.play()
                else:
                    score1+=1
                    label.config(text=players[1]+" Wins 🔥")
                    pygame.mixer.music.pause()
                    win.play()
            elif check_winner() == 'Tie':
                tiescore+=1
                pygame.mixer.music.pause()
                tie_sound.play()
                label.config(text="Tied 🤝",)
                tie.config(text="Tie Score = "+str(tiescore))
def check_winner():
    for row in range(3):
        if buttons[row][0]['text']== buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#00C853")
            buttons[row][1].config(bg="#00C853")
            buttons[row][2].config(bg="#00C853")
            return True
    for column in range(3):
        if buttons[0][column]['text']== buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#00C853")
            buttons[1][column].config(bg="#00C853")
            buttons[2][column].config(bg="#00C853")
            return True
    if buttons[0][0]['text']==buttons[1][1]["text"]==buttons[2][2]['text']!="":
        buttons[0][0].config(bg="#00C853")
        buttons[1][1].config(bg="#00C853")
        buttons[2][2].config(bg="#00C853")
        return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        buttons[0][2].config(bg="#00C853")
        buttons[1][1].config(bg="#00C853")
        buttons[2][0].config(bg="#00C853")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#F48FB1")
        return "Tie"
    else: 
        return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                spaces-=1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    menuclick.play()
    window.after(1500, pygame.mixer.music.unpause())
    global player,buttons
    player = players[0]
    label.config(text=player+"'s Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#2c2c2c")
    score_0.config(text=f"{players[0]}'s Score = {score0}")
    score_1.config(text=f"{players[1]}'s Score = {score1}")
    tie.config(text="Tie Score = "+str(tiescore))

pygame.mixer.music.load("Sounds/board_soundtrack.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

click=pygame.mixer.Sound("Sounds/click.mp3")
win=pygame.mixer.Sound("Sounds/win.mp3")
lost=pygame.mixer.Sound("Sounds/lost.mp3")
tie_sound=pygame.mixer.Sound("Sounds/tie.mp3")
blip=pygame.mixer.Sound("Sounds/ai_blip.mp3")
menuclick=pygame.mixer.Sound("Sounds/menu_click.mp3")

window =Tk()
window.title("Tic-Tac-Toe")
players = ["X","O"]
player=players[0]
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]
label = Label(text=player+"'s turn",font=('Helvetica',40),bg="#1e1e1e", fg="#f0f0f0")
label.pack(side="top")

button_frame= Frame(window,bg="#1e1e1e")
button_frame.pack(side="bottom", pady=10)
reset_button=Button(button_frame,text="Restart 🔁",font=('Helvetica',20), bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444", activeforeground="#ffffff",command=new_game)
reset_button.pack(side='left',padx=5)

reset_score=Button(button_frame,text= "Reset scoreboard👾",font=('Helvetica',20), bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444", activeforeground="#ffffff",command=score_reset)
reset_score.pack(side="left",padx=5)

score0=0
score1=0
tiescore=0
score_frame = Frame(window,bg="#1e1e1e")
score_frame.pack(side="right", padx=10)

score_0= Label(score_frame,text=players[0]+"'s Score = "+str(score0),font=('Helvetica',18),bg="#1e1e1e", fg="#f0f0f0")
score_1=Label(score_frame,text=players[1]+"'s Score = "+str(score1),font=("Helvetica",18),bg="#1e1e1e", fg="#f0f0f0")
tie= Label(score_frame,text="Tie Score = "+str(tiescore),font=('Helvetica',18),bg="#1e1e1e", fg="#f0f0f0")
score_0.pack()
score_1.pack()
tie.pack()



frame=Frame(window)
frame.pack()
window.configure(bg="#1e1e1e")
for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",font=('Helvetica',20),width=5,height=2,bg="#2c2c2c", fg="#f0f0f0",activebackground="#444444", activeforeground="#ffffff",command=lambda row=row, column=column: next_turn(row,column), )
        buttons[row][column].grid(row=row, column=column)

window.mainloop()