# GUI.py
# RUN THIS FILE
import sys

import pygame
import solver
from solver import solve, valid, find_empty, print_board
import time
pygame.font.init()


class Grid:
    # To change the starting board change this
    board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

    board_beginner = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    board_easy = [
        [0, 0, 1, 6, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 1, 0, 0, 0, 5],
        [3, 0, 0, 0, 0, 9, 0, 2, 0],
        [8, 0, 0, 0, 0, 4, 0, 9, 0],
        [0, 5, 0, 0, 2, 0, 0, 7, 0],
        [0, 6, 0, 8, 0, 0, 0, 0, 4],
        [0, 2, 0, 4, 0, 0, 0, 0, 1],
        [5, 0, 0, 0, 9, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 1, 2, 0, 0]
    ]

    board_moderate = [
        [0, 0, 9, 2, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 4, 0, 0, 0, 6],
        [4, 0, 0, 0, 0, 9, 0, 1, 0],
        [7, 0, 0, 0, 0, 1, 0, 9, 0],
        [0, 4, 0, 0, 7, 0, 0, 5, 0],
        [0, 1, 0, 9, 0, 0, 0, 0, 7],
        [0, 6, 0, 7, 0, 0, 0, 0, 4],
        [5, 0, 0, 0, 2, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 3, 2, 0, 0]
    ]

    board_hard = [
        [0, 0, 3, 5, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 1, 0, 0, 0, 6],
        [9, 0, 0, 0, 0, 3, 0, 5, 0],
        [8, 0, 0, 0, 0, 5, 0, 2, 0],
        [0, 1, 0, 0, 9, 0, 0, 7, 0],
        [0, 7, 0, 2, 0, 0, 0, 0, 4],
        [0, 4, 0, 7, 0, 0, 0, 0, 9],
        [6, 0, 0, 0, 2, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 6, 4, 0, 0]
    ]

    board_evil = [
        [0, 0, 7, 4, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 5, 0, 0, 0, 7],
        [3, 0, 0, 0, 0, 8, 0, 2, 0],
        [4, 0, 0, 0, 0, 2, 0, 8, 0],
        [0, 1, 0, 0, 9, 0, 0, 3, 0],
        [0, 7, 0, 6, 0, 0, 0, 0, 9],
        [0, 3, 0, 5, 0, 0, 0, 0, 6],
        [1, 0, 0, 0, 4, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 9, 1, 0, 0]
    ]

    board_fiendish = [
        [0, 0, 5, 7, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 1, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 3, 0, 5, 0],
        [6, 0, 0, 0, 0, 7, 0, 3, 0],
        [0, 8, 0, 0, 4, 0, 0, 7, 0],
        [0, 5, 0, 6, 0, 0, 0, 0, 1],
        [0, 2, 0, 9, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 3, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 8, 2, 0, 0]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row,col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return int(y), int(x)
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


win = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("comicsans", 40)
Clock = pygame.time.Clock()






def button(win, button_pos, text, font, color):
    text_render = font.render(text, 1, (0, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = button_pos
    pygame.draw.line(win, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(win, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(win, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(win, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(win, color, (x, y, w, h))
    return win.blit(text_render, (x, y))


def redraw_window(win, board, time, strikes, b1, b2):
    win.fill((255, 255, 255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Время: " + format_time(time), 1, (0, 0, 0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    text = fnt.render(f"{5 - strikes} осталось", 1, (255, 0, 0))
    win.blit(text, (150, 560))
    b1 = button(win, (600, 100), "Выход", font, (100, 100, 100))
    b2 = button(win, (600, 50), "Сдаюсь!", font, (0, 250, 0))
    # Draw grid and board
    board.draw(win)

def format_time(secs):
    sec = secs % 60
    minute = secs//60
    hour = minute//60
    mat = " " + str(minute) + ":" + str(sec)
    return mat


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect = (x, y)
    surface.blit(textobj, textrect)


def main_menu(win, run):
    running = True
    while running:
        win.fill((255, 255, 255))
        draw_text("Выберите уровень сложности: ", font, (0, 0, 0), win, 20, 20)
        b1 = button(win, (20, 400), "Выход", font, (100, 100, 100))
        b2 = button(win, (20, 100), "Новичок", font, (0, 250, 0))
        b3 = button(win, (20, 150), "Легкий", font, (255, 255, 0))
        b4 = button(win, (20, 200), "Средний", font, (255, 200, 0))
        b5 = button(win, (20, 250), "Сложный", font, (255, 100, 0))
        b6 = button(win, (20, 300), "Ужасный", font, (255, 55, 0))
        b7 = button(win, (20, 350), "Кошмарный", font, (255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = False
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if b2.collidepoint(pygame.mouse.get_pos()):
                    Grid.board = Grid.board_beginner
                    running = False
                if b3.collidepoint(pygame.mouse.get_pos()):
                    Grid.board = Grid.board_easy
                    running = False
                if b4.collidepoint(pygame.mouse.get_pos()):
                    Grid.board = Grid.board_moderate
                    running = False
                if b5.collidepoint(pygame.mouse.get_pos()):
                    Grid.board = Grid.board_hard
                    running = False
                if b6.collidepoint(pygame.mouse.get_pos()):
                    Grid.board = Grid.board_evil
                    running = False
                if b7.collidepoint(pygame.mouse.get_pos()):
                    Grid.board = Grid.board_fiendish
                    running = False
        pygame.display.update()
        Clock.tick(60)


def sudoku(win, board, run):
    slv = []
    start = time.time()
    strikes = 0
    while run:
        b1 = button(win, (600, 100), "Выход", font, (100, 100, 100))
        b2 = button(win, (600, 50), "Сдаюсь!", font, (0, 250, 0))
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False
                        if strikes == 5:
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if b2.collidepoint(pygame.mouse.get_pos()):
                    slv = solve(Grid.board)
                    print(slv)
        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes, b1, b2)
        pygame.display.update()


def main(win):
    pygame.display.set_caption("Sudoku")
    key = None
    run = True
    main_menu(win, run)
    board = Grid(9, 9, 540, 540)
    sudoku(win, board, run)


main(win)
pygame.quit()
