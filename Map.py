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
        self.positions_wall = self.find_positions_wall()


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
        return "".join([''.join(a) for a in self.get_state_player("X")])

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

    def find_positions_wall(self):
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

    def get_state_player(self, the_char):
        """Return a new version of the map with the new place of the player"""
        the_ret = []
        idx_row = 0
        for row in self.map:
            if idx_row == self.position_player[0]:
                temp = list(row)
                temp[self.position_player[1]] = the_char
                the_ret.append("".join(temp))
            else:
                the_ret.append(row)
            idx_row += 1
        return the_ret

    def move_player(self, next_move):
        """Move the player into the labyrinth and return the new position"""
        # move left
        if next_move == "q":
            self.position_player[1] -= 1
            if tuple(self.position_player) in self.positions_wall:
                return self
            return self.position_player[1]
        # move right
        elif next_move == "d":
            self.position_player[1] += 1
            if tuple(self.position_player) in self.positions_wall:
                return self
            return self.position_player[1]
        # move down
        elif next_move == "s":
            self.position_player[0] += 1
            if tuple(self.position_player) in self.positions_wall:
                return self
            return self.position_player[0]
        # move up
        elif next_move == "z":
            self.position_player[0] -= 1
            if tuple(self.position_player) in self.positions_wall:
                return self
            return self.position_player[0]

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

