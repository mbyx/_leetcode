import collections

class Solution:
    def maximumLength(self, s: str) -> int:
        n: int = len(s)
        occurences = collections.Counter()

        for k in range(n + 1):
            for i in range(n - k + 1):
                substr: str = ''
                for j in range(k):
                    substr += s[i + j]

                counter = collections.Counter(substr)
                if len(counter) == 1:
                    occurences[substr] += 1

        lengths = [len(substr) for (substr, count) in occurences.items() if count >= 3]
        return -1 if len(lengths) == 0 else max(lengths)
