import pygame.draw

from game_dev_tools.game_dev_tools import Circle, MovementSystem
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
        self.surf_factory = PygameSurfaceFactory(self.window, 4,4)
        self.surf_factory.create_surfaces()

        #############################################
        sub_surf0  = self.surf_factory.surf_list[0]
        sub_surf_center = sub_surf0.get_rect().center
        # Définir la shape et movement system ici pour avoir le controle
        circle1 = Circle((0,255,255))

        self.player = Player(sub_surf0,pygame.Vector2(sub_surf_center), circle1)
        # initialisation du movement system aprés instanciation du player
        self.player.movement_system = MouseMovementSystem(self.player, sub_surf0) #passer l'instance de player pour pouvoir modif la position
        ###############################################
        sub_surf1 = self.surf_factory.surf_list[1]
        # Définir la shape et movement system ici pour avoir le controle
        circle2 = Circle((255, 0, 255))

        self.player2 = Player(sub_surf1, pygame.Vector2(sub_surf_center), circle2, pygame.Vector2(0,0),5)
        # initialisation du movement system aprés instanciation du player
        self.player2.movement_system = KeyboardMovementSystem(self.player2, sub_surf1)  # passer l'instance de player pour pouvoir modif la position

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.time = pygame.time.get_ticks() / 1000  # temps écoulé en millisecondes depuis appel de pygame.init()
        #Logique de jeu (collisions, score, etc.)
        self.surf_factory.fill_surfaces()

        self.player.update()
        self.player2.update()

        self.check_collisions()

    def check_collisions(self):
        # Logique de collision
        pass

    def draw(self):

        self.window.blit(self.background)
        self.player.draw()
        self.player2.draw()
        self.surf_factory.blit_surfaces()
        self.visual_helper.draw_dots(4, 4)
        self.visual_helper.draw_grid(2, 2)

        #pygame.draw.circle(self.window,(255,255,255), pygame.mouse.get_pos(), 20)
        #self.visual_helper.draw_coordinate_fraction(8, 8, 24)

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

