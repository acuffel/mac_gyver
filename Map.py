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
        - Guardian position
        - Walls position"""
        self.map = []
        self.map_name = map_name
        self.map = self.launch_map()
        self.position_player = self.find_position_player()
        self.position_exit = self.find_position_exit()
        self.position_guardian = self.find_position_guardian()
        self.positions_walls = self.find_positions_walls()

    def launch_map(self):
        """Call the file of the map and put it in a list"""
        for self.map_name in os.listdir("maps"):
            if self.map_name.endswith(".txt"):
                path = os.path.join("maps", self.map_name)
                with open(path, "r") as files:
                    for line in files:
                        the_ret = []
                        for chr in line:
                            the_ret.append(chr)
                        self.map.append(the_ret)
                    return self.map

    def __repr__(self):
        """Print the map and join the rows with position player"""
        return "".join([''.join(a) for a in self.map])

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

    def find_position_guardian(self):
        """Find the position of the guardian"""
        return self.find_position_char("G")

    def find_positions_walls(self):
        """Find the position of a character in the map"""
        walls = []
        idx_row = 0
        for row in self.map:
            idx_col = 0
            for col in row:
                if "O" in col:
                    walls.append((idx_row, idx_col))
                idx_col += 1
            idx_row += 1
        return walls

    def clean_char(self, the_char):
        """Clean the start character after getting the positions"""
        idx_row = 0
        for row in self.map:
            idx_col = 0
            for col in row:
                if the_char in col:
                    self.map[idx_row][idx_col] = " "
                idx_col += 1
            idx_row += 1
        return self.map

    def post_object(self):
        """Create objects in the map"""
        find_objects = []
        idx_row = 0
        for row in self.map:
            idx_col = 0
            for col in row:
                if " " in col:
                    find_objects.append((idx_row, idx_col))
                idx_col += 1
            idx_row += 1
        random_position_object1 = random.choice(find_objects)
        random_position_object2 = random.choice(find_objects)
        if random_position_object1 != random_position_object2:
            x1 = random_position_object1[0]
            y1 = random_position_object1[1]
            x2 = random_position_object2[0]
            y2 = random_position_object2[1]
            self.map[x1][y1] = 'A'
            self.map[x2][y2] = 'B'
            return self.map
        else:
            return self
