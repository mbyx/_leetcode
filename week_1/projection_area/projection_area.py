class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        columns: int = len(grid[0])

        xy: int = 0
        for row in grid:
            for cell in row:
                if cell != 0:
                    xy += 1

        xz: int = sum([max(row) for row in grid])

        yz: int = 0
        for column in range(columns):
            yz += max([row[column] for row in grid])

        return xy + xz + yz
