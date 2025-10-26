from math import atan2, degrees

import pygame
from pygame import Vector2

from imports import *
from entities import *
from movement_systems import *
from game_entities_appearance import *
from game_dev_tools import *

class Game:
    def __init__(self):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.font = pygame.font.Font(None, DEFAULT_FONT_SIZE)
        self.time = 0.0
        self.clock = pygame.time.Clock() # Object to help track time
        self.running = True
        self.dt = 0

        self.background = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background.fill(color_palette['background'])

        self.visual_helper = VisualHelper(self.window)
        #self.surf_factory = PygameSurfaceFactory(self.window, 3,3)
        #self.surf_factory.create_surfaces()

        self.game_entities = [] # Stocker les entités pour update et draw d'un seul coup sans modifier à chaque fois
        # exemple dans update() :
        # for i in range(len(self.game_entities)):
        #       self.game_entities[i].update()

        self.collision_count = 0

        window_center = pygame.Vector2(self.window.get_rect().center)

        self.player = Player(self.window,pygame.Vector2(0,0))
        print(self.window)
        self.player.movement_system = MouseMovementSystem(self.player, self.window)
        self.player.game_entity_appearance = PlayerAppearance8([], self.player)
        self.player.radius = 100
        #self.player.central_shape.radius = self.player.radius
        #p_radius = self.player.central_shape.radius
        p_radius = self.player.radius
        p_pos = self.player.pos
        self.player.rect = pygame.Rect(p_pos, (p_radius*2, p_radius*2))
        self.player.rect.center = p_pos

        #self.player.central_shape.rect = pygame.Rect(p_pos, (p_radius * 2, p_radius * 2))
        #self.player.central_shape.rect.center = p_pos
        self.player.border_width = 1
        self.game_entities.append(self.player)

        self.player_projectile = PlayerProjectile(self.window, window_center)
        self.player_projectile.movement_system = PlayerProjectileMovementSystem(self.player_projectile, self.window)
        self.player_projectile.game_entity_appearance = PlayerProjectileAppearance([],self.player_projectile)
        self.player_projectile.radius= 50

        #self.player_projectile.central_shape.radius = self.player_projectile.radius
        #pp_radius = self.player_projectile.central_shape.radius

        pp_radius = self.player_projectile.radius
        pp_pos = self.player_projectile.pos
        width_height = (pp_radius * 2, pp_radius * 2)
        self.player_projectile.rect = pygame.Rect(pp_pos, width_height)
        self.player_projectile.rect.center = pp_pos

        # self.player_projectile.central_shape.rect = pygame.Rect(pp_pos, (pp_radius*2, pp_radius*2))
        # self.player_projectile.central_shape.rect.center = pp_pos

        self.player_projectile.color = (255,0,0)
        self.player_projectile.speed = 4

        self.game_entities.append(self.player_projectile)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.time = pygame.time.get_ticks() / 1000  # temps écoulé en millisecondes depuis appel de pygame.init()
        #Logique de jeu (collisions, score, etc.)
        #self.surf_factory.fill_surfaces()

        for i in range(len(self.game_entities)):
            self.game_entities[i].update(self.dt)

        self.check_collisions()

    def check_collisions(self):
        # Logique de collision
        # if pygame.sprite.collide_circle(self.player.central_shape, self.player_projectile.central_shape):
        #print(f" player rect : {self.player.rect}")
        #print(f" player projectile rect : {self.player_projectile.rect}")
        if pygame.sprite.collide_circle(self.player, self.player_projectile):
            collision_vector = self.player_projectile.pos - self.player.pos
            current_speed = self.player_projectile.velocity.length()

            if current_speed == 0:
                current_speed = self.player_projectile.speed

            # SÉPARER les sprites d'abord
            distance = collision_vector.length()
            overlap = (self.player.radius + self.player_projectile.radius) - distance

            if overlap > 0:
                # Pousser le projectile hors du joueur
                separation = collision_vector.normalize() * overlap
                self.player_projectile.pos += separation

            n = collision_vector.normalize()

            self.player_projectile.velocity = n * current_speed

    def draw(self):
        self.window.blit(self.background)

        for i in range(len(self.game_entities)):
            self.game_entities[i].draw()

        #self.surf_factory.blit_surfaces()
        # Dessine sur window
        #self.visual_helper.draw_dots(4, 4)
        #self.visual_helper.draw_grid(3, 3)
        # Dessiner l'ui (score, vies, etc.)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

