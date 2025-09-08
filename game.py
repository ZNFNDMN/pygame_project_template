from imports import *
#from entities import *
from game_dev_tools.game_dev_tools import Grid

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
        pass

    def draw(self):
        self.window.fill(color_palette['background'])
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

