class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            # print(f"{n} >> {i}, bit: {bit}")
            # print(f"res: {res | bit << (31 - i)}")
            res = res | (bit << (31 - i))
        print(res)
        return res