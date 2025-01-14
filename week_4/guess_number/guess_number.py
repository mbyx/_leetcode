# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start: int = 1
        end: int = n
        while start <= end:
            middle: int = (start + end) // 2
            result: int = guess(middle)
            if result == -1:
                end = middle - 1
            elif result == 1:
                start = middle + 1
            else:
                return middle
        return start
