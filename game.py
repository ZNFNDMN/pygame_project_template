import pygame

from imports import *
#from entities import *
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
        self.surf_factory = PygameSurfaceFactory(self.window, 2,2)
        self.surf_factory.create_surfaces()

        #############################################
        sub_surf0  = self.surf_factory.surf_list[0]
        sub_surf_center = sub_surf0.get_rect().center

        self.player = Player(sub_surf0,pygame.Vector2(sub_surf_center), Circle())
        self.player.movement_system = KeyboardMovementSystem(self.player, sub_surf0) #passer l'instance de player pour pouvoir modif la position
        self.player.game_entity_appearence = PlayerAppearance3([], self.player)
        self.player.size = 40
        self.player.color = (255,0,0)
        # ###############################################
        # sub_surf1 = self.surf_factory.surf_list[1]
        # # Définir la shape et movement system ici pour avoir le controle
        # circle2 = Circle((255, 0, 255))
        #
        # self.player2 = Player(sub_surf1, pygame.Vector2(sub_surf_center), circle2, pygame.Vector2(0,0),5)
        # # initialisation du movement system aprés instanciation du player
        # self.player2.movement_system = KeyboardMovementSystem(self.player2, sub_surf1)  # passer l'instance de player pour pouvoir modif la position
        ################################################################
        sub_surf2 = self.surf_factory.surf_list[2]

        self.player3 = Player(sub_surf2, pygame.Vector2(sub_surf_center), Circle())
        self.player3.movement_system = KeyboardMovementSystem(self.player3, sub_surf2)
        self.player3.game_entity_appearence = PlayerAppearence([], self.player3)
        self.player3.size=20
        self.player3.border_width = 1
        self.player3.speed=5

        ########################################################
        sub_surf1  = self.surf_factory.surf_list[1]

        self.player4  = Player(sub_surf1,pygame.Vector2(sub_surf_center), Circle())
        self.player4.movement_system = KeyboardMovementSystem(self.player4, sub_surf1)
        self.player4.game_entity_appearence = PlayerAppearance4([], self.player4)
        self.player4.size = 50
        self.player4.border_width = 1
        self.player4.speed = 10

        ##########################################################
        sub_surf3 = self.surf_factory.surf_list[3]

        self.player5 = Player(sub_surf3, pygame.Vector2(sub_surf_center), Circle())
        self.player5.game_entity_appearence = PlayerAppearance5([], self.player5)
        self.player5.size = 50
        self.player5.border_width = 1

        # initialisation des Enemis qui se déplacent autour de l'écran
        self.procedural_enemy_factory = ProceduralEnemyFactory(sub_surf0)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.time = pygame.time.get_ticks() / 1000  # temps écoulé en millisecondes depuis appel de pygame.init()
        #Logique de jeu (collisions, score, etc.)
        self.surf_factory.fill_surfaces()

        self.player.update()
        #self.player2.update()
        self.player3.update()
        self.player4.update()
        #self.player5.update()

        self.check_collisions()

    def check_collisions(self):
        # Logique de collision
        pass

    def draw(self):
        self.window.blit(self.background)
        self.player.draw()
        # self.player2.draw()
        self.player3.draw()
        self.player4.draw()
        self.player5.draw()

        self.procedural_enemy_factory.rotate_around_surface()

        self.surf_factory.blit_surfaces()
        # Dessine sur window
        #self.visual_helper.draw_dots(4, 4)
        self.visual_helper.draw_grid(2, 2)

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

