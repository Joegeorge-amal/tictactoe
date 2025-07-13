import random

def ai_move(buttons, next_turn):
    empty=[]
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"]=="":
                empty.append((r,c))
    if empty:
        row,column=random.choice(empty)
        next_turn(row,column)