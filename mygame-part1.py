import pygame
import sys


class MySprite:
    def __init__(self, image, location):
        self.the_image = pygame.image.load(image)
        self.the_rect = self.the_image.get_rect()
        self.the_rect.left = location[0]
        self.the_rect.top = location[1]

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

    def blit(self, the_surface):
        the_surface.blit(self.the_image, self.the_rect)


class MainWindow:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10, 10)
        self.width = 700
        self.height = 700
        size = (self.width, self.height)
        self.DISPLAYSURF = pygame.display.set_mode(size)
        pygame.display.set_caption("FireTech")

        self.ball = MySprite("player.png", (300, 300))

    def main_game_loop(self):
        while True:  # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ball.move_left()
                    # if it's the right arrow
                    elif event.key == pygame.K_RIGHT:
                        self.ball.move_right(self.width)
                    # if it's the up arrow
                    elif event.key == pygame.K_UP:
                        self.ball.move_up()
                    # if it's the down arrow
                    elif event.key == pygame.K_DOWN:
                        self.ball.move_down(self.height)
            self.DISPLAYSURF.fill([0, 0, 0])
            self.ball.blit(self.DISPLAYSURF)
            pygame.display.update()
            pygame.display.flip()


my_game = MainWindow()
my_game.main_game_loop()
