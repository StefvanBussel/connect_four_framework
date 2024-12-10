# ------------------------ Imports ------------------------
# Interface import
from game_interface.board_interface import board as board_int
# Connect four imports
from connect_four_move import connect_four_move as cf_move


# ------------------------ Extension ------------------------
class connect_four_board(board_int):
    """
    Board object to store the board of a connect four game.
    """

    def __init__(self):
        super().__init__()
        self.column_size = 7
        self.row_size = 6

        # Initialize the board (7 columns, 6 rows)
        self.board = []
        for i in range(self.column_size):
            self.board.append([None] * self.row_size)

    def __repr__(self) -> str:
        """
        Method to have a string version of the board.
        This can be used in a user interface or for debugging purposes.
        :return: A string representation of the board.
     snac   """
        return ("    {0:4} {1:4} {2:4} {3:4} {4:4} {5:4} {6:4}\n".format("A", "B", "C", "D", "E", "F", "G")
                + "".join([(str(row + 1) + " | " if column == 0 else " ")
                           + ("{0:4} |\n" if column == (self.column_size - 1) else "{0:4}")
                           .format(((str(self.board[column][row])) if (self.board[column][row]) is not None else " "))
                           for row in range(self.row_size) for column in range(self.column_size)]))

    def minimum_players(self) -> int:
        """
        Method to return the minimum amount of players allowed.
        :return: The minimum number of players.
        """
        return 2

    def maximum_players(self) -> int:
        """
        Method to return the maximum amount of players allowed.
        :return: The maximum number of players.
        """
        return 2

    def board_deepcopy(self) -> board_int:
        """
        Method to deepcopy the board object.
        :return: A deepcopy of the board object.
        """

        new_board = connect_four_board()
        for row in range(self.row_size):
            for column in range(self.column_size):
                new_board.board[column][row] = self.board[column][row]

        return new_board

    def make_move(self, move: cf_move) -> board_int:
        """
        Method to advance the game state.
        :param move: Input move to be made.
        :return: Itself, fully updated.
        """

        self.board[move.get_column()][move.get_row()] = move.get_player()
        return self

    def can_win(self, player: str) -> bool:
        """
        Method to return if a player can win or not with the next move.
        :param player: The player to check.
        :return: True if the player can win, otherwise False.
        """

        # Get all possible moves
        possible_moves = self.possible_moves(player)

        # Loop through all possible moves, make a new board, make the move, check if there is a winner.
        # Return True if a winner is found.
        for move in possible_moves:
            winner = self.board_deepcopy().make_move(move).get_winner()
            if winner is not None and winner != -1:
                return True

        # If no winner was found, return False.
        return False

    def get_winner(self) -> int:
        """
        Method to check if there is a winner.
        :return: A player if there is a winner. If drawn, -1. Otherwise, None.
        """

        is_empty = True

        # Check horizontal and vertical for a winner
        for row in range(self.row_size):
            for column in range(self.column_size):
                # Define current cell and player
                player = self.board[column][row]

                # If the player is None, skip this iteration
                if player is None:
                    is_empty = False
                    continue
                else:
                    result = 1 if player == "R" else 0

                # Check if the next 3 cells have the same player (horizontal)
                if (column < (self.column_size - 3)
                        and self.board[column + 1][row] == player
                        and self.board[column + 2][row] == player
                        and self.board[column + 3][row] == player):
                    # Return if True
                    return result

                # Check if the next 3 cells have the same player (vertical)
                elif (row < (self.row_size - 3)
                      and self.board[column][row + 1] == player
                      and self.board[column][row + 2] == player
                      and self.board[column][row + 3] == player):
                    # Return if True
                    return result

                # Check if diagonally, the next 3 cells have the same player (top right to bottem left)
                elif (column < (self.column_size - 3)
                      and row > 2
                      and self.board[column + 1][row - 1] == player
                      and self.board[column + 2][row - 2] == player
                      and self.board[column + 3][row - 3] == player):
                    # Return if True
                    return result

                # Check if diagonally, the next 3 cells have the same player (top left to bottem right)
                elif (row < (self.row_size - 3)
                      and column < (self.column_size - 3)
                      and self.board[column + 1][row + 1] == player
                      and self.board[column + 2][row + 2] == player
                      and self.board[column + 3][row + 3] == player):
                    # Return if True
                    return result

        # Return nothing if there is no winner
        return None if not is_empty else -1

    def possible_moves(self, player: str) -> list[cf_move]:
        """
        Method to return all the current possible moves in a list (array).
        :param player: The player for which to return a list (array) of moves.
        :return: The list (array) of possible moves.
        """

        # Create an empty list for the return value
        result = list()

        # Iterate through all the columns of the board
        for column in range(self.column_size):

            # Check if there is still an empty pace in the column
            if None in self.board[column]:
                # Find the index of the first occurring None by reversing the list,
                # find the first occurrence of None,
                # then subtract that number of the (length - 1).
                # It is of upmost importance that reversed() is not used, since this changes the list,
                # while the used method uses a copy.
                row = self.row_size - 1 - self.board[column][::-1].index(None)
                result.append(cf_move(player, column, row))
        return result

        # Oneliner that does the same, but is less human-readable if you are not used to it.
        # return [cf_move(player, column, self.row_size - 1 - self.board[column][::-1].index(None))
        #         for column in range(self.column_size) if None in self.board[column]]

    def maximum_tries(self) -> int:
        return 1
