import random

def ai_move(buttons, next_turn):
    #try to win
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"]=="":
                buttons[r][c]["text"]="O"
                if checkwinner(buttons):
                    buttons[r][c]["text"] = ""
                    next_turn(r,c)
                    return
                buttons[r][c]["text"]=""
    #block
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"]=="":
                buttons[r][c]["text"]="X"
                if checkwinner(buttons):
                    buttons[r][c]["text"]=""
                    next_turn(r,c)
                    return
                buttons[r][c]["text"]=""
    empty=[]
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"]=="":
                empty.append((r,c))
    if empty:
        row,column=random.choice(empty)
        next_turn(row,column)

def checkwinner(buttons):
    for r in range(3):
        if buttons[r][0]['text'] == buttons[r][1]['text'] == buttons[r][2]['text'] != "":
            return True
    for c in range(3):
        if buttons[0][c]['text'] == buttons[1][c]['text'] == buttons[2][c]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False