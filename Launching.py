# -*-coding:Utf-8 -*

from character import *
from map import *

mac_gyver = Map("base_map")
# print("Ci-dessous la carte du jeu: \n")
# print(mac_gyver)
mac_gyver.get_clean_map("S")
print(mac_gyver.position_wall)

# won = False
# while not won:
#     choose_move = input_move()
#     deplacement = Character(mac_gyver.position_player)
#     deplacement.move_player(choose_move)
#     print(mac_gyver)
#     won = mac_gyver.is_won()

