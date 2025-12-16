from tkinter import *
<<<<<<< HEAD
import math

# ---------------- CONSTANTS ----------------
HUMAN = "X"
AI = "O"
EMPTY = ""

game_over = False

board = [[EMPTY for _ in range(3)] for _ in range(3)]

# ---------------- GAME LOGIC ----------------
def check_winner(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != EMPTY:
            return b[i][0], [(i,0),(i,1),(i,2)]
        if b[0][i] == b[1][i] == b[2][i] != EMPTY:
            return b[0][i], [(0,i),(1,i),(2,i)]

    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return b[0][0], [(0,0),(1,1),(2,2)]
    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return b[0][2], [(0,2),(1,1),(2,0)]

    if all(b[r][c] != EMPTY for r in range(3) for c in range(3)):
        return "Tie", []

    return None, []

def minimax(b, is_max):
    winner, _ = check_winner(b)
    if winner == AI: return 1
    if winner == HUMAN: return -1
    if winner == "Tie": return 0

    if is_max:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == EMPTY:
                    b[r][c] = AI
                    best = max(best, minimax(b, False))
                    b[r][c] = EMPTY
        return best
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == EMPTY:
                    b[r][c] = HUMAN
                    best = min(best, minimax(b, True))
                    b[r][c] = EMPTY
        return best

def ai_move():
    best_score = -math.inf
    move = None

    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = AI
                score = minimax(board, False)
                board[r][c] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (r, c)

    if move:
        place_move(move[0], move[1], AI)

# ---------------- UI LOGIC ----------------
def place_move(r, c, player):
    global game_over
    board[r][c] = player
    buttons[r][c].config(text=player)

    winner, cells = check_winner(board)
    if winner:
        game_over = True
        end_game(winner, cells)
    else:
        if player == HUMAN:
            label.config(text="AI thinking...")
            window.after(300, ai_move)
        else:
            label.config(text="Your turn")

def on_click(r, c):
    if board[r][c] == EMPTY and not game_over:
        place_move(r, c, HUMAN)

def end_game(winner, cells):
    if winner == "Tie":
        label.config(text="It's a Tie!")
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="yellow")
    else:
        label.config(text=f"{winner} wins!")
        for r, c in cells:
            buttons[r][c].config(bg="green")

def new_game():
    global game_over
    game_over = False
    label.config(text="Your turn")
    for r in range(3):
        for c in range(3):
            board[r][c] = EMPTY
            buttons[r][c].config(text="", bg="white")

# ---------------- TKINTER SETUP ----------------
window = Tk()
window.title("Tic Tac Toe - AI")
window.resizable(False, False)

label = Label(window, text="Your turn", font=("Consolas", 24))
label.pack(pady=10)

Button(window, text="Restart", font=("Consolas", 16), command=new_game).pack(pady=5)

frame = Frame(window)
frame.pack(pady=10)

buttons = [[None]*3 for _ in range(3)]

for r in range(3):
    for c in range(3):
        btn = Button(
            frame,
            text="",
            font=("Consolas", 36),
            width=3,
            height=1,
            bg="white",
            command=lambda r=r, c=c: on_click(r, c)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = btn
=======
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
>>>>>>> 569df2d05bc134abf9c174809236ee61d0548eee

window.mainloop()
