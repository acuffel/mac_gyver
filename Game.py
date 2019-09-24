import pygame
import os
from Map import *
from Display import *
from Character import *


class Game:

    def launch_game(self):
        """Launch the game"""
        pygame.init()
        clock = pygame.time.Clock()

        # Main Loop
        continue_game = True
        while continue_game:
            # Open window
            start_window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))

            # Display the menu in the window
            start_menu = pygame.image.load(os.path.join('ressource', "accueil-macgyver.png")).convert()
            start_menu_onscall = pygame.transform.scale(start_menu, (SIDE_WINDOW, SIDE_WINDOW))
            start_window.blit(start_menu_onscall, (0, 0))

            # Refresh the window
            pygame.display.flip()

            # Move the player when it stays pressed
            pygame.key.set_repeat(400, 30)

            # Initializing Boolean for Loops
            exit_game = False
            won = False
            dead = False
            display_menu = True

            # Loop for the menu
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

            # Loop for the game
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

                    # Display text on the map
                    character_mac_gyver.pass_guardian(map_mac_gyver, map_mac_gyver, display_window)
                    character_mac_gyver.is_won(map_mac_gyver, display_window)

                    # Exit the window if the player win the game or died
                    if character_mac_gyver.position_player == map_mac_gyver.position_exit:
                        won = True
                    if character_mac_gyver.position_player == map_mac_gyver.position_guardian:
                        if len(character_mac_gyver.counter) != 2:
                            dead = True

                    # Display the window after actions
                    display_window.window.blit(display_window.background, (0, 0))
                    display_window.display_images_on_map(character_mac_gyver.map_new_player, character_mac_gyver.position_player)

                    # Reload screen
                    pygame.display.flip()


if __name__ == '__main__':
    Game().launch_game()
