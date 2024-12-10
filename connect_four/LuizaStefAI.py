# ------------------------ Imports ------------------------
# Connect four imports
from connect_four_board import connect_four_board as cf_board
from connect_four_move import connect_four_move as cf_move
import random
import math
#from interface import kleur

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
        my_player = "Y"
        enemy_player = "R"
        depth = 5
        possible_moves = board.possible_moves(my_player)

        _, best_move = self.minmax(depth, board, True, my_player, enemy_player, -math.inf, math.inf)
        # print(best_move)
        if best_move == None:
            best_move = random.choice(possible_moves)
        return best_move
    
    def minmax(self, depth, board : cf_board, is_max, my_player, enemy_player, alpha, beta):

        winner = board.get_winner()
        if depth == 0 or winner is not None:
            if winner == 0:
                return 1000, None
            elif winner == 1:
                return -1000, None
            elif winner == -1: 
                return 0, None
            return 0, None

        if is_max:
            best_value = -math.inf
            possible_moves = board.possible_moves(my_player)
        else:
            best_value = math.inf
            possible_moves = board.possible_moves(enemy_player)

        best_move = None

        for move in possible_moves:
            copy_board = board.board_deepcopy()
            copy_board.make_move(move)

            new_value, _ = self.minmax(depth - 1, copy_board, not is_max, my_player, enemy_player, alpha, beta)

            col = move.get_column

            if col == 3:
                new_value += 10
            elif col == 2:
                new_value += 5
            elif col == 4:
                new_value += 5

            can_we_win = board.can_win(my_player)
            can_they_win = board.can_win(enemy_player)

            if is_max:
                
                if can_we_win:
                    new_value += 20
                elif can_they_win:
                    new_value -= 20

                if new_value > best_value:
                    best_value = new_value
                    best_move = move

                alpha = max(alpha, new_value)

            else:

                if can_they_win:
                    new_value += 20
                elif can_we_win:
                    new_value -= 20

                if new_value < best_value:
                    best_value = new_value
                    best_move = move

                beta = min(beta, new_value)
            
            if beta <= alpha:
                break
            
        # print(f"Depth: {depth},Current_move: {move}, Best_value: {best_value}, Best_move: {best_move}")
        return best_value, best_move


