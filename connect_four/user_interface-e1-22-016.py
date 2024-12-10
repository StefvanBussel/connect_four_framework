# ------------------------ Imports ------------------------
# Interface imports
from player_interfaces.player_template import player
from game_interface.board_interface import board as board_int
import connect_four_board

# Import game manager
from game import game


# ------------------------ Methods ------------------------
def board_selector() -> board_int:
    """
    Method to select the type of game to play.
    :return: The board object to play on.
    """

    # TODO: implement

    return board_int()


def player_selector() -> list[player]:
    """
    Method to select players through a user interface.
    :return: A list of players.
    """

    # TODO: implement

    return list()


# Start the game
state = game(player_selector(), board_selector())
state.start_game()

# TODO: handle the termination of the game
