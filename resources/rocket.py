from .values import *


class Rocket:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 105
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.realpath('media/rocket.png'))

    def movement(self, v: int):
        self.y = self.y + v
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        SCREEN.blit(self.graphics, (self.x, self.y))
