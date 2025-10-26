import pygame
from game_dev_tools import GameEntityAppearance, Circle, Rectangle
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class PlayerProjectileAppearance(GameEntityAppearance):
    def __init__(self, shapes: list, game_entity):
        super().__init__(shapes)
        self.game_entity=game_entity

    def draw(self):
        game_entity = self.game_entity
        #self.draw_game_entity_primary_shape()
        surf = game_entity.target_surf

        pos = game_entity.pos
        radius = game_entity.radius


        #Rectangle().draw(surf,rect_color,pos, width_height)
        #pygame.draw.rect(surf, (0, 255, 0), game_entity.rect)

        Circle(surf,pos,radius).draw()
