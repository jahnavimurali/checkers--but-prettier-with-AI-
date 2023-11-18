import pygame
from .constants import RED, SQUARE_SIZE, CROWN, REDPLAYER, WHITEPLAYER


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0 
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        if self.color == RED:
            win.blit(REDPLAYER, (self.x - REDPLAYER.get_width() // 2, self.y - REDPLAYER.get_height() // 2))
        else:
            win.blit(WHITEPLAYER, (self.x - WHITEPLAYER.get_width() // 2, self.y - WHITEPLAYER.get_height() // 2))
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y-CROWN.get_width()//2))
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)



