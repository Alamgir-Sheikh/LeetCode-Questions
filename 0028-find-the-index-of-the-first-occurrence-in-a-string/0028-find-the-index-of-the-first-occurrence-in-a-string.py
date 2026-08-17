class Solution:
    def compute_lps(self, pattern):
        lps = [0] * len(pattern)
        i = 0
        j = 1
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                lps[j] = i+1

                i += 1
                j += 1  
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]

        return lps

    def strStr(self, haystack: str, needle: str) -> int:
        lps = self.compute_lps(needle)
        print(lps)

        i = j = 0
        while i < len(haystack) and j < len(needle):
            # print(f"Value of i: {i}, Value of j: {j}")
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j - 1 >= 0:
                    j = lps[j-1]
                else:
                    i += 1
                    j = 0
                
        
        if j == len(needle):
            return i-j
        else:
            return -1
