from Map import *


# Class character : Allow a character to move
class Character:
    def __init__(self, position_player, positions_wall):
        """Initializing the class Character with:
        - Get_position_player"""
        self.position_player = position_player
        self.positions_wall = positions_wall

    def move_player(self, next_move):
        """Move the player into the labyrinth and return the new position"""
        # move left
        if next_move == "q":
            self.position_player[1] -= 1
            if tuple(self.position_player) in self.positions_wall:
                return self
            else:
                return self.position_player
        # move right
        elif next_move == "d":
            self.position_player[1] += 1
            if tuple(self.position_player) in self.positions_wall:
                return self
            else:
                return self.position_player
        # move down
        elif next_move == "s":
            self.position_player[0] += 1
            if tuple(self.position_player) in self.positions_wall:
                return self
            else:
                return self.position_player
        # move up
        elif next_move == "z":
            self.position_player[0] -= 1
            if tuple(self.position_player) in self.positions_wall:
                return self
            else:
                return self.position_player

    def __repr__(self):
        return "{}".format(self.position_player)

