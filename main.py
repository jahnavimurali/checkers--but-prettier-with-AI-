import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED
from checkers.game import Game
from minimax.algorithm import minimax_alpha_beta, minimax, minimax_for_red

FPS = 60 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        

        if game.turn == WHITE:
            # higher the depth, better the AI, more computationally expensive
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            # value, new_board = minimax_alpha_beta(game.get_board(), 5, float('-inf'), float('inf'), WHITE, game)
            game.ai_move(new_board)

        # AI Vs AI
        # pygame.time.delay(100)
            
        # if game.turn == RED:
        #     value, new_board = minimax_for_red(game.get_board(), 3, RED, game)
        #     if new_board == game.board:
        #         print("GAME OVER")
        #         run = False
        #         break
        #     game.ai_move(new_board)

        # if not game.board:
        #     print("GAME OVER!")
        #     run = False
        #     break
            

        if game.winner() != None:
            if game.winner() == WHITE:
                print("AI WINS!!!")
            elif game.winner() == RED:
                print("YOU WIN!!!")
            else:
                print("GAME OVER!")
                pygame.time.delay(5000)

            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        pygame.display.update()

    pygame.quit()

main()
