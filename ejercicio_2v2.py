# SANCHEZ CALVIMONTES PABLO
# INGENIERIA DE SISTEMAS
# SIS 420 - INTELIGENCIA ARTIFICIAL
# ING PACHECO LORA CARLOS


# PRIMER PARCIAL - EJERCICIO 2 -
# version 2
# ===================================================== #

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        while True:
            if checkForWin():
                if letter == 'X':
                    c += 1
                    print(f"Puntos de IA -> {c}")
                else:
                    c  += 1
                    print(f"Punto de Usuario -> {c}")
                    exit()
            return

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():
    c = 0
    i = 0
    while True:
        if (board[1] == board[2] and board[1] != ' '):
            c += 1
            return c 
        elif (board[4] == board[5] and board[4] != ' '): 
            c += 1
            return c
        elif (board[7] == board[8] and board[7] != ' '):
            c += 1
            return c
        elif (board[2] == board[3] and board[2] != ' '):
            c += 1
            return c
        elif (board[5] == board[6] and board[5] != ' '):
            c += 1
            return c
        elif (board[8] == board[9] and board[8] != ' '):
            c += 1
            return c
        elif (board[1] == board[4] and board[1] != ' '):
            c += 1
            return c
        elif (board[2] == board[5] and board[2] != ' '):
            c += 1
            return c
        elif (board[3] == board[6] and board[3] != ' '):
            c += 1
            return c
        elif (board[4] == board[7] and board[4] != ' '):
            c += 1
            return c
        elif (board[5] == board[8] and board[5] != ' '):
            c += 1
            return c
        elif (board[6] == board[9] and board[6] != ' '):
            c += 1
            return c
        else:
            return False


def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == mark):
        return True 
    elif (board[4] == board[5] and board[4] == mark): 
        return True
    elif (board[7] == board[8] and board[7] == mark):
        return True
    elif (board[2] == board[3] and board[2] == mark):
        return True
    elif (board[5] == board[6] and board[5] == mark):
        return True
    elif (board[8] == board[9] and board[8] == mark):
        return True
    elif (board[1] == board[4] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == mark):
        return True
    elif (board[4] == board[7] and board[4] == mark):
        return True
    elif (board[5] == board[8] and board[5] == mark):
        return True
    elif (board[6] == board[9] and board[6] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return


def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True

i = 0
while i < 9:
    while not checkForWin():
        compMove()
        playerMove()
