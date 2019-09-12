# -*-coding:Utf-8 -*

from Character import *
from Map import *

mac_gyver = Map("base_map")
print("Ci-dessous la carte du jeu: \n")

#print(mac_gyver.post_object())
print(mac_gyver)


won = False
while not won:
    choose_move = input("Entrer un mouvement pour déplacer Mac gyver") #We ask to the player to choose the move
    movement = Character(mac_gyver.position_player, mac_gyver.positions_wall)#Call the class Character to move mac_gyver
    move = movement.move_player(choose_move)
    print(mac_gyver)

    print(mac_gyver.position_player)

    won = mac_gyver.is_won()




