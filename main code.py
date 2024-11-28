import tkinter as tk
from tkinter import messagebox


class UltimateTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Ультимейт Крестики-Нолики")
        self.current_player = "X"
        self.boards = [[" " for _ in range(9)] for _ in range(9)]  # 9 маленьких полей
        self.buttons = self.create_boards()
        self.active_board = None  # Указывает, какое поле активно для следующего хода
        self.overall_board = [" " for _ in range(9)]  # Большое поле для победы
        self.create_reset_button()

    def create_boards(self):
        buttons = []
        for big_row in range(3):
            for big_col in range(3):
                # Создаем рамку для каждого большого поля
                frame = tk.Frame(self.master, borderwidth=2, relief="solid", padx=5, pady=5)
                frame.grid(row=big_row * 3, column=big_col * 3, rowspan=3, columnspan=3, sticky="nsew")

                small_buttons = []
                for row in range(3):
                    for col in range(3):
                        # Создаем кнопку для каждой ячейки маленького поля
                        button = tk.Button(
                            frame, text=" ", font=("Arial", 12), width=4, height=2,
                            command=lambda br=big_row, bc=big_col, sr=row, sc=col: self.on_button_click(br, bc, sr, sc)
                        )
                        button.grid(row=row, column=col, sticky="nsew")
                        small_buttons.append(button)
                buttons.append(small_buttons)
        return buttons

    def on_button_click(self, br, bc, sr, sc):
        if self.active_board is not None and self.active_board != br * 3 + bc:
            messagebox.showinfo("Ошибка", "Вы должны играть в активном поле.")
            return

        index = sr * 3 + sc
        board_index = br * 3 + bc

        if self.boards[board_index][index] == " ":
            self.boards[board_index][index] = self.current_player
            self.buttons[board_index][index].config(text=self.current_player)

            if self.check_winner(self.boards[board_index]):
                self.overall_board[board_index] = self.current_player
                self.update_board_ui(board_index, self.current_player)
                if self.check_winner(self.overall_board):
                    messagebox.showinfo("Победа", f"Игрок {self.current_player} выиграл на большом поле!")
                    self.reset_game()
                    return

            elif " " not in self.boards[board_index]:
                self.overall_board[board_index] = "draw"

            self.active_board = index if self.overall_board[index] == " " else None
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showinfo("Ошибка", "Эта ячейка уже занята!")

    def check_winner(self, board):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for condition in win_conditions:
            if all(board[i] == self.current_player for i in condition):
                return True
        return False

    def update_board_ui(self, board_index, winner):
        for button in self.buttons[board_index]:
            button.config(text=winner, state=tk.DISABLED)

    def create_reset_button(self):
        reset_button = tk.Button(self.master, text="Новая игра", command=self.reset_game)
        reset_button.grid(row=9, column=0, columnspan=9, sticky="nsew")

    def reset_game(self):
        self.current_player = "X"
        self.boards = [[" " for _ in range(9)] for _ in range(9)]
        self.overall_board = [" " for _ in range(9)]
        self.active_board = None
        for small_buttons in self.buttons:
            for button in small_buttons:
                button.config(text=" ", state=tk.NORMAL)


root = tk.Tk()
game = UltimateTicTacToe(root)
root.mainloop()
