class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot: int = 0
        end: int = len(nums) - 1

        while pivot < end:
            middle: int = (pivot + end) // 2
            if nums[middle] > nums[end]:
                pivot = middle + 1
            else:
                end = middle

        nums = nums[pivot:] + nums[:pivot]

        start: int = 0
        end: int = len(nums) - 1
        while start <= end:
            middle: int = (start + end) // 2
            real_middle = (middle + pivot) % len(nums)
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            else:
                return real_middle

        return -1
