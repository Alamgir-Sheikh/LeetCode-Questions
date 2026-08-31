class Solution:

    # def addByDigits(self, n):
    #     sum = 0
    #     while n:
    #         sum += n % 10
    #         n = n//10
    #     return sum

    def addDigits(self, num: int) -> int:
    #     if num in range(10):
    #         return num
        
    #     while num not in range(10):
    #         num = self.addByDigits(num)
    #     return num
        if num == 0:
            return 0

        return 1 + ((num-1) % 9)