from Game import *
import pygame


def main():
    """Main to launch the game"""
    pygame.init()
    launch_game = Game()
    launch_game.display_menus()


if __name__ == '__main__':
    main()
