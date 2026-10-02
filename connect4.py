import tkinter as tk
from tkinter import messagebox


# -----------------------------
# Game settings
# -----------------------------

ROWS = 6
COLS = 7

# O = empty
# R = red
# B = blue
board = [["O" for _ in range(COLS)] for _ in range(ROWS)]

current_player = "R"
game_over = False


# -----------------------------
# Window
# -----------------------------

window = tk.Tk()
window.title("Connect 4")
window.resizable(False, False)


# -----------------------------
# Functions
# -----------------------------

def update_turn_label():

    if current_player == "R":
        turn_label.config(
            text="Red's Turn",
            fg="red"
        )

    else:
        turn_label.config(
            text="Blue's Turn",
            fg="blue"
        )


def drop_piece(column):

    global current_player, game_over

    if game_over:
        return

    # Start from the bottom of the column
    for row in range(ROWS - 1, -1, -1):

        # Find an empty cell
        if board[row][column] == "O":

            # Place the piece
            board[row][column] = current_player

            update_board()

            # Check for a win
            if check_win(row, column):

                game_over = True

                if current_player == "R":
                    winner = "Red"
                    winner_colour = "red"
                else:
                    winner = "Blue"
                    winner_colour = "blue"

                turn_label.config(
                    text=f"{winner} Wins!",
                    fg=winner_colour
                )

                play_again = messagebox.askyesno(
                    "Game Over",
                    f"{winner} wins!\n\nPlay again?"
                )

                if play_again:
                    reset_game()
                else:
                    window.destroy()

                return

            # Check for a draw
            if all(board[0][col] != "O" for col in range(COLS)):

                game_over = True

                turn_label.config(
                    text="It's a Draw!",
                    fg="black"
                )

                play_again = messagebox.askyesno(
                    "Game Over",
                    "It's a draw!\n\nPlay again?"
                )

                if play_again:
                    reset_game()
                else:
                    window.destroy()

                return

            # Change player
            if current_player == "R":
                current_player = "B"
            else:
                current_player = "R"

            update_turn_label()

            return

    # Column is full
    messagebox.showinfo(
        "Column Full",
        "That column is full!"
    )


def check_win(row, col):

    player = board[row][col]

    # Horizontal
    # Vertical
    # Diagonal down-right
    # Diagonal down-left
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1)
    ]

    for row_direction, col_direction in directions:

        count = 1

        # Check one direction
        r = row + row_direction
        c = col + col_direction

        while (
            0 <= r < ROWS
            and 0 <= c < COLS
            and board[r][c] == player
        ):

            count += 1

            r += row_direction
            c += col_direction

        # Check opposite direction
        r = row - row_direction
        c = col - col_direction

        while (
            0 <= r < ROWS
            and 0 <= c < COLS
            and board[r][c] == player
        ):

            count += 1

            r -= row_direction
            c -= col_direction

        # Four in a row
        if count >= 4:
            return True

    return False


def update_board():

    for row in range(ROWS):

        for col in range(COLS):

            if board[row][col] == "R":

                cells[row][col].config(
                    bg="red"
                )

            elif board[row][col] == "B":

                cells[row][col].config(
                    bg="blue"
                )

            else:

                cells[row][col].config(
                    bg="white"
                )


def reset_game():

    global current_player, game_over

    # Reset the matrix
    for row in range(ROWS):

        for col in range(COLS):

            board[row][col] = "O"

    current_player = "R"
    game_over = False

    update_board()
    update_turn_label()


# -----------------------------
# Turn label
# -----------------------------

turn_label = tk.Label(
    window,
    text="Red's Turn",
    font=("Arial", 20, "bold"),
    fg="red"
)

turn_label.pack(pady=10)


# =========================================================
# EVERYTHING BELOW USES ONE GRID
# =========================================================

game_frame = tk.Frame(window)

game_frame.pack()


# Width of each Connect 4 column
COLUMN_WIDTH = 65


# Make all 7 columns exactly the same width
for col in range(COLS):

    game_frame.columnconfigure(
        col,
        minsize=COLUMN_WIDTH
    )


# =========================================================
# COLUMN BUTTONS
# =========================================================

for col in range(COLS):

    button = tk.Button(
        game_frame,
        text="▼",
        font=("Arial", 12, "bold"),
        command=lambda c=col: drop_piece(c)
    )

    button.grid(
        row=0,
        column=col,
        sticky="ew"
    )


# =========================================================
# GAME BOARD
# =========================================================

cells = []


for row in range(ROWS):

    # Make every row the same height
    game_frame.rowconfigure(
        row + 1,
        minsize=COLUMN_WIDTH
    )

    row_cells = []

    for col in range(COLS):

        cell = tk.Frame(
            game_frame,
            width=COLUMN_WIDTH,
            height=COLUMN_WIDTH,
            bg="white",
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=2
        )

        # Don't let the frame resize itself
        cell.grid_propagate(False)

        cell.grid(
            row=row + 1,
            column=col
        )

        row_cells.append(cell)

    cells.append(row_cells)


# =========================================================
# RESTART BUTTON
# =========================================================

reset_button = tk.Button(
    window,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game
)

reset_button.pack(pady=10)


# -----------------------------
# Start game
# -----------------------------

update_turn_label()

window.mainloop()
