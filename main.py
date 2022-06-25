import pygame as pg
from time import sleep

class Board:
    def __init__(self, turn):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = turn

    def check(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != None:
                return True, self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != None:
                return True, self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            return True, self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            return True, self.board[0][2]

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == None:
                    return False, None

        return True, -1

    def move(self, x, y):
        if self.board[x][y] == None:
            self.board[x][y] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            return True
        return False

turn = 'X'
x, y = None, None
width, height = 300, 300
white, black = (255, 255, 255), (0, 0, 0)

clock = pg.time.Clock()
running = True

pg.display.set_caption('Tic Tac Toe')
screen = pg.display.set_mode((width, height))

board = Board(turn)
pg.init()
while running:
    if board.check()[0]:
        if board.check()[1] == -1:
            print('Draw')
        else:
            print(f'{board.check()[1]} wins!')
        running = False
        sleep(3)
        continue
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mousex, mousey = pg.mouse.get_pos()
            x, y = int(mousex // (width // 3)), int(mousey // (height // 3))
            if board.move(x, y):
                board.check()

    screen.fill(black)
    for i in range(3):
        for j in range(3):
            if board.board[i][j] == None:
                continue
            if board.board[i][j] == 'X':
                pg.draw.line(screen, white, (i * (width // 3), j * (height // 3)), ((i + 1) * (width // 3), (j + 1) * (height // 3)), 5)
                pg.draw.line(screen, white, ((i + 1) * (width // 3), j * (height // 3)), (i * (width // 3), (j + 1) * (height // 3)), 5)
            if board.board[i][j] == 'O':
                pg.draw.circle(screen, white, ((i + 1 / 2) * (width // 3), (j + 1 / 2) * (height // 3)), (width // 3) // 2, 5)
    
    pg.display.update()
    clock.tick(60)