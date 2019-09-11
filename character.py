from map import *


# Class character : Allow a character to move
class Character:
    def __init__(self, get_position_player):
        """Initializing the class Character with:
        - Get_position_player"""
        self.get_position_player = get_position_player

    def move_player(self, next_move):
        """Move the player into the labyrinth and return the new position"""
        if next_move == "q":
            self.get_position_player[1] -= 1
            return self.get_position_player[1]
        elif next_move == "d":
            self.get_position_player[1] += 1
            return self.get_position_player[1]
        elif next_move == "s":
            self.get_position_player[0] += 1
            return self.get_position_player[0]
        elif next_move == "z":
            self.get_position_player[0] -= 1
            return self.get_position_player[0]

    def __repr__(self):
        return "{}".format(self.get_position_player)

