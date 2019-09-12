import os
import random


# Class map : Get the maps in a file and launch it
class Map:
    def __init__(self, map_name):
        """Initializing class Map with :
        - Name
        - Map
        - Start position
        - Exit position
        - Position Wall
        - clean Map"""
        self.map = []
        self.map_name = map_name
        self.map = self.launch_map()
        self.position_player = self.find_position_player()
        self.position_exit = self.find_position_exit()
        self.positions_wall = self.find_positions_wall('O')

    def launch_map(self):
        """Call the file of the map and put it in a list which contains the rows"""
        for self.map_name in os.listdir("maps"):
            if self.map_name.endswith(".txt"):
                path = os.path.join("maps", self.map_name)
                with open(path, "r") as files:
                    for line in files:
                        theret = []
                        for chr in line:
                            theret.append(chr)
                        self.map.append(theret)
                    #contains = files.read()
                    #self.map = contains.split("\n")
                    return self.map

    def __repr__(self):
        """Print the map and join the rows with position player"""
        self.map[0] + self.map[1]
        return "\n".join(self.map)

    def find_position_char(self, the_char):
        """Find the position of a character in the map"""
        idx_row = 0
        for row in self.map:
            if the_char in row:
                idx_col = row.index(the_char)
                return [idx_row, idx_col]
            idx_row += 1

    def find_position_player(self):
        """Find the position of the player"""
        return self.find_position_char("S")

    def find_position_exit(self):
        """Find the position of the exit"""
        return self.find_position_char("E")

    def find_positions_wall(self, char_walls):
        """Find the position of a character in the map"""
        # nb_col = len(self.map[0])
        # nb_row = len(self.map[1])
        # walls = [(x, y) for x in enumerate(nb_row) for y in enumerate(nb_col) if self.map[x][y] == 'O']
        # return walls
        walls = []
        for row in self.map:
            if char_walls in row:
                walls.append((self.map.index(row), row.index(char_walls)))
            return walls

    def get_clean_map(self, the_char):
        """Clean the start character after getting the positions"""
        the_ret = []
        for row in self.map:
            if the_char in row:
                the_char = " "
            the_ret.append(row)
        return the_ret


    def is_won(self):
        """Return True when the game is won"""
        if self.position_player == self.position_exit:
            print("Bravo!! Tu as réussi à sortir du labyrinthe!!!")
            return True

    def post_object(self):
        nb_col = len(self.map[0])
        nb_row = len(self.map[1])
        find_object = [(x, y) for x in range(nb_row) for y in range(nb_col) if self.map[x][y] != 'O' and self.map[x][y]
                       != 'S' and self.map[x][y] != 'E']
        position_object = random.choice(find_object)
        x = position_object[0]
        y = position_object[1]
        self.map[x][y] = 'A'

        #for row in self.map:
          #  for elt in row:
          #      self.map[x] = 'A'
        #return "\n".join(self.map)
