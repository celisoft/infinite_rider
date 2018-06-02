import pygame, os


class Game:

    def __init__(self, screen, clock):

        self.screen = screen
        self.screen.fill((0, 0, 0))

        self.clock = clock

        # Pointer Sprite
        image_path = os.path.dirname(__file__) + os.sep + ".." + os.sep + "assets" + os.sep + "pointer.png"
        self.pointer = pygame.image.load(image_path).convert_alpha()

        # Player Sprite
        image_path = os.path.dirname(__file__) + os.sep + ".." + os.sep + "assets" + os.sep + "player.png"
        self.player = pygame.image.load(image_path).convert_alpha()
        self.player_rect = pygame.Rect(0, 0, self.player.get_width(), self.player.get_height())

        # Mouse position
        self.mouse_position = pygame.mouse.get_pos()
        
        self.playing = True
        self.display()

    def display(self):
        # Looping game at 30 FPS
        self.clock.tick(60)

        while self.playing:
            self.screen.fill((0, 0, 0))

            # Mouse position
            self.mouse_position = pygame.mouse.get_pos()
            cursorW, cursorH = self.mouse_position

            # Mouse indication follow cursor
            mouse_rect = self.screen.blit(self.pointer, (cursorW, cursorH))
            self.player_rect = self.screen.blit(self.player, (self.player_rect.x, self.player_rect.y))

            if self.player_rect.x is not mouse_rect.x:
                if self.player_rect.x < mouse_rect.x:
                    self.player_rect.x += 1
                if self.player_rect.x > mouse_rect.x:
                    self.player_rect.x -= 1

            if self.player_rect.y is not mouse_rect.y:
                if self.player_rect.y < mouse_rect.y:
                    self.player_rect.y += 1
                if self.player_rect.y > mouse_rect.y:
                    self.player_rect.y -= 1
            pygame.time.wait(20)
            pygame.display.flip()

            self.events()

    def events(self):
        # Game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False

    def show_go_screen(self):
        # Game over / Continue
        pass
