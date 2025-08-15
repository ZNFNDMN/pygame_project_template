import math
import pygame
import sys
from settings import *
from entities import Player, Player2, Enemy

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
        self.dt = 0 #?

        self.player = Player(self.window)
        self.player2 = Player2(self.window)
        self.collision_not_happened = False
        self.enemy1 = Enemy(self.window, 0 + 200, 0 + 200)
        self.enemy2 = Enemy(self.window, WINDOW_WIDTH, 0)
        self.enemy3 = Enemy(self.window, 0, WINDOW_HEIGHT)
        self.enemy4 = Enemy(self.window, WINDOW_WIDTH, WINDOW_HEIGHT)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if not (event.type == pygame.APPMOUSEFOCUS) and self.time <=1: # Si le jeu n'a pas le focus
                pygame.event.set_grab(True)  # Capture le curseur
                pygame.mouse.set_visible(False)

            if self.time > int(1): #Aprés 1 seconde de jeu le joueur 2 suit la souris
                self.player2.position = list(pygame.mouse.get_pos())

    def update(self):
        self.time = pygame.time.get_ticks() / 1000  # temps écoulé en millisecondes depuis appel de pygame.init()

        self.player.update(self.dt)
        self.player2.update(self.dt)

        #Logique de jeu (collisions, score, etc.)
        self.check_collisions()

    def check_collisions(self):
        # Logique de collision
        if Game.players_collide([self.player, self.player2]):
            self.draw_players_collision()
            self.change_player_direction()
        else:
            # réinitialiser valeurs modifiés pendant collision
            self.reinitialize_after_collision()

    @staticmethod
    def players_collide(sprites):
        #dx = self.player.position[0] - self.player2.position[0]
        dx = sprites[0].position[0] -  sprites[1].position[0]
        #dy = self.player.position[1] - self.player2.position[1]
        dy = sprites[0].position[1] -  sprites[1].position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)

        #if distance <= self.player.radius + self.player2.radius: return True
        if distance <= sprites[0].radius + sprites[1].radius: return True
        else: return False

    def draw_players_collision(self):
        player = self.player
        player2 = self.player2

        player.color = player.collision_color
        player2.color = player2.collision_color

        # trouver point de collision entre 2 cercles
        collision_point = self.find_collision_point_of_circles([player, player2])

        # trouver le point opposé au point de collision
        collision_opposite_point = self.find_collision_opposite_point_of_circles([player, player2])

        # Dessiner un cercle plein autour du point de collision
        pygame.draw.circle(self.window, color_palette['text'], (collision_point.x, collision_point.y), 5)

        # Dessiner un cercle plein autour du point opposé au point de collision
        pygame.draw.circle(self.window, color_palette['text'], (collision_opposite_point.x, collision_opposite_point.y), 5)

        #lignes du point de collision
        pygame.draw.line(self.window, color_palette['primary'], (collision_point.x, 0),
                         (collision_point.x, WINDOW_HEIGHT), 1)
        pygame.draw.line(self.window, color_palette['primary'], (0, collision_point.y), (WINDOW_WIDTH, collision_point.y),
                         1)

        # lignes du point opposé
        pygame.draw.line(self.window, color_palette['text'], (collision_opposite_point.x, 0),
                         (collision_opposite_point.x, WINDOW_HEIGHT), 1)
        pygame.draw.line(self.window, color_palette['text'], (0, collision_opposite_point.y), (WINDOW_WIDTH, collision_opposite_point.y),
                         1)

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
        player = self.player
        player2 = self.player2
        enemy1 = self.enemy1
        enemy2 = self.enemy2
        enemy3 = self.enemy3
        enemy4 = self.enemy4

        self.window.fill(color_palette['background'])

        #self.check_collisions()  # si cette fonction est appelé ici les lignes horizontales et verticales s'affichent

        player.draw()
        player2.draw()
        enemy1.draw()
        enemy2.draw()
        enemy3.draw()
        enemy4.draw()

        txt1 = self.font.render(f"player velocity x : {player.velocity.x}", True, color_palette['text'])
        txt2 = self.font.render(f"player velocity y : {player.velocity.y}", True, color_palette['text'])
        txt3 = self.font.render(f"player speed : {player.speed}", True, color_palette['text'])
        txt4 = self.font.render(f"player position x : {player.position.x}", True, color_palette['text'])
        txt5 = self.font.render(f"player position y : {player.position.y}", True, color_palette['text'])
        txt6 = self.font.render(f"time : {self.time}", True, color_palette['text'])
        txt7 = self.font.render(f"dt : {self.dt}", True, color_palette['text'])

        #self.window.blit(txt1, (0,0))
        #self.window.blit(txt2, (0,24))
        #self.window.blit(txt3, (0,48))
        #self.window.blit(txt4, (0,72))
        #self.window.blit(txt5, (0,96))
        #self.window.blit(txt6, (DISPLAY_WIDTH - 150,0))
        #self.window.blit(txt7, (DISPLAY_WIDTH - 150,24))

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

