from tkinter import *
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
            return b[i][0], [(i, 0), (i, 1), (i, 2)]
        if b[0][i] == b[1][i] == b[2][i] != EMPTY:
            return b[0][i], [(0, i), (1, i), (2, i)]

    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return b[0][0], [(0, 0), (1, 1), (2, 2)]

    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return b[0][2], [(0, 2), (1, 1), (2, 0)]

    if all(b[r][c] != EMPTY for r in range(3) for c in range(3)):
        return "Tie", []

    return None, []


def minimax(b, is_max):
    winner, _ = check_winner(b)
    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if winner == "Tie":
        return 0

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
        make_move(move[0], move[1], AI)

# ---------------- UI LOGIC ----------------
def make_move(r, c, player):
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
        make_move(r, c, HUMAN)


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

buttons = [[None for _ in range(3)] for _ in range(3)]

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

window.mainloop()
