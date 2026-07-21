class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1]) % 2 == 1:
            return num
        else:
            for i in range(len(num), 0, -1):
                if int(num[i-1]) % 2 == 1:
                    return num[:i]
        return ""