class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        rightIndex = len(nums) - 1
        leftIndex = 0
        while leftIndex < rightIndex:
            if nums[leftIndex] % 2 != 0 and nums[rightIndex] % 2 == 0:
                nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
            elif nums[leftIndex] % 2 == 0 and nums[rightIndex] % 2 == 0:
                leftIndex += 1
            elif nums[leftIndex] % 2 != 0 and nums[rightIndex] % 2 != 0:
                rightIndex -= 1
            else:
                leftIndex += 1
        return nums
