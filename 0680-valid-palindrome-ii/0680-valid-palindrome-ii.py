class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                l = s[i:len(s)-i-1]
                r = s[i+1:len(s)-i]
                return l == l[::-1] or r == r[::-1]
        return True