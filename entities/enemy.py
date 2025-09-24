from imports import pygame
import math
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, color_palette

class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen:pygame.Surface, x, y):
        super().__init__()
        self.circle = None
        self.screen = screen
        self.position = pygame.Vector2(x,y)
        self.normal_color = color_palette['enemy']
        self.little_circles_color =  color_palette['enemy_little_circle']
        self.radius = 120
        self.second_circle_radius = 60
        self.little_circles_radius = 20
        self.border_width = 1

    def update(self):
        pass

    def draw(self):
        time = pygame.time.get_ticks() / 1000

        variable_radius1 = self.radius * -math.sin(time)
        variable_radius2 = self.second_circle_radius * math.sin(time)
        #Cercles principaux
        pygame.draw.circle(self.screen, self.normal_color, self.position, variable_radius1, self.border_width)
        pygame.draw.circle(self.screen, self.normal_color, self.position, variable_radius2, self.border_width)

        # Petits cercles en mouvement circulaire
        angle = 0

        rotation_speed = 0.1
        little_circles_quantity = 4
        for i in range(1,9):
            x = self.position.x + variable_radius2 * math.cos((-time * rotation_speed)+ angle)
            y = self.position.y + variable_radius2 * math.sin((-time * rotation_speed) + angle)
            pygame.draw.circle(self.screen, self.normal_color, (x, y), self.little_circles_radius)
            pygame.draw.circle(self.screen, self.little_circles_color, (x, y), self.little_circles_radius, 1)
            angle += math.pi /4


        angle = 0

        for i in range(1,17):
            x = self.position.x + variable_radius1 * math.cos((time * rotation_speed)+ angle)
            y = self.position.y + variable_radius1 * math.sin((time * rotation_speed) + angle)
            pygame.draw.circle(self.screen, self.normal_color, (x, y), self.little_circles_radius)
            pygame.draw.circle(self.screen, self.little_circles_color, (x, y), self.little_circles_radius, 1)
            angle += math.pi / 8

# class Enemy2(pygame.sprite.Sprite):
#     def __init__(self, window:pygame.Surface):
#         super().__init__()
#         self.circle = None
#         self.window = window
#         self.position = pygame.Vector2(DISPLAY_WIDTH,0)
#         self.normal_color = color_palette['enemy']
#         self.radius = 120
#         self.border_width = 3
#
#     def update(self):
#         pass
#
#     def draw(self):
#         pygame.draw.circle(self.window, self.normal_color, self.position, self.radius, self.border_width)
#
# class Enemy3(pygame.sprite.Sprite):
#     def __init__(self, window:pygame.Surface):
#         super().__init__()
#         self.circle = None
#         self.window = window
#         self.position = pygame.Vector2(0,DISPLAY_HEIGHT)
#         self.normal_color = color_palette['enemy']
#         self.radius = 120
#         self.border_width = 3
#
#     def update(self):
#         pass
#
#     def draw(self):
#         pygame.draw.circle(self.window, self.normal_color, self.position, self.radius, self.border_width)
#
# class Enemy4(pygame.sprite.Sprite):
#     def __init__(self, window:pygame.Surface):
#         super().__init__()
#         self.circle = None
#         self.window = window
#         self.position = pygame.Vector2(DISPLAY_WIDTH,DISPLAY_HEIGHT)
#         self.normal_color = color_palette['enemy']
#         self.radius = 120
#         self.border_width = 3
#
#     def update(self):
#         pass
#
#     def draw(self):
#         pygame.draw.circle(self.window, self.normal_color, self.position, self.radius, self.border_width)