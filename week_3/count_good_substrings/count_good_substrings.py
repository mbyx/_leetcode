import collections

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k: int = 3
        count: int = 0

        for i in range(len(s) - k + 1):
            counter = collections.Counter()
            for j in range(k):
                counter[s[i + j]] += 1
            if all([v == 1 for (_, v) in counter.items()]):
                count += 1

        return count
