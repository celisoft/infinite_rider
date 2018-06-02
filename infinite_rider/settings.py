#!/usr/bin/env python3

import json


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


# Histoire de faire quelques tests en solo :)
if __name__ == '__main__':
    s = Settings()
    print(s.get_volume())
    s.set_volume(80)
    print(s.get_volume())
    s.save()
