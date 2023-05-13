#!/usr/local/bin/python3.7

import pygame
import sys
import random


class MySprite:
    def __init__(self, image, location):
        self.the_image = pygame.image.load(image)
        self.the_rect = self.the_image.get_rect()
        self.the_rect.left = location[0]
        self.the_rect.top = location[1]

    def blit(self, the_surface):
        the_surface.blit(self.the_image, self.the_rect)

    def check_collision(self, the_sprite):
        return self.the_rect.colliderect(the_sprite.the_rect)


class Ghost(MySprite):
    def __init__(self, image, location):
        super().__init__(image, location)

        self.speed = [random.randint(-2, 2), random.randint(-2, 2)]

    def move(self):
        self.the_rect = self.the_rect.move(self.speed)

    def check_edge(self, width, height):
        if self.the_rect.left < 0 or self.the_rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.the_rect.top < 0 or self.the_rect.bottom > height:
            self.speed[1] = -self.speed[1]


class Player(MySprite):
    def __init__(self, image, location):
        super().__init__(image, location)

    def move_left(self):
        check = self.the_rect.left - 5
        if check > 0:
            self.the_rect.left = check

    def move_right(self, edge):
        check = self.the_rect.right + 5
        if check < edge:
            self.the_rect.right = check

    def move_up(self):
        check = self.the_rect.top - 5
        if check > 0:
            self.the_rect.top = check

    def move_down(self, edge):
        check = self.the_rect.bottom + 5
        if check < edge:
            self.the_rect.bottom = check


class MainWindow:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10, 10)
        self.width = 1200
        self.height = 700
        size = (self.width, self.height)
        self.DISPLAYSURF = pygame.display.set_mode(size)
        pygame.display.set_caption("FireTech")

        self.player = Player("player.png", (300, 300))
        self.ghost = Ghost("ghost.png", (100, 100))

    def main_game_loop(self):
        while True:  # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right(self.width)
                    elif event.key == pygame.K_UP:
                        self.player.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.player.move_down(self.height)
            self.DISPLAYSURF.fill([0, 0, 0])
            self.ghost.move()
            self.ghost.check_edge(self.width, self.height)
            if self.player.check_collision(self.ghost):
                self.player.the_rect.left = 0
                self.player.the_rect.top = 0
            self.ghost.blit(self.DISPLAYSURF)
            self.player.blit(self.DISPLAYSURF)
            pygame.display.update()
            pygame.display.flip()


my_game = MainWindow()
my_game.main_game_loop()
