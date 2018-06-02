import pygame, os
from infinite_rider import settings

TITLE = 'Inifinite rider'
FPS = 30
cursorW, cursorH = 0, 0

class Game:
    def __init__(self):
        # initialize game window, etc
        # Init
        pygame.init()
        pygame.mixer.init()
        pygame.mouse.set_visible(0)

        # Title
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((800, 600))

        # Speed
        self.clock = pygame.time.Clock()

        # Splashscreen Image
        image_path = os.path.dirname(__file__) + os.sep + "assets" + os.sep + "splash.jpg"
        self.splashscreen_img = pygame.image.load(image_path)

        #Pointer Sprite
        image_path = os.path.dirname(__file__)+ os.sep + "assets" + os.sep + "pointer.png"
        self.pointer = pygame.image.load(image_path).convert_alpha()

        # Player Sprite
        image_path = os.path.dirname(__file__) + os.sep + "assets" + os.sep + "player.png"
        self.player = pygame.image.load(image_path).convert_alpha()

        # # Music
        # music_path = os.path.dirname(__file__) + os.sep + "assets" + os.sep + "music.ogg"
        # pygame.mixer.music.load(music_path)
        # pygame.mixer.music.play()

        self.running = True

    def new(self):
        # Start a new game

        # Sprites
        self.all_sprites = pygame.sprite.Group()
        self.run()

    def run(self):
        #Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Game loop update
        self.all_sprites.update()
    def events(self):
        #Game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        # Mouse position
        self.mouse_surface = pygame.Surface((32, 32))
        self.screen.fill((0, 0, 0))
        self.mouse_position = pygame.mouse.get_pos()
        cursorW, cursorH = self.mouse_position



        # Player follow mouse
        self.screen.blit(self.pointer, (cursorW, cursorH))
        self.screen.blit(self.player, (0, 0))


    def draw(self):
        #Game loop draw
        # self.screen.fill((0, 0, 0))
        # self.screen.blit(self.splashscreen_img, (0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    def show_start_screen(self):
        #Game splash / Start screen
        pass

    def show_go_screen(self):
        #Game over / Continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
