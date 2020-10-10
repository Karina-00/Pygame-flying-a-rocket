import pygame
import os

pygame.init()
pygame.display.set_caption('Space Game')
game = True

WIDTH = 700
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_GAME = pygame.image.load(os.path.realpath('media/background.jpg'))
BACKGROUND_MENU = pygame.image.load(os.path.realpath('media/menu_background.jpg'))
OBS_NR = 20
rocket_step = 0.7

mode = "menu"
obstacles = []
dy = rocket_step
points = 0
