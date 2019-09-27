# Class character : Allow a character to move
class Character:
    def __init__(self, position_player, positions_walls, game_map):
        """Initializing the class Character with:
        - Get_position_player"""
        self.position_player = position_player
        self.positions_walls = positions_walls
        self.game_map = game_map
        self.map_new_player = self.get_state_player('X')
        self.counter = []

    def move_player(self, next_move):
        """Move the player into the labyrinth and return the new position"""
        # move left
        if next_move == "q":
            self.position_player[1] -= 1
            if tuple(self.position_player) in self.positions_walls:
                self.position_player[1] += 1
            return self.position_player[1]
        # move right
        elif next_move == "d":
            self.position_player[1] += 1
            if tuple(self.position_player) in self.positions_walls:
                self.position_player[1] -= 1
            return self.position_player[1]
        # move down
        elif next_move == "s":
            self.position_player[0] += 1
            if tuple(self.position_player) in self.positions_walls:
                self.position_player[0] -= 1
            return self.position_player[0]
        # move up
        elif next_move == "z":
            self.position_player[0] -= 1
            if tuple(self.position_player) in self.positions_walls:
                self.position_player[0] += 1
            return self.position_player[0]

    def get_state_player(self, the_char):
        """When the player is moving, it returns a new version of the map with the new position of the player"""
        the_ret = []
        idx_row = 0
        for row in self.game_map:
            if idx_row == self.position_player[0]:
                temp = list(row)
                temp[self.position_player[1]] = the_char
                the_ret.append("".join(temp))
            else:
                the_ret.append(row)
            idx_row += 1
        return the_ret

    def __repr__(self):
        """Print the map and join the rows with position player"""
        return "".join([''.join(a) for a in self.get_state_player('X')])

    def catch_object(self, clean, position_char, display, *objects_on_map):
        """Create a list of objects when the player catch one"""
        objects_catch = list(objects_on_map)
        for object in objects_catch:
            if self.position_player == position_char.find_position_char(object):
                self.counter.append(object)
                display.display_text_on_map("Félicitations! Vous avez récupéré l'objet : {}".format(object))
                clean.clean_char(object)

    def pass_guardian(self, clean, position_guardian, display):
        """Remove the guardian when the player get all objects, otherwise he dies"""
        if self.position_player == position_guardian.find_position_guardian():
            if len(self.counter) == 2:
                display.display_text_on_map("Bien joué, Tu as réussi à endormir le garde")
                clean.clean_char("G")
            else:
                display.display_text_on_map("Mac Gyver n'a pas réussi à récupérer tous les objets, il en est mort...")

    def is_won(self, position_exit, display):
        """Return True when the game is won"""
        if self.position_player == position_exit.find_position_exit():
            display.display_text_on_map("Bravo!! Tu as réussi à sortir du labyrinthe!!!")
