import functools

class Solution:
    @functools.cache
    def isHappy(self, n: int, max_steps: int = 50) -> bool:
        if max_steps == 0:
            return False
        if n == 1:
            return True

        happified: int = sum([int(c) ** 2 for c in str(n)])
        try:
            return self.isHappy(happified, max_steps - 1)
        except RecursionError:
            return False
