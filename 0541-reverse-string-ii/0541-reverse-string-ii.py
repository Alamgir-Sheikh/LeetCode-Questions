class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        i = 0
        while i < len(s):
            print(f"Index: {i}, chatAt(i): {s[i]}, 2*{i}+{k}:{2*(i+k)}")
            if i % (2*k) == 0:
                # s[i], s[i+1] = s[i+1], s[i]
                res += s[i:i+k][::-1]
                i += k
            else:
                res += s[i]
                i += 1
        return res