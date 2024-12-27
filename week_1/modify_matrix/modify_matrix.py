def transpose(matrix: List[List[int]]) -> List[List[int]]:
    transposed = []
    for _ in range(len(matrix[0])):
        transposed.append([])

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            print(j)
            transposed[j].append(cell)
    
    return transposed


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix = transpose(matrix)
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == -1:
                    matrix[i][j] = max(row)
        return transpose(matrix)
