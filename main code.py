import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = self.create_buttons()

        self.reset_button = tk.Button(self.master, text="Новая игра", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def create_buttons(self):
        buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=("Arial", 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            buttons.append(row)
        return buttons

    def on_button_click(self, i, j):
        index = i * 3 + j
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Победа", f"Игрок {winner} выиграл!" if winner != "draw" else "Ничья!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == self.current_player for i in condition):
                return self.current_player
        if " " not in self.board:
            return "draw"
        return None

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for row in self.buttons:
            for button in row:
                button.config(text=" ")


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()

