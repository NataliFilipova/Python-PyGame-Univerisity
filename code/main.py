import sys
from Button import *
from code import game
from game import *


# Pygame setup
pygame.init()
pygame.display.set_caption('Runner')  # title of the game*-

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

game = Game(screen)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.open_menu()

    pygame.display.update()
    clock.tick(60)
