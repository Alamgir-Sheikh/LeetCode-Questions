class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        chars = len(columnTitle)
        for i in range(chars):
            # print(f"{columnTitle[i]}: {ord(columnTitle[i])}")
            ans += (ord(columnTitle[i]) - 64) * 26 ** (chars - i - 1)
        return ans