class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xs: int = 0
        os: int = 0
        o_wins: bool = False
        x_wins: bool = False

        # Checking for wins
        # Multiple n^2 loops for readability

        # Columns
        for i in range(3):
            column = ''
            for row in board:
                column += row[i]

            if column == 'OOO':
                o_wins = True
            elif column == 'XXX':
                x_wins = True

        # Rows
        for row in board:
            if row == 'OOO':
                o_wins = True
            elif row == 'XXX':
                x_wins = True

        # Diagonals
        primary = ''
        secondary = ''
        for i in range(3):
            for j in range(3):
                if i == j:
                    primary += board[i][j]
                if i + j == 2:
                    secondary += board[i][j]
        if primary == 'XXX' or secondary == 'XXX':
            x_wins = True
        if primary == 'OOO' or secondary == 'OOO':
            o_wins = True

        for row in board:
            for cell in row:
                if cell == 'X':
                    xs += 1
                if cell == 'O':
                    os += 1

        if os > xs:
            return False
        elif abs(xs - os) > 1:
            return False
        elif x_wins and o_wins:
            return False
        elif x_wins and xs == os:
            return False
        elif o_wins and os < xs:
            return False

        return True
