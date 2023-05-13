import sys
import pygame


class MainWindow:
    def __init__(self):
        pygame.init()
        self.bg = pygame.image.load("chess-board-closeup-background-35435497.jpg")
        self.bg_rect = self.bg.get_rect()
        size = self.bg.get_size()
        self.DS = pygame.display.set_mode(size)
        pygame.display.set_caption("Chess Game")

    def main_game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.DS.blit(self.bg,
                         self.bg_rect)
            pygame.display.flip()


main_window = MainWindow()
main_window.main_game_loop()
