# ------------------------ Imports ------------------------
# Interface imports
from player_interfaces.player_template import player
from connect_four_board import connect_four_board as cf_board
from player_interfaces.random_player import random_player as r_player
from LuizaStefAI import connect_four_player as cf_player
from game_interface.board_interface import board as board_int

# Import game manager
from game import game


# ------------------------ Methods ------------------------
def board_selector() -> board_int:
    """
    Method to select the type of game to play.
    :return: The board object to play on.
    """

    return cf_board()


def player_selector() -> list[player]:
    """
    Method to select players through a user interface.
    :return: A list of players.
    """
    return list((cf_player("Y", "Yannick"), r_player("R", "Roos")))


# Start the game
state = game(player_selector(), board_selector())
winner = state.start_game()
print(state.board)
print(cf_player.get_move(self=cf_player, board=board_int))
if winner is None:
    print("Draw")
else:
    print(winner.name)
