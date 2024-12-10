# ------------------------ Imports ------------------------
# Interface imports
from game_interface.move_interface import move as move_int

# ------------------------ Extension ------------------------
class connect_four_move(move_int):
    """
    Class to store coordinates and the player of a (legal) connect four move.
    """

    def __init__(self, player: str, column: int, row: int):
        super().__init__(player)
        self.column = column
        self.row = row

    def __repr__(self) -> str:
        """
        Method to return a representation of a move in a string.
        :return: A representation of a move in a string.
        """
        result = "("
        elements = [("Column: ", str(self.column)), ("Row: ", str(self.row))]
        for i in range(len(elements)):
            result += elements[i][0] + elements[i][1]
            if i + 1 is not len(elements):
                result += ", "

        result += ")"
        return result

    def get_column(self) -> int:
        """
        Method to get the column coordinate of the move.
        :return: The column coordinate of the move.
        """
        return self.column

    def get_row(self) -> int:
        """
        Method to get the row coordinate of the move.
        :return: The row coordinate of the move.
        """
        return self.row
