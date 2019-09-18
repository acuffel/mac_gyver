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

# Function which post the images in the window
def images_on_map(map, position_player):
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

    num_col = 0
    for row in map:
        num_row = 0
        for sprite in row:
            x = num_row * size_sprite
            y = num_col * size_sprite
            x_macgyver = position_player[1] * size_sprite
            y_macgyver = position_player[0] * size_sprite
            if sprite == 'O':
                window.blit(img_walls_onscall, (x, y))
            elif sprite == 'G':
                window.blit(img_guardian_onscall, (x, y))
            elif sprite == 'E':
                window.blit(img_exit_onscall, (x, y))
            elif sprite == 'A':
                window.blit(img_obj_a_onscall, (x, y))
            elif sprite == 'B':
                window.blit(img_obj_b_onscall, (x, y))
            elif sprite == 'X':
                window.blit(img_mac_gyver_onscall, (x_macgyver, y_macgyver))
            num_row += 1
        num_col += 1

# Move the player when it stays pressed
pygame.key.set_repeat(400, 30)

# Call class Map and display the window
mac_gyver = Map("base_map")
mac_gyver.post_object()
mac_gyver.clean_char("S")

won = False
dead = False
while not (won or dead):
    # 30 fps
    clock.tick(30)

    # Event for closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                mac_gyver.move_player("s")
            elif event.key == pygame.K_UP:
                mac_gyver.move_player("z")
            elif event.key == pygame.K_RIGHT:
                mac_gyver.move_player("d")
            elif event.key == pygame.K_LEFT:
                mac_gyver.move_player("q")

    # Interaction with Mac Gyver and the map
    mac_gyver.catch_object("A", "B")
    dead = mac_gyver.pass_guardian()
    won = mac_gyver.is_won()

    # Display the window after actions
    window.blit(fond, (0, 0))
    images_on_map(mac_gyver.map_new_player, mac_gyver.position_player)
    # move_image_macgyver(mac_gyver.map_new_player, mac_gyver.position_player)

    # Reload screen
    pygame.display.flip()
