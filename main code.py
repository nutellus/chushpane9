import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master  # Определение корневого окна
        self.master.title("Крестики-нолики")  # Установка заголовка окна

        self.current_player = "X"  # Установка начального игрока
        self.board = [" " for _ in range(9)]  # Создание пустого игрового поля

        self.buttons = []  # Создание списка для хранения кнопок игрового поля
        for i in range(3):
            row = []  # Создание списка для хранения кнопок в строке
            for j in range(3):
                # Создание кнопки и привязка метода on_button_click к событию нажатия
                button = tk.Button(self.master, text=" ", font=("Arial", 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, sticky="nsew")  # Размещение кнопки на сетке
                row.append(button)  # Добавление кнопки в строку
            self.buttons.append(row)  # Добавление строки кнопок в общий список

        self.reset_button = tk.Button(self.master, text="Новая игра", command=self.reset_game)  # Создание кнопки для сброса игры
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")  # Размещение кнопки на сетке

    def on_button_click(self, i, j):
        if self.board[i * 3 + j] == " ":  # Проверка, что клетка пуста
            self.board[i * 3 + j] = self.current_player  # Установка символа текущего игрока в клетку
            self.buttons[i][j].config(text=self.current_player)  # Обновление текста на кнопке
            if self.check_winner(i, j):  # Проверка на победу
                messagebox.showinfo("Победа", f"Игрок {self.current_player} выиграл!")  # Отображение сообщения о победе
                self.reset_game()  # Сброс игры
            elif " " not in self.board:  # Проверка на ничью
                messagebox.showinfo("Ничья", "Ничья!")  # Отображение сообщения о ничьей
                self.reset_game()  # Сброс игры
            else:
                self.current_player = "O" if self.current_player == "X" else "X"  # Смена игрока

    def check_winner(self, i, j):
        row = all(self.board[i*3 + col] == self.current_player for col in range(3))  # Проверка по горизонтали
        col = all(self.board[row*3 + j] == self.current_player for row in range(3))  # Проверка по вертикали
        diag1 = all(self.board[i*3 + i] == self.current_player for i in range(3))  # Проверка по диагонали
        diag2 = all(self.board[i*3 + 2-i] == self.current_player for i in range(3))  # Проверка по диагонали
        return any([row, col, diag1, diag2])  # Возвращает True, если есть победа

    def reset_game(self):
        self.current_player = "X"  # Установка начального игрока
        self.board = [" " for _ in range(9)]  # Очистка игрового поля
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")  # Очистка текста на кнопках


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
