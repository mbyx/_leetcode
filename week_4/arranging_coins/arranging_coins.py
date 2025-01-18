class Solution:
    def arrangeCoins(self, n: int) -> int:
        start: int = 0
        end: int = n

        while start <= end:
            middle: int = (start + end) // 2
            coins_needed: int = middle * (middle + 1) / 2
            if coins_needed > n:
                end = middle - 1
            elif coins_needed < n:
                start = middle + 1
            else:
                return middle

        return start - 1
