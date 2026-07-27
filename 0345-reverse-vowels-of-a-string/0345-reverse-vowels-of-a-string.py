class Solution:
    def reverseVowels(self, s: str) -> str:
        low = 0
        high = len(s) - 1
        # s = s.lower()
        ls = list(s)
        vowels = 'AEIOUaeiou'
        while low <= high:
            if ls[low] in vowels and ls[high] in vowels:
                ls[low], ls[high] = ls[high], ls[low]
                low += 1
                high -= 1
            elif ls[low] not in vowels:
                low += 1
            else:
                high -= 1
        return "".join(ls)