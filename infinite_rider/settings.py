#!/usr/bin/env python3

import json


class Settings:
    def __init__(self, path="../ir_settings.json"):
        # load the file into json mapping
        self.path = path
        self.properties = None
        self.load()

    def restore_default(self):
        self.properties = {
            "game_props": {
                "sound_volume": 100,
            }
        }

    def get_volume(self):
        return self.properties["game_props"]["sound_volume"]

    def set_volume(self, new_value):
        self.properties["game_props"]["sound_volume"] = new_value

    def load(self):
        with open(self.path, "r") as settings_file:
            self.properties = json.load(settings_file)
        if self.properties is None:
            self.restore_default()

    def save(self):
        with open(self.path, "w") as settings_file:
            json.dump(self.properties, settings_file, indent=4)


if __name__ == '__main__':
    s = Settings()
    print(s.get_volume())
    s.set_volume(80)
    print(s.get_volume())
    s.save()
