import pygame
import os
from Map import *
from constants import *

pygame.init()
clock = pygame.time.Clock()

# Open window pygame
window = pygame.display.set_mode((side_window, side_window))

# Loading and display fond
fond = pygame.image.load(os.path.join('ressource', "grass.jpg")).convert()
window.blit(fond, (0, 0))


def image_on_map(map):
    # Images
    img_mac_gyver = pygame.image.load(os.path.join('ressource', "MacGyver.png")).convert_alpha()
    img_mac_gyver_onscall = pygame.transform.scale(img_mac_gyver, (30, 30))
    img_walls = pygame.image.load(os.path.join('ressource', "mur.png")).convert_alpha()
    img_walls_onscall = pygame.transform.scale(img_walls, (30, 30))
    img_guardian = pygame.image.load(os.path.join('ressource', "Gardien.png")).convert_alpha()
    img_guardian_onscall = pygame.transform.scale(img_guardian, (30, 30))
    img_exit = pygame.image.load(os.path.join('ressource', "exit.png")).convert_alpha()
    img_exit_onscall = pygame.transform.scale(img_exit, (30, 30))
    img_obj_a = pygame.image.load(os.path.join('ressource', "seringue.png")).convert_alpha()
    img_obj_a_onscall = pygame.transform.scale(img_obj_a, (30, 30))
    img_obj_b = pygame.image.load(os.path.join('ressource', "ether.png")).convert_alpha()
    img_obj_b_onscall = pygame.transform.scale(img_obj_b, (30, 30))

    num_row = 0
    for row in map:
        num_square = 0
        for sprite in row:
            x = num_square * size_sprite
            y = num_row * size_sprite
            if sprite == 'O':
                window.blit(img_walls_onscall, (x, y))
            elif sprite == 'X':
                window.blit(img_mac_gyver_onscall, (x, y))
            elif sprite == 'G':
                window.blit(img_guardian_onscall, (x, y))
            elif sprite == 'E':
                window.blit(img_exit_onscall, (x, y))
            elif sprite == 'A':
                window.blit(img_obj_a_onscall, (x, y))
            elif sprite == 'B':
                window.blit(img_obj_b_onscall, (x, y))
            num_square += 1
        num_row += 1


# Move the player when it stays pressed
pygame.key.set_repeat(400, 30)

mac_gyver = Map("base_map")
mac_gyver.post_object()
mac_gyver.clean_char("S")

loop = True
while loop:

    # Event for closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                mac_gyver.position_player[0] = mac_gyver.move_player("s") * size_sprite
            elif event.key == pygame.K_UP:
                mac_gyver.position_player[0] = mac_gyver.move_player("z") * size_sprite
            elif event.key == pygame.K_RIGHT:
                mac_gyver.position_player[1] = mac_gyver.move_player("d") * size_sprite
            elif event.key == pygame.K_LEFT:
                mac_gyver.position_player[1] = mac_gyver.move_player("q") * size_sprite

    window.blit(fond, (0, 0))
    image_on_map(mac_gyver.map_new_player)

    # Reload screen
    pygame.display.flip()
    # 10 fps
    clock.tick(10)

