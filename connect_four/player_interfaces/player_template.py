# ------------------------ Imports ------------------------
# Interface imports
from game_interface.board_interface import board as board_int
from game_interface.move_interface import move as move_int


# ------------------------ Interface ------------------------
class player:
    """
    Player interface to be implemented by students.
    """

    def __init__(self, color: str, name: str):
        self.name = name
        self.color = color

    def get_name(self) -> str:
        """
        Method to return the name of the player.
        :return: The name of the player as a string.
        """
        return self.name

    def get_move(self, board: board_int) -> move_int: ...
