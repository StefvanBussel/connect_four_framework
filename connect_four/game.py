# ------------------------ Imports ------------------------
# Interface imports
from player_interfaces.player_template import player as player_int
from game_interface.move_interface import move as move_int
from game_interface.board_interface import board as board_int
from appJar.appjar import *
from connect_four_move import connect_four_move
from LuizaStefAI import connect_four_player as cf_player
# ------------------------ Class & function ------------------------
def print_board_state(board: board_int):
    # def kleur():
    #     kleur = app.addLabelEntry("Welke kleur kies je? (rood/groen/roze)", 2, 0 ,7) 
    #     if kleur == "rood":
    #         kleur == "R"
    #     elif kleur == "groen":
    #         kleur == "G"
    #     else:
    #         kleur == "P"
    #     return kleur

    # def beginSpel():
    #     for x in range (1, 7) : 
    #         for i in range (0, 7) :
    #             app.addImage("zwarte bol" + str(x) + str(i), "zwarteBol.gif", x, i)

    # app = gui("Grid", "400x500")
    # app.setBg("blue")
    # app.setFg("white")
    # app.addLabel("titel", "Connect four", 0, 0, 7)
    # app.addLabel("naam", "Wat is je naam? ", 1, 0, 7)
    # kleurSpeler = kleur()
    # app.addButton("Begin spel", beginSpel)

    # app.go()
    pass
    # TODO: implement


class game:
    """
    Object to manage a game.
    Comes with relevant methods to control the game flow and update game states.
    """

    def __init__(self, player_list: list[player_int], board: board_int):
        # Initialize the board
        self.board = board

        # Initialize the player list and make sure there are enough players to play the game
        self.player_list = player_list
        if len(self.player_list) < self.board.minimum_players():
            raise Exception("Cannot have less then " + str(self.board.minimum_players()) + " players")
        elif len(self.player_list) > self.board.maximum_players():
            raise Exception("Cannot have more then " + str(self.board.maximum_players()) + " players")

        # Initialize the turn.
        # The turn is the index of the active player in the player list.
        self.turn = 0

        # Try counter, for games that have multiple moves per turn.
        # IMPORTANT: Starts at 1 because we do not start counting tries at 0.
        self.tries = 1

    def __update_turn(self):
        """
        Method to update the turn.
        Please do not use unless you know what you are doing.
        """

        # Loop around if tries has reached is maximum.
        if self.tries is self.board.maximum_tries():
            self.tries = 1

            # Loop around if turn is out of bounds for the list length.
            if self.turn is (len(self.player_list) - 1):
                self.turn = 0
            else:
                self.turn += 1
        else:
            self.tries += 1

    def make_move(self, move: move_int):
        """
        Make a move in the game.
        :param move: The move to be made.
        """
        self.board.make_move(move)
        self.__update_turn()

    def get_players_list(self) -> list[player_int]:
        """
        Get all the players.
        :return: The list of players
        """
        return self.player_list

    def start_game(self) -> player_int:
        """
        Method to initiate a game sequence.
        :return: The winner, else, None (draw).
        """
        winner: int
        winner = self.board.get_winner()
        while winner is None:
            self.make_move(self.player_list[self.turn].get_move(self.board.board_deepcopy()))

            print_board_state(self.board.board_deepcopy())

            winner = self.board.get_winner()

        return self.get_players_list()[winner] if winner >= 0 else None
