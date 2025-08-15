import math
import pygame
import sys
from settings import *
from entities import *

class Game:

    def __init__(self):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.time = 0.0
        self.clock = pygame.time.Clock() # Object to help track time
        self.running = True
        self.dt = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.time = pygame.time.get_ticks() / 1000  # temps écoulé en millisecondes depuis appel de pygame.init()

        #Logique de jeu (collisions, score, etc.)
        self.check_collisions()

    def check_collisions(self):
        # Logique de collision



    def reinitialize_after_collision(self):
        self.player.color = self.player.normal_color
        self.player2.color = self.player2.normal_color

    @staticmethod
    def find_collision_point_of_circles(circles: list):
        if not isinstance(circles, list):
            raise TypeError("L'argument doit être une liste")
        if len(circles) < 2 or len(circles) > 2:
            raise ValueError("La liste doit contenir 2 élements")

        angle1 = math.atan2(circles[1].position[1] - circles[0].position[1], circles[1].position[0] - circles[0].position[0])
        angle2 = angle1 + math.pi

        #angle3 = math.atan2(circles[0].position[1] - circles[1].position[1], circles[0].position[0] - circles[1].position[0])
        #angle4 = angle3 + math.pi

        collision_point_x = circles[0].position[0] + circles[0].radius * math.cos(angle1)
        collision_point_y = circles[0].position[1] + circles[0].radius * math.sin(angle1)

        collision_point = pygame.Vector2(collision_point_x,collision_point_y)
        #collision_point2_x = circles[0].position[0] + circles[0].radius * math.cos(angle3)
        #c#ollision_point2_y = circles[0].position[1] + circles[0].radius * math.sin(angle3)

        return collision_point

    def find_collision_opposite_point_of_circles(self,circles: list):

        if not isinstance(circles, list):
            raise TypeError("L'argument doit être une liste")
        if len(circles) < 2 or len(circles) > 2:
            raise ValueError("La liste doit contenir 2 élements")

        angle3 = self.find_collision_opposite_point_angle(circles)
        angle4 = angle3 + math.pi

        collision_opposite_point_x = circles[0].position[0] + circles[0].radius * math.cos(angle3)
        collision_opposite_point_y = circles[0].position[1] + circles[0].radius * math.sin(angle3)

        collision_opposite_point = pygame.Vector2(collision_opposite_point_x,collision_opposite_point_y)
        return collision_opposite_point

    @staticmethod
    def find_collision_opposite_point_angle(circles):
        collision_opposite_point_angle = math.atan2(circles[0].position[1] - circles[1].position[1],
                   circles[0].position[0] - circles[1].position[0])
        return collision_opposite_point_angle

    def change_player_direction(self):
        # pointer la nouvelle direction vers le point opposé au point de collision
        player = self.player
        player2 = self.player2

        collision_point = self.find_collision_point_of_circles([player,player2])
        collision_opposite_point = self.find_collision_opposite_point_of_circles([player,player2])

        player_direction = collision_point - collision_opposite_point
        #print (player_direction)

        #player.position.x =
        player.velocity.x = math.cos(Game.find_collision_opposite_point_angle([player,player2])) * player.speed_after_collision
        player.velocity.y = math.sin(Game.find_collision_opposite_point_angle([player, player2])) * player.speed_after_collision

    def draw(self):

        self.window.fill(color_palette['background'])

        #self.check_collisions()  # si cette fonction est appelé ici les lignes horizontales et verticales s'affichent

        #self.all_sprites.draw(self.window)
        # Dessiner l'ui (score, vies, etc.)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.dt = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

