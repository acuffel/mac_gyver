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
        move_row = self.position_player[0]
        move_col = self.position_player[1]
        if next_move == "q":
            move_col -= 1 #move left
            if tuple(self.position_player) in self.positions_wall:
                return self
            return self.position_player
        elif next_move == "d":
            move_col += 1 #move right
            if tuple(self.position_player) in self.positions_wall:
                return self
            return self.position_player
        elif next_move == "s":
            move_row += 1 #move down
            if tuple(self.position_player) in self.positions_wall:
                return self
            return self.position_player
        elif next_move == "z":
            move_row -= 1 #move up
            if tuple(self.position_player) in self.positions_wall:
                return self
            return self.position_player

    def __repr__(self):
        return "{}".format(self.position_player)

