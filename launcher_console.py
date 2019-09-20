# -*-coding:Utf-8 -*

from Character import *
from Map import *

map_mac_gyver = Map("base_map")
character_mac_gyver = Character(map_mac_gyver.position_player, map_mac_gyver.positions_walls, map_mac_gyver.map)
# movement = Character(mac_gyver.position_player, mac_gyver.positions_wall)#Call the class Character to move mac_gyver
print("Ci-dessous la carte du jeu: \n")
map_mac_gyver.post_object()
map_mac_gyver.clean_char("S")
print(character_mac_gyver)

won = False
dead = False
while not won or dead:
    choose_move = input("Entrer un mouvement pour déplacer Mac gyver") #We ask to the player to choose the move
    character_mac_gyver.move_player(choose_move)
    print(character_mac_gyver)
    character_mac_gyver.catch_object(map_mac_gyver, map_mac_gyver, "A", "B")
    dead = character_mac_gyver.pass_guardian(map_mac_gyver, map_mac_gyver)
    won = character_mac_gyver.is_won(map_mac_gyver)




