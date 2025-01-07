class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        li: int = 0
        ri: int = k
        min_diff: int = 10e6 # > than given constraint.
        length = len(nums)

        while ri != length + 1:
            diff: int = abs(nums[li] - nums[ri - 1])
            if diff < min_diff:
                min_diff = diff
            li += 1
            ri += 1

        return min_diff
