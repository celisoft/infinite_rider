#!/usr/bin/env python3

import os
import pygame
from infinite_rider import game


class Player(pygame.sprite.Sprite):
    PLAYER_RUN1 = 0
    PLAYER_STOP = 1
    PLAYER_RUN2 = 2

    PLAYER_WIDTH = 24
    PLAYER_HEIGHT = 64

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Retrieve the image file to load it as spritesheet
        path = os.path.dirname(__file__) + os.sep + ".." + os.sep + "assets" + os.sep + "player.png"
        self.spritesheet = pygame.image.load(path)

        # Define the player sprites from the spritesheet (24x64)
        self.sprites = []
        for sprite_id in range(3):
            self.sprites.append(
                self.spritesheet.subsurface(self.PLAYER_WIDTH * sprite_id, 0, self.PLAYER_WIDTH,
                                            self.PLAYER_HEIGHT))

        # Default sprite is the droplet one
        self.current_shape = self.PLAYER_STOP
        self.image = self.sprites[self.current_shape]

        # Define the default rect
        self.rect = pygame.Rect(0, 0, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)

        # Set the group as a single sprite one
        self.group = pygame.sprite.GroupSingle(self)

    def get_rect(self):
        return self.rect

    def display(self, screen):
        """
        Affiche le joueur
        :param screen: La surface sur laquelle on blit
        """
        self.group.draw(screen)

    def shapeshift(self):
        """
        Mets à jour la forme du joueur
        """
        if self.current_shape == self.PLAYER_RUN1:
            self.current_shape = self.PLAYER_RUN2
            self.image = self.sprites[self.PLAYER_RUN2]
        else:
            self.current_shape = self.PLAYER_RUN1
            self.image = self.sprites[self.PLAYER_RUN1]


if __name__ == "__main__":
    TITLE = 'Inifinite rider Player test'

    # Title
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((800, 600))

    # Speed
    clock = pygame.time.Clock()
    g = game.Game(screen, clock)
    pygame.quit()
