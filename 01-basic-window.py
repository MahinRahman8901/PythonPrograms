import pygame
import sys


class MainWindow:
    def __init__(self):
        pygame.init()
        size = (1200, 1300)
        self.DISPLAYSURF = pygame.display.set_mode(size)
        pygame.display.set_caption('Hello World!')

    @staticmethod
    def main_game_loop():
        while True:  # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


game = MainWindow()
game.main_game_loop()
