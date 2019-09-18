# -*-coding:Utf-8 -*

from Character import *
from Map import *

mac_gyver = Map("base_map")
# movement = Character(mac_gyver.position_player, mac_gyver.positions_wall)#Call the class Character to move mac_gyver
print("Ci-dessous la carte du jeu: \n")
mac_gyver.post_object()
mac_gyver.clean_char("S")
print(mac_gyver)

won = False
dead = False
while not won or dead:
    choose_move = input("Entrer un mouvement pour déplacer Mac gyver") #We ask to the player to choose the move
    mac_gyver.move_player(choose_move)
    print(mac_gyver)
    mac_gyver.catch_object("A", "B")
    dead = mac_gyver.pass_guardian()
    won = mac_gyver.is_won()




