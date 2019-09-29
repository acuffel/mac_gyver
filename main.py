from Game import *
from Map import *
from Character import *
from Display import *


def main():
    launch_game = Game()
    pygame.init()

    display_window = Display()
    while launch_game.continue_game:
        map_mac_gyver = Map("base_map")
        character_mac_gyver = Character(map_mac_gyver.position_player,
                                        map_mac_gyver.positions_walls,
                                        map_mac_gyver.map)
        launch_game.main_loop()

        # Loop for the menu
        launch_game.display_objects(map_mac_gyver)

        while launch_game.display_menu:
            launch_game.menu_loop()

        # Loop for the game
        while launch_game.display_game:
            launch_game.display_game_loop(map_mac_gyver, character_mac_gyver, display_window)
            # If MacGyver dies, the game display the dead menu

            while launch_game.dead_menu:
                launch_game.dead_menu_loop()

            # If MacGyver wins, the game display the win menu
            while launch_game.win_menu:
                launch_game.win_menu_loop()


if __name__ == '__main__':
    main()
