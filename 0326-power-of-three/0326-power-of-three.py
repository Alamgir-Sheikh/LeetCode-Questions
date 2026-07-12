class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # for i in range(0, (n//2)+1):
        #     if (3 ** i) == n:
        #         return True
        return n > 0 and 1162261467 % n == 0