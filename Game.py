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
            # Open menu
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
            display_menu = True
            display_game = True

            # Loop for the menu
            while display_menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        display_menu = False
                        continue_game = False
                        display_game = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_b or event.key == pygame.K_ESCAPE:
                            display_menu = False
                            continue_game = False
                            display_game = False

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
            while display_game:
                # 30 fps
                clock.tick(30)

                win_menu = False
                dead_menu = False

                # Event for closing the window
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        display_game = False

                    if event.type == pygame.KEYDOWN:
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
                        display_game = False
                        win_menu = True

                    if character_mac_gyver.position_player == map_mac_gyver.position_guardian \
                            and len(character_mac_gyver.counter) != 2:
                        display_game = False
                        dead_menu = True
                    # Display the window after actions
                    display_window.window.blit(display_window.background, (0, 0))
                    display_window.display_images_on_map(character_mac_gyver.map_new_player, character_mac_gyver.position_player)

                    # Reload screen
                    pygame.display.flip()

                # If MacGyver dies, the game display the dead menu
                while dead_menu is True:

                    # Display the menu in the window
                    dead_window = pygame.image.load(os.path.join('ressource', "end_menu.jpg")).convert()
                    dead_window_on_scall = pygame.transform.scale(dead_window, (SIDE_WINDOW, SIDE_WINDOW))
                    start_window.blit(dead_window_on_scall, (0, 0))

                    # Refresh the window
                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            dead_menu = False
                            continue_game = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_b or event.key == pygame.K_ESCAPE:
                                dead_menu = False
                                continue_game = False

                            if event.key == pygame.K_a:
                                dead_menu = False

                # If MacGyver wins, the game display the win menu
                while win_menu is True:

                    # Display the menu in the window
                    win_window = pygame.image.load(os.path.join('ressource', "end_menu.jpg")).convert()
                    win_window_on_scall = pygame.transform.scale(win_window, (SIDE_WINDOW, SIDE_WINDOW))
                    start_window.blit(win_window_on_scall, (0, 0))

                    # Refresh the window
                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            win_menu = False
                            continue_game = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_b or event.key == pygame.K_ESCAPE:
                                win_menu = False
                                continue_game = False

                            if event.key == pygame.K_a:
                                win_menu = False

if __name__ == '__main__':
    Game().launch_game()
