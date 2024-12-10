# ------------------------ Imports ------------------------
# Connect four imports
from connect_four_board import connect_four_board as cf_board
from connect_four_move import connect_four_move as cf_move

from random import randrange

# Interface imports
from player_interfaces.player_template import player as player_int


# ------------------------ Extension ------------------------
class connect_four_player(player_int):
    """
    Connect four player, to be implemented by the student.
    """
    def __init__(self, color: str, name: str):
        super().__init__(color, name)

    def get_move(self, board: cf_board) -> cf_move:
        """
        Method to get the move this player makes.
        :param board: A deepcopy of the current board state.
        :return: A legal move that the player can make.
        """

        # TODO: implement
        available_moves = board.possible_moves(self.color)

        # return best_move
        return available_moves[0][randrange(len(available_moves))]
