from difflib import Match
from operator import truediv
from pdb import line_prefix
import pygame as py
import sys

py.init()

#screen size
size = width, height = 600,600

#rgb main colors
BG_COLOR = 8,127,140
LINE_COLOR = 9,52,56
FIGURE_COLOR = 173,52,62

#init of screen
screen = py.display.set_mode(size)
py.display.set_caption('TİC TAC TOE')

#board
board = [[0,0,0],[0,0,0],[0,0,0]]

#turn
player = 1

def markSquare(col,row,player):
    if board[col][row] == 0:
        board[col][row] = player         
    pass

def drawLines():
    py.draw.line(screen, LINE_COLOR, (200,0), (200,600), 10)
    py.draw.line(screen, LINE_COLOR, (400,0), (400,600), 10)
    py.draw.line(screen, LINE_COLOR, (0,200), (600,200), 10)
    py.draw.line(screen, LINE_COLOR, (0,400), (600,400), 10)
    pass

def drawCircle(x,y):
    py.draw.circle(screen, FIGURE_COLOR, (x,y), 70)
    py.draw.circle(screen, BG_COLOR, (x,y), 55)
    pass

def drawCross(x,y):
    py.draw.line(screen, FIGURE_COLOR, (x-70,y-70), (x+70,y+70), 20)
    py.draw.line(screen, FIGURE_COLOR, (x+70,y-70), (x-70,y+70), 20)
    pass

def drawElem():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                drawCross(i*200+100,j*200+100) 
            elif board[i][j] == 2:
                drawCircle(i*200+100,j*200+100)

def checkWin(player):
    for i in range(3):
        #horizontal win
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            py.draw.line(screen, FIGURE_COLOR, (i*200+100,20), (i*200+100,580), 15)
            return True
        #vertical win
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:   
            py.draw.line(screen, FIGURE_COLOR, (20,i*200+100), (580,i*200+100), 15)
            return True
    #diogonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        py.draw.line(screen, FIGURE_COLOR, (20,20), (580,580), 15)
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        py.draw.line(screen, FIGURE_COLOR, (580,20), (20,580), 15)
        return True
    return False

def restart():
    for i in range(3):
        for j in range(3):
            board[i][j] = 0

    screen.fill(BG_COLOR)
    drawLines()



screen.fill(BG_COLOR)
drawLines()
gameEnd = False    
while 1:
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()
        if not gameEnd:
            if event.type == py.MOUSEBUTTONDOWN:
                mouseX,mouseY = py.mouse.get_pos()
            
                clickedCol = int(mouseX // 180)
                clickedRow = int(mouseY // 180)
                if clickedCol == 3:
                    clickedCol =2
                if clickedRow == 3:
                    clickedRow =2    

                if player ==1:
                    markSquare(clickedCol,clickedRow,player)
                    gameEnd = checkWin(player)
                    player = 2
                elif player == 2:
                    markSquare(clickedCol,clickedRow,player)
                    gameEnd = checkWin(player)
                    player =1    
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                restart()
                player = 1
                gameEnd = False    



    drawElem()
    py.display.update()