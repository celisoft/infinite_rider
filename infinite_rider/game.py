import os
import pygame

from infinite_rider import player


class Game:

    def __init__(self, screen, clock):

        self.screen = screen
        self.screen.fill((0, 0, 0))

        self.clock = clock

        # Pointer Sprite
        image_path = os.path.dirname(__file__) + os.sep + ".." + os.sep + "assets" + os.sep + "pointer.png"
        self.pointer = pygame.image.load(image_path).convert_alpha()
        self.player = player.Player()

        # Mouse position
        self.mouse_position = pygame.mouse.get_pos()

        self.playing = True
        self.running = False
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
            self.player.display(self.screen)

            if self.running is True:
                self.player.shapeshift()
                if self.player.rect.x is not mouse_rect.x:
                    if self.player.rect.x < mouse_rect.x:
                        self.player.rect.x += 1
                    if self.player.rect.x > mouse_rect.x:
                        self.player.rect.x -= 1

                if self.player.rect.y is not mouse_rect.y:
                    if self.player.rect.y < mouse_rect.y:
                        self.player.rect.y += 1
                    if self.player.rect.y > mouse_rect.y:
                        self.player.rect.y -= 1

            pygame.time.wait(20)
            pygame.display.flip()

            self.events()

    def events(self):
        # Game loop events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.running = True
                self.player.shapeshift()
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False

    def show_go_screen(self):
        # Game over / Continue
        pass
