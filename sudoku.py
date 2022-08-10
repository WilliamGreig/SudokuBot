# Sudoku!!

import pygame
import numpy as np
import math


list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

background_colour = (255,255,255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sudoku')


class Sudoku:
    def __init__(self, preset):
        self.size = 9
        self.board = []
        self.createBoard(preset)
        self.selected = None
        self.toggle = True

    # method initializes/resets board
    def createBoard(self, preset):
        self.board = []
        if not preset:
            for i in range(self.size):
                temp = []
                for j in range(self.size):
                    temp.append(np.random.randint(1, 10))
                self.board.append(temp)
        else:
            self.board = [
                ["4", "", "", "", "3", "2", "", "", "5"],
                ["5", "", "8", "7", "6", "4", "2", "1", ""],
                ["", "", "2", "5", "9", "", "", "7", "", "4"],
                ["3", "", "5", "8", "", "1", "", "", "6"],
                ["", "2", "6", "", "4", "9", "", "5", ""],
                ["8", "", "1", "", "", "", "4", "", ""],
                ["9", "", "3", "", "", "7", "5", "", ""],
                ["", "8", "", "", "", "", "", "", ""],
                ["2", "", "4", "6", "8", "", "", "", ""]
            ]


    def __str__(self):
        string = ""
        for i in range(len(self.board)):
            string += str(self.board[i]) + "\n"
        return string

    def play(self):
        pygame.init()
        running = True
        while running:
            self.render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # selected is the exact coordinates (X, Y) of the window
                    self.selected = pygame.mouse.get_pos()
                    # selected coord is the coordinates of the position on the board itself (data structure)
                    self.selec_coord = (math.floor( (self.selected[0] / width * self.size) % self.size),
                                     math.floor( (self.selected[1] / width * self.size) % self.size))

                # change the value
                if event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_t:
                            self.toggle = not self.toggle

                        if int(event.unicode) in list_nums:
                            self.board[self.selec_coord[1]][self.selec_coord[0]] = str(event.unicode)
                        if int(event.unicode) == 0:
                            self.board[self.selec_coord[1]][self.selec_coord[0]] = ""
                    except:
                        pass
            self.render()

    def draw_lines(self):
        for j in range(9):
            pygame.draw.line(screen, pygame.Color(0, 0, 0), [0, (j+1) / 3 * height / 3], [width, (j+1)/3 * height / 3], width=2)
            pygame.draw.line(screen, pygame.Color(0, 0, 0), [(j+1) / 3 * width / 3, 0], [(j+1) / 3 * width / 3, height], width=2)

        # draw board
        for i in range(2):
            # horizontal -- big line
            pygame.draw.line(screen, pygame.Color(128, 91, 255), [0, (i+1) / 3 * height], [width, (i+1)/3 * height], width=5)
            # vertical -- big line
            pygame.draw.line(screen, pygame.Color(128, 91, 255), [(i+1) / 3 * width, 0], [(i+1) / 3 * width, height], width=5)

    def draw_numbers(self):
        # numbers
        row_index = 0
        for row in self.board:
            col_index = 0
            for number in row:
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(number), True, pygame.Color(0, 0, 0))
                textRect = text.get_rect()
                off_set = height / self.size / 2
                textRect.center = (col_index * height / self.size + off_set, row_index * width / self.size + off_set)
                screen.blit(text, textRect)
                col_index = col_index + 1
            row_index = row_index + 1

    # gets intersecting row and column cells from a specified coordinate from the board
    def get_intersecting_row_cols(self, x, y):
        cells = []
        for i in range(self.size):
            cells.append( (i, y) )
            cells.append( (x, i) )
        return cells

    def draw_selected(self):
        # get the closest coordinate
        if self.selected is not None:
            cells = self.get_intersecting_row_cols(self.selec_coord[0], self.selec_coord[1])
            for cell in cells:
                coor_x = cell[0] * width / self.size
                coor_y = cell[1] * width / self.size
                pygame.draw.rect(screen, pygame.Color(220, 220, 220), pygame.Rect(coor_x, coor_y, width / self.size, height / self.size))
            coor_x = math.floor( (self.selected[0] / width * self.size) % self.size) * (width / self.size)
            coor_y = math.floor( (self.selected[1] / width * self.size) % self.size) * (height / self.size)
            pygame.draw.rect(screen, pygame.Color(185, 185, 185), pygame.Rect(coor_x, coor_y, width / self.size, height / self.size))

    def get_quadrant(self, x, y):
        cells = []

        x = math.pow(0, abs(x-3)) + math.pow(0, abs(x-4)) + math.pow(0, abs(x-5)) + 2 * (math.pow(0, abs(x-6)) + math.pow(0, abs(x-7)) + math.pow(0, abs(x-8)))
        y = math.pow(0, abs(y-3)) + math.pow(0, abs(y-4)) + math.pow(0, abs(y-5)) + 2 * (math.pow(0, abs(y-6)) + math.pow(0, abs(y-7)) + math.pow(0, abs(y-8)))
        # x = math.floor(int(x) / 3)
        # y = math.floor(int(y) / 3)
        for i in range(3):
            for j in range(3):
                cells.append( (x * math.sqrt(self.size) + i, y * math.sqrt(self.size) + j) )
        return cells


    def draw_toggle(self):
        if self.toggle and self.selected is not None:
            value = self.board[self.selec_coord[1]][self.selec_coord[0]]
            if value != "" and int(value) in list_nums:
                board_coordinates = []
                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if self.board[i][j] != "":
                            if int(self.board[i][j]) == int(value):
                                board_coordinates.append( [i, j] )
                for x in board_coordinates:
                    cells = self.get_intersecting_row_cols(x[1], x[0])
                    quadrant = self.get_quadrant(x[1], x[0])
                    for cell in cells:
                        coor_x = cell[0] * width / self.size
                        coor_y = cell[1] * width / self.size
                        pygame.draw.rect(screen, pygame.Color(255, 204, 204), pygame.Rect(coor_x, coor_y, width / self.size, height / self.size))
                    for c in quadrant:
                        coor_x = c[0] * width / self.size
                        coor_y = c[1] * width / self.size
                        pygame.draw.rect(screen, pygame.Color(255, 204, 204), pygame.Rect(coor_x, coor_y, width / self.size, height / self.size))

    def print(self):
        for r in self.board:
            print(r)

    def render(self):
        screen.fill(background_colour)
        self.draw_selected()
        self.draw_toggle()
        self.draw_lines()
        self.draw_numbers()
        pygame.display.flip()


s = Sudoku(preset=True)
s.play()
