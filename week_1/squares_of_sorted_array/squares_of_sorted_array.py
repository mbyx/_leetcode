class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []

        ri: int = len(nums) - 1
        li: int = 0
        while len(squares) != len(nums):
            left = abs(nums[li])
            right = abs(nums[ri])

            if left > right:
                squares.append(left ** 2)
                li += 1
            else:
                squares.append(right ** 2)
                ri -= 1

        return squares[::-1]
