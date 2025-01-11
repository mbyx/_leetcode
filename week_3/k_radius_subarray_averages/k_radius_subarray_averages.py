class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n: int = len(nums)
        m: int = 2 * k + 1 # Convert radius into normal window size.
        avgs: list[int] = [-1] * n

        if n < m:
            return avgs

        if k == 0:
            return nums

        window_sum = sum(nums[:m])
        avgs[k] = window_sum // m

        for i in range(1, n - m + 1):
            window_sum += nums[i + m - 1]
            window_sum -= nums[i - 1]
            avgs[i + k] = window_sum // m

        return avgs
