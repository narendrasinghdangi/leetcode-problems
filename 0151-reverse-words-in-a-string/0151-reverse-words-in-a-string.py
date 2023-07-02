class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s=" ".join(s[::-1])
        return s