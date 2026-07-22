class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = 0
        e = len(s) - 1

        while st <= e:
            print(f"s[st]: {s[st]}, s[e]: {s[e]}, {s[st]} == {s[e]}: {s[st] == s[e]}")
            if s[st].isalnum() and s[e].isalnum():
                if s[st] != s[e]:
                    return False
                st += 1
                e -= 1
            elif not s[st].isalnum():
                st += 1
            elif not s[e].isalnum():
                e -= 1
        return True