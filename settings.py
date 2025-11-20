from color_palettes import *
from imports import pygame

#pygame setup
pygame.init()

# window setup
screen_width_percentage = 0.7
screen_height_percentage = 0.8
WINDOW_WIDTH = pygame.display.Info().current_w * screen_width_percentage
WINDOW_HEIGHT = pygame.display.Info().current_h * screen_height_percentage

WINDOW_TITLE = "draft"
DEFAULT_FONT_SIZE = 24

FPS = 60

#Couleurs
color_palette = CLASSIC

# Gameplay
PLAYER_SPEED = 300
ENEMY_SPEED = 100

CONTROLS = {
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT
}


