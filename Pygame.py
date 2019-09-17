import pygame
import os

class Pygame():

    pygame.init()
    clock = pygame.time.Clock()


    def main():
        # Open window pygame
        window = pygame.display.set_mode((640, 480))

        # Loading and display fond
        fond = pygame.image.load(os.path.join('ressource', "floor-tiles-20x20.png")).convert()
        window.blit(fond, (0, 0))

        # Loading and display mac gyver
        img_mac_gyver = pygame.image.load(os.path.join('ressource', "MacGyver.png")).convert_alpha()
        position_mac_gyver = img_mac_gyver.get_rect()
        window.blit(img_mac_gyver, position_mac_gyver)

        loop = True
        while loop:

            # Event for closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        position_mac_gyver = position_mac_gyver.move(0,3)

            window.blit(fond, (0, 0))
            window.blit(img_mac_gyver, position_mac_gyver)

            # Reload screen
            pygame.display.flip()
            # 10 fps
            clock.tick(10)


    if __name__ == '__main__':
        main()
