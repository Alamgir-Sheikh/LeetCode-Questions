class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        s_word = min(strs, key=len)
        for i in range(len(s_word)):
            prefix = s_word[:i+1]
            print(prefix)
            for el in strs:
                if prefix == el[:i+1]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                res = prefix
        return res