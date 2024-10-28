"""
This problem was asked by Salesforce.

Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid. The game ends either when one player creates a line of four consecutive discs of their color (horizontally, vertically, or diagonally), or when there are no more spots left in the grid.

Design and implement Connect 4.


using pygames to implement connect 4

"""

import random, pygame, sys
from pygame.locals import *
from collections import deque

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 7
BOARDHEIGHT = 6
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)


GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
NAVYBLUE = (60, 60, 100)
RED = (250, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DISCCOLORS = (RED, BLACK)

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Connect Four')

    mainBoard = generateNewBoard()
    boardState = generateNewBoardState()

    DISPLAYSURF.fill(BGCOLOR)

    # draw the board

    while True:
        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        
        # when you hover over a row that is not fill, the row highlights
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
        
def generateNewBoard() -> list[list]:
    return [
        [None] * BOARDWIDTH
    ] * BOARDHEIGHT


def generateNewBoardState() -> list[int]:
    return [5] * BOARDWIDTH


def checkIfBoardIsFill(state) -> bool:
    for row in state:
        if row != -1:
            return False
    return True


def inbounds(x, y) -> bool:
    return (0 <= x < BOARDWIDTH) and (0 <= y < BOARDHEIGHT)

def checkIfLine(x, y, color, board) -> bool:
    DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

    queue = deque()
    queue.append((x, y, 1))
    visited = set()
    visited.add((x, y))

    while queue:
        row, col, step = queue.pop()

        if step == 4:
            return True
        
        for dr, dc in DIRECTIONS:
            new_row, new_col = row + dr, col + dc
            coor = (new_row, new_col)
            if inbounds(new_row, new_col) and board[new_row][new_col] == color and coor not in visited:
                visited.add(coor)
                queue.append((new_row, new_col, step + 1))
        
    return False

