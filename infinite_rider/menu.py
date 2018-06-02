import os
import pygame


# Splashscreen with 3 buttons ( rect with text)
# Play
# Settings ( 1 button for saving in a file / 1 button to quit )
# Instructions when playing for the first time ("follow path with cursor") ( press any key or click to leave )
# Quit


class MenuScene:
    """
    Scene PyGame à afficher pour le menu du jeu
    """

    def __init__(self, screen):
        """
        Constructeur
        :param screen: le screen PyGame sur lequel on veut afficher les infos
        """
        if screen is not None:
            self.screen = screen

            # Splashscreen Image
            image_path = os.path.dirname(__file__) + os.sep + ".." + os.sep + "assets" + os.sep + "splash.jpg"
            self.splashscreen = pygame.image.load(image_path)

            self.show = True
            self.display()
        else:
            raise Exception("Cannot use empty screen !")

    def display(self):
        """
        Affiche l'écran de settings pour pouvoir modifier le son
        """

        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        font = pygame.font.SysFont("monospace", 36)
        title = font.render("Infinite Rider", 1, (0, 0, 0))
        msg = font.render("Press a key", 1, (255, 255, 255))

        while self.show:
            self.screen.blit(self.splashscreen, (0, 0))
            self.screen.blit(title, (self.screen.get_width()/2, 100))
            self.screen.blit(msg, (10, 550))
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    self.show = False
