class TicTacToe:
    """
    Idea:
        In each move, check if a row, col, dia is filled
        If not, update the corresponding array of the value
    """

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.dia = 0
        self.an_dia = 0

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
        self.rows[row] = self.rows[row] + 1 if player == 1 else self.rows[row] - 1
        self.cols[col] = self.cols[col] + 1 if player == 1 else self.cols[col] - 1
        if row == col:
            self.dia = self.dia + 1 if player == 1 else self.dia - 1
        if row + col + 1 == len(self.rows):
            self.an_dia = self.an_dia + 1 if player == 1 else self.an_dia - 1
        if self.dia == len(self.rows) or self.an_dia == len(self.rows) or self.rows[row] == len(self.rows) or self.cols[col] == len(self.cols):
            return 1
        elif self.dia == -len(self.rows) or self.an_dia == -len(self.rows) or self.rows[row] == -len(self.rows) or self.cols[col] == -len(self.cols):
            return 2
        else:
            return 0

