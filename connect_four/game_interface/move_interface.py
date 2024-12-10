# ------------------------ Interface ------------------------
class move:
    """
    Move object to store the player and the move for a game.
    """
    def __init__(self, player: str):
        self.player = player

    def __repr__(self) -> str: ...

    def get_player(self) -> str:
        """
        Method to get the player of the move.
        :return: The player of the move.
        """
        return self.player
