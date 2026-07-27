class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        start = 0
        end = 0

        while end < len(word):
            if word[end] == ch:
                break
            end += 1
        
        # print(start, end)
        if end != len(word):
            return word[start:end+1][::-1] + word[end+1:]
        else:
            return word