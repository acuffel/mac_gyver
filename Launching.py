# -*-coding:Utf-8 -*

from character import *
from map import *

mac_gyver = Map("base_map")
print("Ci-dessous la carte du jeu: \n")
print(mac_gyver)
mac_gyver.get_clean_map("S")


won = False
while not won:
    choose_move = input("Entrer un mouvement pour déplacer Mac gyver") #We ask to the player to choose the move

    deplacement = Character(mac_gyver.position_player) #Call the class Character to move mac_gyver
    move = deplacement.move_player(choose_move)

    if tuple(mac_gyver.position_player) in mac_gyver.find_position_wall(): #We check if the position is in a wall
        if choose_move == "d":
            deplacement.get_position_player[1] -= 1
        elif choose_move == "q":
            deplacement.get_position_player[1] += 1
        elif choose_move == "z":
            deplacement.get_position_player[0] += 1
        elif choose_move == "s":
            deplacement.get_position_player[0] -= 1

    print(mac_gyver)
    won = mac_gyver.is_won()



