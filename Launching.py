# -*-coding:Utf-8 -*

from character import *
from map import *

mac_gyver = Map("base_map")
print("Ci-dessous la carte du jeu: \n")
print(mac_gyver)
mac_gyver.get_clean_map("S")


won = False
while not won:
    choose_move = input("Entrer un mouvement pour déplacer Mac gyver")
    deplacement = Character(mac_gyver.position_player)
    move = deplacement.move_player(choose_move) #Rework in movement
    # if tuple(mac_gyver.position_player) not in mac_gyver.find_position_wall(): #We check if the position is not in a wall
    print(mac_gyver)
    won = mac_gyver.is_won()



