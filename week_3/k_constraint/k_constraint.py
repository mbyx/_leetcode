class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n: int = len(s)
        count: int = 0

        for m in range(1, n + 1):
            for i in range(n - m + 1):
                ones: int = 0
                for j in range(m):
                    if s[i + j] == '1':
                        ones += 1
                if ones <= k or (j + 1) - ones <= k:
                    count += 1

        return count
