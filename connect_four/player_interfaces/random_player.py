# ------------------------ Imports ------------------------
# Interface imports
from game_interface.board_interface import board as board_int
from player_interfaces.player_template import player

# Utility import
from random import randrange


# ------------------------ Extension ------------------------
class random_player(player):
    """
    A player that makes a random move.

    First boss for a student to beat.
    """

    def get_move(self, board: board_int):
        """
        Method to get the next move of the player
        :param board: The board for a board state.
        :return: A (random) move to play in a game.
        """
        possible_moves = board.possible_moves(self.color)

        return possible_moves[randrange(len(possible_moves))]
