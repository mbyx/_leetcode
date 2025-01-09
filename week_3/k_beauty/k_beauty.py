class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num: str = str(num)
        n: int = len(str_num)

        count: int = 0
        for i in range(n - k + 1):
            substring: str = ''
            for j in range(k):
                substring += str_num[i + j]
            sub_num: int = int(substring)
            if sub_num != 0 and num % sub_num == 0:
                count += 1

        return count
