import pygame
import os
from Map import *
from Display import *
from Character import *


class Game:

    def launch_game(self):

        pygame.init()
        clock = pygame.time.Clock()

        # BOUCLE PRINCIPALE
        continue_game = True
        while continue_game:

            start_window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))

            # Move the player when it stays pressed
            pygame.key.set_repeat(400, 30)


            # Chargement et affichage de l'écran d'accueil
            start_menu = pygame.image.load(os.path.join('ressource', "accueil-macgyver.png")).convert()
            start_menu_onscall = pygame.transform.scale(start_menu, (SIDE_WINDOW, SIDE_WINDOW))
            start_window.blit(start_menu_onscall, (0, 0))

            # Rafraichissement
            pygame.display.flip()

            # Move the player when it stays pressed
            pygame.key.set_repeat(400, 30)

            # Initializing Boolean for Loops
            exit_game = False
            won = False
            dead = False
            display_menu = True

            while display_menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        display_menu = False
                        continue_game = False
                        exit_game = True

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_b or event.key == pygame.K_ESCAPE:
                            display_menu = False
                            continue_game = False
                            exit_game = True

                        elif event.key == pygame.K_a:
                            display_menu = False

            # Call class Map and display the window
            map_mac_gyver = Map("base_map")
            character_mac_gyver = Character(map_mac_gyver.position_player, map_mac_gyver.positions_walls,
                                            map_mac_gyver.map)

            # Initializing window
            map_mac_gyver.post_object()
            map_mac_gyver.clean_char("S")

            display_window = Display()

            while not (won or dead or exit_game):
                # 30 fps
                clock.tick(30)

                # Event for closing the window
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            character_mac_gyver.move_player("s")
                            display_window.refresh_text_on_map()
                        elif event.key == pygame.K_UP:
                            character_mac_gyver.move_player("z")
                            display_window.refresh_text_on_map()
                        elif event.key == pygame.K_RIGHT:
                            character_mac_gyver.move_player("d")
                            display_window.refresh_text_on_map()
                        elif event.key == pygame.K_LEFT:
                            character_mac_gyver.move_player("q")
                            display_window.refresh_text_on_map()

                    # Interaction with Mac Gyver and the map
                    character_mac_gyver.catch_object(map_mac_gyver, map_mac_gyver, display_window,  "A", "B")
                    dead = character_mac_gyver.pass_guardian(map_mac_gyver, map_mac_gyver, display_window)
                    won = character_mac_gyver.is_won(map_mac_gyver, display_window)

                    if (dead or won) is True:
                        display_window.pause_game()

                    # Display the window after actions
                    display_window.window.blit(display_window.background, (0, 0))
                    display_window.display_images_on_map(character_mac_gyver.map_new_player, character_mac_gyver.position_player)

                    # Reload screen
                    pygame.display.flip()


if __name__ == '__main__':
    Game().launch_game()
