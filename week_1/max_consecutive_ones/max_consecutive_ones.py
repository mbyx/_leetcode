class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if all(map(lambda num: num == 0, nums)):
            return 0

        count: int = 1
        max_count: int = 1

        prev_index: int = 0
        for num in nums[1:]:
            prev = nums[prev_index]
            if num == prev == 1 and count == 0:
                count += 2
            elif num == prev == 1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
            prev_index += 1

        return max(max_count, count)
