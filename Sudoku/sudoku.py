# Sudoku!!

# practice programming after taking a break for like 3 months lol

import pygame



class Board:
    def __init__(self):
        self.size = 9
        self.board = []

    # method initializes/resets board
    def createBoard(self, random=False):
        self.board = []
        for i in range(self.size):
            temp = []
            for j in range(self.size):
                temp.append("")
            self.board.append(temp)

    def __str__(self):
        string = ""
        for i in range(len(self.board)):
            string += str(self.board[i]) + "\n"
        return string

def main():
    board = Board()
    board.createBoard()
    print(board)


main()
