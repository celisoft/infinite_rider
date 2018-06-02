import pygame
#Game loop

WIDTH = 800
HEIGHT = 600
FPS = 30

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Inifinite rider')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.ticks(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass

    def events(self):
        pass

    def draw(self):
        pass

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
pygame.quit()