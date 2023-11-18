import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
PADDING = 10

RED = (248, 200, 220)
WHITE = (245, 245, 245)
# RED = (255, 0, 0)
# WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (144, 238, 144)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44,25))
REDPLAYER = pygame.transform.scale(pygame.image.load('assets/red_flower.png'), (SQUARE_SIZE - 2 * PADDING, SQUARE_SIZE - 2 * PADDING))
WHITEPLAYER = pygame.transform.scale(pygame.image.load('assets/white_flower.png'), (SQUARE_SIZE - 2 * PADDING, SQUARE_SIZE - 2 * PADDING))



