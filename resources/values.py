import pygame
import os

pygame.init()
game = True

WIDTH = 600
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_GAME = pygame.image.load(os.path.realpath('media/background.jpg'))
BACKGROUND_MENU = pygame.image.load(os.path.realpath('media/menu_background.jpg'))

mode = "menu"
obstacles = []
dy = 1
points = 0
