import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = collections.Counter(nums1) & collections.Counter(nums2)
        nums = []
        for num, count in intersection.items():
            for _ in range(count):
                nums.append(num)
        return nums
