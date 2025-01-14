class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start: int = 0
        # It's impossible to have a square root bigger than this.
        end: int = num // 2 + 1

        while start <= end:
            middle = (start + end) // 2
            square = middle * middle
            if square > num:
                end = middle - 1
            elif square < num:
                start = middle + 1
            else:
                return True
        return False
