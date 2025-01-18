class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallestEatingSpeed: int = 1
        largestEatingSpeed: int = max(piles)

        while smallestEatingSpeed < largestEatingSpeed:
            middleEatingSpeed: int = (smallestEatingSpeed + largestEatingSpeed) // 2
            hours: int = sum((pile + middleEatingSpeed - 1) // middleEatingSpeed for pile in piles)
            if hours > h:
                smallestEatingSpeed = middleEatingSpeed + 1
            elif hours <= h:
                largestEatingSpeed = middleEatingSpeed

        return smallestEatingSpeed
