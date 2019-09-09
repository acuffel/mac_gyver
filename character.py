from map import *

# Class character : Allow a character to move
class Character:
    def __init__(self, get_position_player):
        """Initializing the class Character with:
        - Get_position_player"""
        self.get_position_player = get_position_player

    def move_player(self, next_move):
        """Move the player into the labyrinth and return the new position"""
        if next_move == 'O':
            self.get_position_player[1] -= 1
            return self.get_position_player[1]
        elif next_move == "E":
            self.get_position_player[1] += 1
            return self.get_position_player[1]
        elif next_move == "S":
            self.get_position_player[0] += 1
            return self.get_position_player[0]
        elif next_move == "N":
            self.get_position_player[0] -= 1
            return self.get_position_player[0]


def input_move():
    """Check if the client """
    choice = input("Veuillez saisir un déplacement \n E : EST\n "
                  "O : OUEST \n N : NORD \n S : SUD \n")
    choice = choice.upper()
    try:
        if choice in ["E", "N", "S", "O"]:
            return choice
        else:
            print("Il y a des erreurs dans la saisie de votre déplacement")
            return input_move()
    except ValueError:
        print("Attention, ce n'est pas un déplacement autorisé \n")
        return input_move()
