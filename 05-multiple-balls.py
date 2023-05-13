import sys
import pygame
import random


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

        self.width = self.background_rect.width
        self.height = self.background_rect.height

        self.balls = []
        for i in range(10):
            the_speed = [random.randint(-5, 5), random.randint(-5, 5)]
            starting_point = [random.randint(10, self.width-100),
                              random.randint(10, self.height-100)]
            self.balls.append(MySprite("ball.png", the_speed, starting_point))

        self.DISPLAYSURF = pygame.display.set_mode(self.background.get_size())
        pygame.display.set_caption("Look At My Rock!")

    def main_game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.DISPLAYSURF.blit(self.background, self.background_rect)
            for ball in self.balls:
                ball.move()
                ball.check_edge(self.width, self.height)
                ball.blit(self.DISPLAYSURF)
            pygame.display.flip()


main_game = MainWindow()
main_game.main_game_loop()
