import pygame

class Shape:
    def __init__(self, game):
        self.game = game
        self.shape = pygame.Rect(0, game.screen_height / 2 - 50, 100, 100)
        self.move_speed = 200
        self.x_direction = 1
        self.y_direction = 1
        self.pos = pygame.math.Vector2(self.shape.topleft)

    def move(self, dt):
        self.pos.x += self.x_direction * self.move_speed * dt
        self.pos.y += self.y_direction * self.move_speed * dt
        self.shape.x = round(self.pos.x)
        self.shape.y = round(self.pos.y)

        self.constrain_to_screen()
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.shape)

    def constrain_to_screen(self):
        if self.shape.right > self.game.screen_width or self.shape.left < 0:
            self.x_direction *= -1
        if self.shape.bottom > self.game.screen_height or self.shape.top < 0:
            self.y_direction *= -1
