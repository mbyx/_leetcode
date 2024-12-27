def removeRow(mat: List[List[int]], row_index: int) -> tuple[List[List[int]], List[int]]:
    """Remove row from matrix and return new matrix and row that was removed."""
    return ([row for index, row in enumerate(mat) if index != row_index], mat[row_index] if len(mat) != 0 else [])

def removeColumn(mat: List[List[int]], column_index: int) -> tuple[List[List[int]], List[int]]:
    """Remove column from matrix and return new matrix and column that was removed."""
    matrix = []
    column = []
    for row_index, row in enumerate(mat):
        matrix.append([])
        for index, cell in enumerate(row):
            if index != column_index:
                matrix[row_index].append(cell)
            else:
                column.append(cell)
    return (matrix, column)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral: list[int] = []
        ri: int = 0
        ci: int = 0

        m: int = len(matrix)
        n: int = len(matrix[0])

        while len(spiral) != m * n:
            matrix, top = removeRow(matrix, 0)
            if matrix == []:
                spiral += top
                break

            matrix, right = removeColumn(matrix, len(matrix[0]) - 1)
            matrix, bottom = removeRow(matrix, len(matrix) - 1)
            matrix, left = removeColumn(matrix, 0)

            for item in top + right + bottom[::-1] + left[::-1]:
                spiral.append(item)

        return spiral
