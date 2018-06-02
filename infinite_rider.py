import pygame, os
from infinite_rider import settings, game, menu

TITLE = 'Inifinite rider'
cursorW, cursorH = 0, 0

# initialize game window, etc
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(0)

# Title
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((800, 600))

# Speed
clock = pygame.time.Clock()

# # Music
# music_path = os.path.dirname(__file__) + os.sep + "assets" + os.sep + "music.ogg"
# pygame.mixer.music.load(music_path)
# pygame.mixer.music.play()

running = True
m = menu.MenuScene(screen)
g = game.Game(screen, clock)
m.display()
pygame.quit()
