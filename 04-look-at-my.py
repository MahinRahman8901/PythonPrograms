import sys
import pygame


class MySprite:
    def __init__(self, image, speed, location):
        self.the_image = pygame.image.load(image)
        self.the_rect = self.the_image.get_rect()
        self.the_rect.left = location[0]
        self.the_rect.top = location[1]

        self.speed = speed

    def move(self):
        self.the_rect = self.the_rect.move(self.speed)

    def check_edge(self, width, height):
        if self.the_rect.left < 0 or self.the_rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.the_rect.top < 0 or self.the_rect.bottom > height:
            self.speed[1] = -self.speed[1]

    def blit(self, the_surface):
        the_surface.blit(self.the_image, self.the_rect)


class MainWindow:
    def __init__(self):
        pygame.init()

        self.background = pygame.image.load("myrock.jpg")
        self.background_rect = self.background.get_rect()

        self.ball = MySprite("ball.png", [2, 1], (300, 300))
        

        self.width = self.background_rect.width
        self.height = self.background_rect.height

        self.DISPLAYSURF = pygame.display.set_mode(self.background.get_size())
        pygame.display.set_caption("Look At My Rock!")

    def main_game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.ball.move()
            self.ball.check_edge(self.width, self.height)
            self.DISPLAYSURF.blit(self.background, self.background_rect)
            self.ball.blit(self.DISPLAYSURF)
            pygame.display.flip()


main_game = MainWindow()
main_game.main_game_loop()
