import random
from .values import *


class Obstacle:
    def __init__(self, x: int, width: int):
        self.x = x
        self.width = width
        self.y_top = 0
        self.height_top = random.randint(150, 250)
        self.space = 200
        self.y_bottom = self.height_top + self.space
        self.height_bottom = HEIGHT - self.y_bottom
        self.color = (21, 3, 51)
        self.upper_rect = pygame.Rect(self.x, self.y_top, self.width, self.height_top)
        self.lower_rect = pygame.Rect(self.x, self.y_bottom, self.width, self.height_bottom)

    def reset_obstacles(self):
        self.upper_rect = pygame.Rect(self.x, self.y_top, self.width, self.height_top)
        self.lower_rect = pygame.Rect(self.x, self.y_bottom, self.width, self.height_bottom)

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self.upper_rect, 0)
        pygame.draw.rect(SCREEN, self.color, self.lower_rect, 0)

    def movement(self, v: float):
        self.x = self.x - v
        self.reset_obstacles()

    def collision(self, player):
        if self.upper_rect.colliderect(player) or self.lower_rect.colliderect(player):
            return True
        else:
            return False
