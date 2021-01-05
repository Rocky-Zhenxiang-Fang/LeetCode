class TicTacToe:
    """
    Idea:
        How can a player win a game?
            if he complete an entire row, col, or diagonal
        We can have array for row, col, diagonal to check if any player have win the game
    """

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.row = [0 for _ in range(n)]
        self.col = [0 for _ in range(n)]
        self.dia = 0
        self.anti_dia = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            movement = 1
        else:
            movement = -1
        self.row[row] += movement
        self.col[col] -= movement
        if row == col:
            self.dia += movement
        if row + col == self.size - 1:
            self.anti_dia += movement
        if abs(self.row[row]) == self.size or abs(self.col[col]) == self.size or abs(self.dia) == self.size or abs(self.anti_dia) == self.size:
            return player
        else:
            return 0

