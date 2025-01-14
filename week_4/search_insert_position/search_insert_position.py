class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start: int = 0
        end: int = len(nums) - 1
        while start <= end:
            middle: int = (start + end) // 2
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            else:
                return middle
        return start
