import sys
from time import time

import pygame
from {{cookiecutter.pyproject_slug}} import settings
from {{cookiecutter.pyproject_slug}}.shape import Shape

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("{{cookiecutter.project_slug}}")
        self.screen_width = settings.SCREEN_WIDTH
        self.screen_height = settings.SCREEN_HEIGHT
        self.fps = settings.FPS
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.fill_screen()
        self.clock = pygame.time.Clock()
        self.start_time = time()
        self.dt = self.start_time
        self.playing = True

    def fill_screen(self):
        self.screen.fill((0, 0, 0))

    def update_dt(self):
        new_time = time()
        self.dt = new_time - self.start_time
        self.start_time = new_time

def main():
    game = Game()
    shape = Shape(game)

    while game.playing:
        game.update_dt()
        game.fill_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                pygame.quit()
                sys.exit()
        shape.move(game.dt)
        pygame.display.flip()
        game.clock.tick(game.fps)

if __name__ == "__main__":
    main()
