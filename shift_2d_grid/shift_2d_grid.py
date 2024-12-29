class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m: int = len(grid)
        n: int = len(grid[0])

        for _ in range(k):
            temp_column: list[int] = []

            for ri in range(m):
                for ci in range(n)[::-1]:
                    if ci == n - 1:
                        temp_column.append(grid[ri][ci])
                    else:
                        grid[ri][ci + 1] = grid[ri][ci]

            temp_column.insert(0, temp_column.pop())

            for ri in range(m)[::-1]:
                grid[ri][0] = temp_column.pop()

        return grid
