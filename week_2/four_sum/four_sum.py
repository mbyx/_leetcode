def twoSum(nums: List[int], target: int) -> List[Tuple[int, int]]:
    li = 0
    ri = len(nums) - 1

    pairs = []
    while li < ri:
        b, c = nums[li], nums[ri]
        if b + c == target and li != ri:
            pairs.append((b, c))
            li += 1
            ri -= 1
        elif b + c < target:
            li += 1
        else:
            ri -= 1
    return pairs

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        quadruplets = []

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                a, b = nums[i], nums[j]
                pairs = twoSum(nums[j + 1:], target - a - b)
                for c, d in pairs:
                    quad = [a, b, c, d]
                    quad.sort()
                    if quad not in quadruplets and i != j:
                        quadruplets.append(quad)

        return quadruplets
