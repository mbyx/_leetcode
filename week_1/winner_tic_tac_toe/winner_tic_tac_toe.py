class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        toes: int = 0
        o_wins: bool = False
        x_wins: bool = False

        # Converting input to previous tic tac toe input format
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        player_A = True
        for move in moves:
            board[move[0]][move[1]] = 'X' if player_A else 'O'
            player_A = not player_A

        board = [''.join(row) for row in board]

        # Reusing code because I can
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
                if cell == 'X' or cell == 'O':
                    toes += 1

        if o_wins:
            return 'B'
        elif x_wins:
            return 'A'
        elif toes != 9:
            return 'Pending'
        else:
            return 'Draw'
