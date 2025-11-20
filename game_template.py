
from imports import *
#from entities import *
from game_dev_tools import *

class Game:
    def __init__(self):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.window_center = pygame.Vector2(self.window.get_rect().center)
        pygame.display.set_caption(WINDOW_TITLE)
        self.font = pygame.font.Font(None, DEFAULT_FONT_SIZE)
        self.time = 0.0
        self.clock = pygame.time.Clock() # Object to help track time
        self.running = True
        self.dt = 0.0

        self.background = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background.fill(color_palette['background'])

        self.visual_helper = VisualHelper(self.window)
        self.surf_factory = PygameSurfaceFactory(self.window, 3,3)
        self.surf_factory.create_surfaces()

        self.game_entities = [] # Stocker les entités pour update et draw d'un seul coup sans modifier à chaque fois
        # exemple dans update() :
        # for i in range(len(self.game_entities)):
        #       self.game_entities[i].update()

        ################## gestion des effets de collision  #####################################
        self.active_collisions_stacks = {}  # prévoir de renommer en active_collisions_effects_stacks
        self.collision_conditions = []  # en standby

        # nommer chaque type de collision
        # exemple : 'player_projectile_and_enemy'
        self.collisions = []

        # pour chaque type de collision créer un stack:
        for collision in self.collisions:
            self.active_collisions_stacks[collision] = []

        # permettre création de plusieurs animation pour le meme type de collision
        # supprimer les objets aprés utilisation sinon a chaque collision un objet est créé en mémoire
        # exemple :
        # self.collisions[0]: CollisionEffectAnimation
        self.collision_effects = {}

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.time = pygame.time.get_ticks() / 1000  # temps écoulé en millisecondes depuis appel de pygame.init()
        self.surf_factory.fill_surfaces()

        for entity in self.game_entities:
            entity.update()

        # faire le tri dans les stacks de collision, garder les animations qui sont activées
        # pour ne pas faire dans draw if animation.alive: animation.draw
        for collision in self.collisions:
            self.active_collisions_stacks[collision] = [a for a in self.active_collisions_stacks[collision] if
                                                        a.alive]

        for collision in self.collisions:
            for active_collision in self.active_collisions_stacks[collision]:
                active_collision.update(self.dt)

        self.check_collisions()

    def check_collisions(self):
        # Logique de collision
        pass

    def draw(self):
        self.window.blit(self.background)

        # ne pas oublier de remplir les surfaces avec fill avant de dessiner
        # self.surf_factory.fill_surfaces()

        for entity in self.game_entities:
            entity.draw()

        self.surf_factory.blit_surfaces()
        # Dessine sur window
        #self.visual_helper.draw_dots(4, 4)
        self.visual_helper.draw_grid(3, 3)

        for collision in self.collisions:
            # for game_entity in self.game_entities:
            #     if hasattr(game_entity, 'appearances'):
            #         game_entity.current_appearance = game_entity.appearances['on_collision_with_player_projectile']
            for active_collision in self.active_collisions_stacks[collision]:
                active_collision.draw()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

