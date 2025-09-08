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

        self.background = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background.fill(color_palette['background'])

        self.visual_helper = VisualHelper(self.window)
        #initialiser la grille de surfaces
        self.visual_helper.create_surfaces_in_grid(8, 8)

        #couleurs des surfaces
        for i in range(len(self.visual_helper.surfaces)):
            self.visual_helper.surfaces[i].fill((3*i%255,3*i%255,3*i%255))

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
        self.window.blit(self.background)

        # pour blit chaque surfaces (fonction a créer)
        rows = 8
        lines = 8
        row_width = self.WINDOW_WIDTH / rows
        line_height = self.WINDOW_HEIGHT / lines
        surface_index = 0

        ###########
        for row in range(rows):
            for line in range(lines):
                x = row * row_width
                y = line * line_height
                self.window.blit(self.visual_helper.surfaces[surface_index], (x, y))
                surface_index += 1

        #pygame.draw.circle(self.window,(255,255,255),(307, 172), 20)
        self.visual_helper.blit_grid_surfaces()
        self.visual_helper.draw_grid(4, 4)
        self.visual_helper.draw_dots(8, 8)
        self.visual_helper.draw_coordinate_fraction(8, 8, 24)
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

