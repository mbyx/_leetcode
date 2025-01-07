class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        li: int = 0
        ri: int = 3
        count: int = 0
        length: int = len(colors)

        for _ in range(length):
            side_1, middle, side_2 = colors[li], colors[(li + 1) % length], colors[(ri - 1) % length]
            if (side_1 == 1 and middle == 0 and side_2 == 1) or (side_1 == 0 and middle == 1 and side_2 == 0):
                count += 1
            li = (li + 1) % length
            ri = (ri + 1) % length

        return count
