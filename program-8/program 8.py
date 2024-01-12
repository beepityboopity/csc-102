# The following program creates a simple board for a classic tic-tac-toe game
# There are two 2D arrays - one for board and one for buttons
# Extend the GUI by adding a button to reset the game!
# Display a message upon winning, this might help - https://docs.python.org/3/library/tkinter.messagebox.html
# Add a score layout to the GUI
from tkinter import *


class Grid:
    full = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.empty = True
        self.value = None
        self.button = None


class TicTacToe(Frame):
    player = "X"
    x_score = 0
    o_score = 0

    def __init__(self, master):
        Frame.__init__(self, master)

        for x in range(0, 3):
            Grid.full.append([])
            for y in range(0, 3):
                Grid.full[-1].append(Grid(x, y))
                Grid.full[x][y].button = Button(master, text="", width=10, height=3, font=("Arial", 20),
                                                command=lambda b=Grid.full[x][y]: self.on_button_click(b))
                Grid.full[x][y].button.grid(row=x, column=y)

        self.x_wins = Label(text="X Score: {}" .format(TicTacToe.x_score))
        self.x_wins.grid(row=0, column=3)
        self.o_wins = Label(text="O Score: {}".format(TicTacToe.o_score))
        self.o_wins.grid(row=0, column=3, pady=(50, 0))

    def on_button_click(self, button):
        button.empty = False
        button.value = TicTacToe.player
        button.button.config(text=TicTacToe.player)
        if TicTacToe.player == "X":
            TicTacToe.player = "O"
        else:
            TicTacToe.player = "X"
        self.check_winner()

    def check_winner(self):
        for row in Grid.full:
            if all(obj.value == row[0].value and row[0].value is not None for obj in row):
                self.win()

        for x in range(3):
            if Grid.full[0][x].value == Grid.full[1][x].value == Grid.full[2][x].value and not Grid.full[0][x].empty:
                self.win()

        if Grid.full[0][0].value == Grid.full[1][1].value == Grid.full[2][2].value and not Grid.full[0][0].empty:
            self.win()

        if Grid.full[0][2].value == Grid.full[1][1].value == Grid.full[2][0].value and not Grid.full[0][2].empty:
            self.win()

    def reset_board(self):
        pass

    def win(self):
        print("whee")


window = Tk()
Game = TicTacToe(window)
window.title("Tic Tac Toe")
window.mainloop()
