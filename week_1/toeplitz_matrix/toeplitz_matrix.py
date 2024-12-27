class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows: int = len(matrix)
        columns: int = len(matrix[0])

        for row in range(rows - 1):
            for column in range(columns - 1):
                if matrix[row][column] != matrix[row + 1][column + 1]:
                    return False

        return True
