class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed_words = [word[::-1] for word in words]
        print(reversed_words)
        return " ".join(reversed_words)