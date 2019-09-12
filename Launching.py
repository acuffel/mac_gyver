# -*-coding:Utf-8 -*

from Character import *
from Map import *

mac_gyver = Map("base_map")
# movement = Character(mac_gyver.position_player, mac_gyver.positions_wall)#Call the class Character to move mac_gyver
print("Ci-dessous la carte du jeu: \n")
mac_gyver.get_clean_map('S')
mac_gyver.post_object()


print(mac_gyver)


won = False
while not won:
    choose_move = input("Entrer un mouvement pour déplacer Mac gyver") #We ask to the player to choose the move

    mac_gyver.move_player(choose_move)

    print(mac_gyver)

    won = mac_gyver.is_won()




