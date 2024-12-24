class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        ranges = []
        start_index: int = 0
        read_index: int = 0
        
        for num in nums[1:]:
            if num - nums[read_index] > 1:
                if start_index != read_index:
                    ranges.append(f"{nums[start_index]}->{nums[read_index]}")
                else:
                    ranges.append(f"{nums[start_index]}")
                start_index = read_index + 1
            read_index += 1

        if start_index != read_index:
            ranges.append(f"{nums[start_index]}->{nums[read_index]}")
        else:
            ranges.append(f"{nums[start_index]}")

        return ranges
