from Map import *


# Class character : Allow a character to move
class Character:
    def __init__(self, get_position_player, get_positions_wall):
        """Initializing the class Character with:
        - Get_position_player"""
        self.get_position_player = get_position_player
        self.get_positions_wall = get_positions_wall

    def move_player(self, next_move):
        """Move the player into the labyrinth and return the new position"""
        move_row = self.get_position_player[0]
        move_col = self.get_position_player[1]
        if next_move == "q":
            move_col -= 1 #move left
            if tuple(self.get_position_player) in self.get_positions_wall:
                return self
            return move_col
        elif next_move == "d":
            move_col += 1 #move right
            if tuple(self.get_position_player) in self.get_positions_wall:
                return self
            return move_col
        elif next_move == "s":
            move_row -= 1 #move down
            if tuple(self.get_position_player) in self.get_positions_wall:
                return self
            return move_row
        elif next_move == "z":
            move_row += 1 #move up
            if tuple(self.get_position_player) in self.get_positions_wall:
                return self
            return move_row

    def __repr__(self):
        return "{}".format(self.get_position_player)

