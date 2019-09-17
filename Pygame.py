import pygame
import os
from Map import *


pygame.init()
clock = pygame.time.Clock()

# Open window pygame
number_sprite = 17
size_sprite = 20
side_window = number_sprite * size_sprite
window = pygame.display.set_mode((side_window, side_window))

# Loading and display fond
fond = pygame.image.load(os.path.join('ressource', "grass.jpg")).convert()
window.blit(fond, (0, 0))


def print_map(map):
    # Images
    img_mac_gyver = pygame.image.load(os.path.join('ressource', "MacGyver.png")).convert_alpha()
    img_walls = pygame.image.load(os.path.join('ressource', "mur.png")).convert_alpha()
    img_guardian = pygame.image.load(os.path.join('ressource', "Gardien.png")).convert_alpha()
    img_exit = pygame.image.load(os.path.join('ressource', "exit.png")).convert_alpha()

    # On parcourt la liste du niveau
    num_row = 0
    for row in map:
        # On parcourt les listes de lignes
        num_square = 0
        for sprite in row:
            # On calcule la position réelle en pixels
            x = num_square * size_sprite
            y = num_row * size_sprite
            if sprite == 'O':  # m = Mur
                window.blit(img_walls, (x, y))
            elif sprite == 'S':  # d = Départ
                window.blit(img_mac_gyver, (x, y))
            elif sprite == 'G':  # a = Arrivée
                window.blit(img_guardian, (x, y))
            elif sprite == 'E':  # a = Arrivée
                window.blit(img_exit, (x, y))
            num_square += 1
        num_row += 1

# Move the player when it stays pressed
pygame.key.set_repeat(400, 30)

mac_gyver = Map("base_map")

loop = True
while loop:

    # Event for closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                position_mac_gyver = position_mac_gyver.move(0, 3)
            elif event.key == pygame.K_UP:
                position_mac_gyver = position_mac_gyver.move(0, -3)
            elif event.key == pygame.K_RIGHT:
                position_mac_gyver = position_mac_gyver.move(3, 0)
            elif event.key == pygame.K_LEFT:
                position_mac_gyver = position_mac_gyver.move(-3, 0)

    window.blit(fond, (0, 0))
    print_map(mac_gyver.map)

    # Reload screen
    pygame.display.flip()
    # 10 fps
    clock.tick(10)

