import math

def checkwinner(board,player):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tie(board):
    for r in board:
        for c in r:
            if c == "":
                return False
    return True


def minimax(board, maximizing):
    if checkwinner(board, "O"):
        return 1
    elif checkwinner(board, "X"):
        return -1
    elif tie(board):
        return 0
    
    if maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c]="O"
                    score=minimax(board,False)
                    board[r][c]=""
                    best_score = max(best_score,score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c]="X"
                    score = minimax(board, True)
                    board[r][c]=""
                    best_score = min(best_score, score)
        return best_score

def ai_move(buttons, next_turn):
    board=[[buttons[r][c]['text']for c in range(3)]for r in range(3)]

    best_score= -math.inf
    best_move= None

    for r in range(3):
        for c in range(3):
            if board[r][c]=="":
                board[r][c]="O"
                score= minimax(board, False)
                board[r][c]=""
                if score > best_score:
                    best_score = score
                    best_move = (r,c)
    
    if best_move:
        next_turn(*best_move)

