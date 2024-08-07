import tkinter as tk 
from tkinter import messagebox
import datetime

class Logger:
    
    def __init__(self , file):
        self.log_file = file
        self.new_log()
    
    
    def new_log(self):
        with open(self.log_file, "a") as log:
            log.write("\nNew Game Started at {}\n".format(datetime.datetime.now()))
            log.write("Initial Board:\n")
            self.log_board_state([[" " for _ in range(3)] for _ in range(3)], log)
    
    
    def log_move(self, turn_count , row , col, player , board):
        with open(self.log_file, "a") as log:
            log.write("Move {}: Player {} to position ({}, {})\n".format(turn_count, player, row, col))
            self.log_board_state(board, log)
            
            
    def log_board_state(self, board, log):
        
        for row in board:
            log.write("| " + " | ".join(cell if cell else " " for cell in row)+ " |\n")
        log.write("\n")
        
class TicTacToe:
    
    def __init__(self, root):
        
        self.root = root
        self.root.title("Game of Tic Tak Toe")
        self.turn = True
        self.turn_count = 0 
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.widgets()
        self.logger = Logger("Tic-tac-toe_history.txt")
        
    def widgets(self):
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2,
                                              command=lambda row=i, col=j: self.on_click(row,col))
                self.buttons[i][j].grid(row=i , column=j)
                
        self.reset = tk.Button(self.root, text="New Game", command=self.reset_game)
        self.reset.grid(row=3 , column=0, columnspan=3)
        
        
    def on_click(self , row , col):
        if self.board[row][col] == "" and self.turn:
            self.board[row][col] = "X"
            self.buttons[row][col]["text"] = "X"
            
            self.logger.log_move(self.turn_count, row, col, "X", self.board)
            
            self.turn = False
            self.turn_count += 1
        elif self.board[row][col] == "" and not self.turn:
            self.board[row][col] = "O"
            self.buttons[row][col]["text"] = "O"
            
            self.logger.log_move(self.turn_count, row, col, "O", self.board)
            
            self.turn = True
            self.turn_count += 1
        self.check_for_winner()
        
    def check_for_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                self.show_winner(self.board[i][0])
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                self.show_winner(self.board[0][i])
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.show_winner(self.board[0][0])
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.show_winner(self.board[0][2])
            return
        if self.turn_count == 9:
            self.show_draw()

    def show_winner(self, winner):
        with open(self.logger.log_file, "a") as log:
            log.write("Winner: {}\n".format(winner))
        messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
        self.reset_game()

    def show_draw(self):
        with open(self.logger.log_file, "a") as log:
            log.write("Result: It's a draw!\n")
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.turn = True
        self.turn_count = 0
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.logger.new_log()


def main():
    
     
    root = tk.Tk()
     
    ictacktoe_game = TicTacToe(root)
     
    root.mainloop()
     
main()
    
        
        
        
        
                
        
        
            
            
    

        
        
        
        
            