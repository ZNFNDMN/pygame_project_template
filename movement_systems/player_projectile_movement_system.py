import pygame
from game_dev_tools import  MovementSystem
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class PlayerProjectileMovementSystem(MovementSystem):
    def __init__(self, game_entity, surface):
        super().__init__(game_entity, surface)

    def move(self,dt):
        game_entity = self.game_entity

        self.keep_on_screen()

        game_entity.pos += game_entity.velocity * game_entity.speed
        game_entity.rect.center = game_entity.pos

    def keep_on_screen(self):
        game_entity = self.game_entity
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()

        # Vérifier et corriger la position + rebond réaliste
        if game_entity.pos.x - game_entity.radius <= 0:
            game_entity.pos.x = game_entity.radius  # Repositionner
            game_entity.velocity.x = abs(game_entity.velocity.x)  # Rebond vers la droite

        if game_entity.pos.x + game_entity.radius >= surface_width:
            game_entity.pos.x = surface_width - game_entity.radius
            game_entity.velocity.x = -abs(game_entity.velocity.x)  # Rebond vers la gauche

        if game_entity.pos.y - game_entity.radius <= 0:
            game_entity.pos.y = game_entity.radius
            game_entity.velocity.y = abs(game_entity.velocity.y)  # Rebond vers le bas

        if game_entity.pos.y + game_entity.radius >= surface_height:
            game_entity.pos.y = surface_height - game_entity.radius
            game_entity.velocity.y = -abs(game_entity.velocity.y)  # Rebon
