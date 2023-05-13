import sys
import pygame


class MainWindow:
    def __init__(self):
        pygame.init()

        self.ball = pygame.image.load("ball.png")
        self.ballRect = self.ball.get_rect()
2ge.load("myrock.jpg")
        self.backgroundRect = self.background.get_rect()

        self.width = self.backgroundRect.width
        self.height = self.backgroundRect.height

        self.speed = [5, 4]

        self.DISPLAYSURF = pygame.display.set_mode(self.background.get_size())
        pygame.display.set_caption("Look At My Rock!")

    def main_game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.ballRect = self.ballRect.move(self.speed)
            if self.ballRect.left < 0 or self.ballRect.right > self.width:
                self.speed[0] = -self.speed[0]
            if self.ballRect.top < 0 or self.ballRect.bottom > self.height:
                self.speed[1] = -self.speed[1]
            self.DISPLAYSURF.blit(self.background, self.backgroundRect)
            self.DISPLAYSURF.blit(self.ball, self.ballRect)
            pygame.display.flip()


main_game = MainWindow()
main_game.main_game_loop()
