class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks: dict[int, str] = {}
        descending_scores = sorted(score)[::-1]

        for rank, s in enumerate(descending_scores):
            if rank == 0:
                ranks[s] = 'Gold Medal'
            elif rank == 1:
                ranks[s] = 'Silver Medal'
            elif rank == 2:
                ranks[s] = 'Bronze Medal'
            else:
                ranks[s] = str(rank + 1)

        return [ranks[s] for s in score]
