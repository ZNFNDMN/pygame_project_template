
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
        self.surf_factory = PygameSurfaceFactory(self.window, 3,3)
        self.surf_factory.create_surfaces()

        self.game_entities = []

        #############################################
        sub_surf0  = self.surf_factory.surf_list[0]
        sub_surf_center = sub_surf0.get_rect().center

        self.player = Player(sub_surf0,pygame.Vector2(sub_surf_center))
        self.game_entities.append(self.player)
        self.player.movement_system = KeyboardMovementSystem(self.player, sub_surf0) #passer l'instance de player pour pouvoir modif la position
        self.player.game_entity_appearence = PlayerAppearance6([], self.player)
        self.player.size = 60
        self.player.color = (255,255,255)
        self.player.border_width = 1

        sub_surf1 = self.surf_factory.surf_list[1]

        self.player2 = Player(sub_surf1, pygame.Vector2(sub_surf_center), Circle())
        self.game_entities.append(self.player2)
        self.player2.movement_system = KeyboardMovementSystem(self.player2,sub_surf1)  # passer l'instance de player pour pouvoir modif la position
        self.player2.game_entity_appearence = PlayerAppearance7([], self.player2)
        self.player2.size = 60
        self.player2.border_width = 1

        sub_surf2 = self.surf_factory.surf_list[2]

        self.entity = Player(sub_surf2, pygame.Vector2(sub_surf_center), Circle())
        self.game_entities.append(self.entity)
        self.entity.movement_system = KeyboardMovementSystem(self.entity,
                                                              sub_surf2)  # passer l'instance de player pour pouvoir modif la position
        self.entity.game_entity_appearence = EntityAppearance([], self.entity)
        self.entity.size = 120
        self.entity.border_width = 1

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.time = pygame.time.get_ticks() / 1000  # temps écoulé en millisecondes depuis appel de pygame.init()
        #Logique de jeu (collisions, score, etc.)
        self.surf_factory.fill_surfaces()

        for i in range(len(self.game_entities)):
            self.game_entities[i].update()

        self.check_collisions()

    def check_collisions(self):
        # Logique de collision
        pass

    def draw(self):
        self.window.blit(self.background)

        for i in range(len(self.game_entities)):
            self.game_entities[i].draw()

        self.surf_factory.blit_surfaces()
        # Dessine sur window
        #self.visual_helper.draw_dots(4, 4)
        self.visual_helper.draw_grid(3, 3)
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

