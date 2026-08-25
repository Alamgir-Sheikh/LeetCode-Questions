class Solution:

    def get_sum(self, num):
        res = 0
        while num:
            res = res + (num % 10) ** 2
            num //= 10
        print(res)
        return res


    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_sum(n)
        return n == 1