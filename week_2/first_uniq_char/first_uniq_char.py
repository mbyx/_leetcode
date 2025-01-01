import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [char for (char, count) in collections.Counter(s).most_common() if count == 1]
        if len(chars) != 0:
            return s.index(chars[0])
        else:
            return -1
