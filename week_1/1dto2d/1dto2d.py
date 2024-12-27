class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        matrix: List[List[int]] = []
        for _ in range(m): # Cannot use [[]] * m due to python shenanigans.
            matrix.append([])

        row: int = 0
        for index, item in enumerate(original):
            if index != 0 and index % n == 0:
                row += 1
            matrix[row].append(item)

        return matrix
