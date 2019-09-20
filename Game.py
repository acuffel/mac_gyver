import pygame
import os
from Map import *
from Display import *
from Character import *


class Game:

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()


        # Move the player when it stays pressed
        pygame.key.set_repeat(400, 30)

        # Call class Map and display the window
        map_mac_gyver = Map("base_map")
        character_mac_gyver = Character(map_mac_gyver.position_player, map_mac_gyver.positions_walls, map_mac_gyver.map)
        # Initializing window
        map_mac_gyver.post_object()
        map_mac_gyver.clean_char("S")

        display_window = Display()

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
                        character_mac_gyver.move_player("s")
                        pygame.time.get_ticks()
                    elif event.key == pygame.K_UP:
                        character_mac_gyver.move_player("z")
                        pygame.time.get_ticks()
                    elif event.key == pygame.K_RIGHT:
                        character_mac_gyver.move_player("d")
                        pygame.time.get_ticks()
                    elif event.key == pygame.K_LEFT:
                        character_mac_gyver.move_player("q")
                        pygame.time.get_ticks()

            # Interaction with Mac Gyver and the map
            character_mac_gyver.catch_object(map_mac_gyver, map_mac_gyver, display_window,  "A", "B")
            dead = character_mac_gyver.pass_guardian(map_mac_gyver, map_mac_gyver, display_window)
            won = character_mac_gyver.is_won(map_mac_gyver, display_window)


            # Display the window after actions
            display_window.window.blit(display_window.background, (0, 0))
            display_window.display_images_on_map(character_mac_gyver.map_new_player, character_mac_gyver.position_player)

            # Reload screen
            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
