import pygame
import os
from constants import *


class Display:

    pygame.init()
    clock = pygame.time.Clock()

    def __init__(self):
        """initializing the class Display with :
        - window
        - background"""
        # Open window pygame
        self.window = pygame.display.set_mode((SIDE_WINDOW,
                                               SIDE_WINDOW + SIZE_SPRITE))
        # Loading and display fond
        self.background = pygame.image.load(os.path.join(
            'ressource', "grass.jpg")).convert()
        self.window.blit(self.background, (0, 0))
        self.show_title = pygame.display.set_caption('Mac Gyver')

    def display_images_on_map(self, game_map, position_player):
        """ Function which post the images in the window"""
        # Images
        img_mac_gyver = pygame.image.load(os.path.join(
            'ressource', "MacGyver.jpg")).convert_alpha()
        img_mac_gyver_onscall = pygame.transform.scale(img_mac_gyver, (30, 30))
        img_walls = pygame.image.load(os.path.join(
            'ressource', "mur.jpg")).convert_alpha()
        img_walls_onscall = pygame.transform.scale(img_walls, (30, 30))
        img_guardian = pygame.image.load(os.path.join(
            'ressource', "Gardien.jpg")).convert_alpha()
        img_guardian_onscall = pygame.transform.scale(img_guardian, (30, 30))
        img_exit = pygame.image.load(os.path.join(
            'ressource', "exit.jpg")).convert_alpha()
        img_exit_onscall = pygame.transform.scale(img_exit, (30, 30))
        img_obj_a = pygame.image.load(os.path.join(
            'ressource', "seringue.png")).convert_alpha()
        img_obj_a_onscall = pygame.transform.scale(img_obj_a, (30, 30))
        img_obj_b = pygame.image.load(os.path.join(
            'ressource', "ether.png")).convert_alpha()
        img_obj_b_onscall = pygame.transform.scale(img_obj_b, (30, 30))

        num_col = 0
        for row in game_map:
            num_row = 0
            for sprite in row:
                x = num_row * SIZE_SPRITE
                y = num_col * SIZE_SPRITE
                x_macgyver = position_player[1] * SIZE_SPRITE
                y_macgyver = position_player[0] * SIZE_SPRITE
                if sprite == 'O':
                    self.window.blit(img_walls_onscall, (x, y))
                elif sprite == 'G':
                    self.window.blit(img_guardian_onscall, (x, y))
                elif sprite == 'E':
                    self.window.blit(img_exit_onscall, (x, y))
                elif sprite == 'A':
                    self.window.blit(img_obj_a_onscall, (x, y))
                elif sprite == 'B':
                    self.window.blit(img_obj_b_onscall, (x, y))
                elif sprite == 'X':
                    self.window.blit(img_mac_gyver_onscall,
                                     (x_macgyver, y_macgyver))
                num_row += 1
            num_col += 1

    def display_text_on_map(self, display_text):
        """Display text on the map"""
        white = (255, 255, 255)
        font_text = pygame.font.Font('freesansbold.ttf', 12)
        text = font_text.render(display_text, True, white)
        text_rect = text.get_rect()
        text_rect.center = (SIDE_WINDOW // 2, SIDE_WINDOW + (SIZE_SPRITE / 2))
        self.window.blit(text, text_rect)

    def refresh_text_on_map(self):
        """Remove text on the map"""
        black = (0, 0, 0)
        pygame.draw.rect(self.window, black, (0, SIDE_WINDOW - SIZE_SPRITE,
                                              SIDE_WINDOW, SIZE_SPRITE), 100)
