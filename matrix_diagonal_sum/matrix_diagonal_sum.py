class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagSum: int = 0

        rows: int = len(mat)
        columns: int = len(mat[0])
        has_center: bool = rows % 2 != 0 and columns % 2 != 0

        for i, j in zip(range(rows), range(columns)):
            if not has_center or (i != rows // 2 and j != columns // 2):
                diagSum += mat[i][j]

        for i, j in zip(range(rows), range(columns)[::-1]):
            diagSum += mat[i][j]


        return diagSum
