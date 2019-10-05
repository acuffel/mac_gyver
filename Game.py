from Map import *
from Character import *
from Display import *


class Game:

    def __init__(self):
        """Initializing the game with :
        - Booleans
        - Start window
        - time.clock"""
        self.start_window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
        self.continue_game = True
        self.display_menu = True
        self.display_game = True
        self.win_menu = False
        self.dead_menu = False
        self.clock = pygame.time.Clock()

    def main_loop(self):
        """Display the main window"""
        start_menu = pygame.image.load(
            os.path.join('ressource', "accueil-macgyver.png")).convert()
        start_menu_onscall = pygame.transform.scale(
            start_menu, (SIDE_WINDOW, SIDE_WINDOW))
        self.start_window.blit(start_menu_onscall, (0, 0))

        # Refresh the window
        pygame.display.flip()

        # Move the player when it stays pressed
        pygame.key.set_repeat(400, 30)

    def display_objects(self, map_mac_gyver):
        """Display objects on pygame window"""
        map_mac_gyver.post_object()
        map_mac_gyver.clean_char("S")

    def menu_loop(self):
        """Display the first menu"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.display_menu = False
                self.continue_game = False
                self.display_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b or event.key == pygame.K_ESCAPE:
                    self.display_menu = False
                    self.continue_game = False
                    self.display_game = False

                elif event.key == pygame.K_a:
                    self.display_menu = False
                    self.display_game = True

    def display_game_loop(self, map_mac_gyver, character_mac_gyver,
                          display_window):
        """Display the game menu"""
        # 30 fps
        self.clock.tick(30)

        # Event for closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.display_game = False
                self.display_menu = True

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
            character_mac_gyver.catch_object(map_mac_gyver,
                                             map_mac_gyver,
                                             display_window,
                                             "A", "B")

            # Display text on the map
            character_mac_gyver.pass_guardian(map_mac_gyver,
                                              map_mac_gyver,
                                              display_window)
            character_mac_gyver.is_won(map_mac_gyver,
                                       display_window)

            # Exit the window if the player win the game or died
            if character_mac_gyver.position_player == \
                    map_mac_gyver.position_exit:
                self.display_game = False
                self.win_menu = True

            if character_mac_gyver.position_player == \
                    map_mac_gyver.position_guardian \
                    and len(character_mac_gyver.counter) != 2:
                self.display_game = False
                self.dead_menu = True
            # Display the window after actions
            display_window.window.blit(display_window.background, (0, 0))
            display_window.display_images_on_map(
                character_mac_gyver.map_new_player,
                character_mac_gyver.position_player)

            # Reload screen
            pygame.display.flip()

    def dead_menu_loop(self):
        """Display the end menu when the player dies"""
        # Display the menu in the window
        dead_window = pygame.image.load(
            os.path.join('ressource', "end_menu.jpg")).convert()
        dead_window_on_scall = pygame.transform.scale(
            dead_window, (SIDE_WINDOW, SIDE_WINDOW))
        self.start_window.blit(dead_window_on_scall, (0, 0))

        # Refresh the window
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.dead_menu = False
                self.continue_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b or event.key == pygame.K_ESCAPE:
                    self.dead_menu = False
                    self.continue_game = False
                    self.win_menu = False

                if event.key == pygame.K_a:
                    self.dead_menu = False
                    self.display_game = False
                    self.continue_game = True
                    self.win_menu = False
                    self.display_menu = True

    def win_menu_loop(self):
        """Display the end menu when the player wins"""
        # Display the menu in the window
        win_window = pygame.image.load(
            os.path.join('ressource', "end_menu.jpg")).convert()
        win_window_on_scall = pygame.transform.scale(win_window,
                                                     (SIDE_WINDOW,
                                                      SIDE_WINDOW))
        self.start_window.blit(win_window_on_scall, (0, 0))

        # Refresh the window
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.win_menu = False
                self.continue_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b or event.key == pygame.K_ESCAPE:
                    self.win_menu = False
                    self.continue_game = False

                if event.key == pygame.K_a:
                    self.win_menu = False
                    self.dead_menu = False

                    self.display_game = False
                    self.continue_game = True
                    self.display_menu = True

    def display_menus(self):
        display_window = Display()
        while self.continue_game:
            map_mac_gyver = Map("base_map")
            character_mac_gyver = Character(map_mac_gyver.position_player,
                                            map_mac_gyver.positions_walls,
                                            map_mac_gyver.map)
            self.main_loop()

            # Loop for the menu
            self.display_objects(map_mac_gyver)

            while self.display_menu:
                self.menu_loop()

            # Loop for the game
            while self.display_game:
                self.display_game_loop(map_mac_gyver, character_mac_gyver,
                                              display_window)
                # If MacGyver dies, the game display the dead menu

                while self.dead_menu:
                    self.dead_menu_loop()

                # If MacGyver wins, the game display the win menu
                while self.win_menu:
                    self.win_menu_loop()
