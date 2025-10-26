import pygame
from entities import *
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from game_dev_tools import GameEntity

class PlayerProjectile(GameEntity):
    # Modifier le mode d'instanciation pour permettre l'initialisation des attributss aprés instanciation
    def __init__(self, target_surf, pos, angle_increment=45, velocity=pygame.Vector2(0,0), speed=1,
                 color=(255, 255, 255), border_width=0, delta_time=0):
        # La forme et le systeme de mouvement sont instanciés dans chaque enfant de GameEntity
        super().__init__(target_surf,pos)
        self.delta_time = delta_time
        self.border_width = border_width

    def handle_input(self):
        pass

    def update(self, dt):
        self.movement_system.move(dt)

    def draw(self):
        self.game_entity_appearance.draw()