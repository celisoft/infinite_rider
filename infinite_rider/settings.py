#!/usr/bin/env python3

import json
import pygame


class Settings:
    """
    Cette classe permet de charger, manipuler les propriétés variables du jeu
    """

    def __init__(self, path="../ir_settings.json"):
        """
        Le constructeur de la classe ...
        :param path: le chemin où se trouve le fichier de conf, pas obligatoire
        """
        self.path = path
        self.properties = None
        self.load()

    def restore_default(self):
        """
        Restaure les propriétés par défaut
        """
        self.properties = {
            "game_props": {
                "sound_volume": 100,
            }
        }

    def get_volume(self):
        """
        Getter du volume sonore
        :return: le niveau de volume sonore
        """
        return self.properties["game_props"]["sound_volume"]

    def set_volume(self, new_value):
        """
        Définit le niveau sonore
        :param new_value: la future valeur du niveau sonore
        """
        if new_value > 0:
            if new_value <= 100:
                self.properties["game_props"]["sound_volume"] = new_value
            else:
                self.properties["game_props"]["sound_volume"] = 100

    def load(self):
        """
        Charge le fichier de configuration
        """
        with open(self.path, "r") as settings_file:
            self.properties = json.load(settings_file)
        if self.properties is None:
            self.restore_default()
        elif self.properties["game_props"]["sound_volume"] > 100:
            self.properties["game_props"]["sound_volume"] = 100

    def save(self):
        """
        Sauvegarde le fichier de configuration
        """
        with open(self.path, "w") as settings_file:
            json.dump(self.properties, settings_file, indent=4)


class SettingScene:
    """
    Scene PyGame à afficher pour configurer le jeu
    """

    def __init__(self, screen, settings):
        """
        Constructeur
        :param screen: le screen PyGame sur lequel on veut afficher les infos
        """
        if screen is not None:
            self.screen = screen
            self.settings = settings
            self.show = True
            self.display()
        else:
            raise Exception("Cannot use empty screen !")

    def display(self):
        """
        Affiche l'écran de settings pour pouvoir modifier le son
        :return: le dictionnaire de settings à recharger dans le jeu
        """
        background = pygame.Surface((800, 600))
        background.convert()
        background.fill(pygame.Color("#000000"))

        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        font = pygame.font.SysFont("monospace", 36)
        sfx_lvl = font.render(str("Volume : %i" % self.settings.get_volume()), 1, (255, 255, 0))
        sfx_msg = font.render("+/- pour monter/baisser le son", 1, (255, 255, 0))
        save_msg = font.render("S pour sauver et revenir au menu", 1, (255, 255, 255))
        exit_msg = font.render("Esc revenir au menu sans sauver", 1, (255, 255, 255))

        while self.show:
            self.screen.blit(background, (0, 0))
            screen.blit(sfx_lvl, (10, 100))
            screen.blit(sfx_msg, (10, 150))

            screen.blit(save_msg, (10, 500))
            screen.blit(exit_msg, (10, 550))
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_KP_PLUS:
                        self.settings.set_volume(self.settings.get_volume() + 1)
                        sfx_lvl = font.render(str("Volume : %i" % self.settings.get_volume()), 1, (255, 255, 0))
                    elif e.key == pygame.K_KP_MINUS:
                        self.settings.set_volume(self.settings.get_volume() - 1)
                        sfx_lvl = font.render(str("Volume : %i" % self.settings.get_volume()), 1, (255, 255, 0))
                    elif e.key == pygame.K_s:
                        self.settings.save()
                    elif e.key == pygame.K_ESCAPE:
                        self.settings.restore_default()
                        self.show = False
        return self.settings


# Histoire de faire quelques tests en solo :)
if __name__ == '__main__':
    # tests de Settings
    s = Settings()
    print(s.get_volume())
    s.set_volume(80)
    print(s.get_volume())
    s.save()

    # tests de SettingsScene
    pygame.init()
    pygame.display.set_caption('Inifinite rider - Settings screen test')
    screen = pygame.display.set_mode((800, 600))
    SettingScene(screen, s)
    pygame.display.quit()
