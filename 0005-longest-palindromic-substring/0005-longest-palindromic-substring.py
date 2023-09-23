class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub = ''
        for indi, i in enumerate(s):
            for indj, j in enumerate(s[indi:],indi):
                if i == j and s[indi:indj+1] == s[indi:indj+1][::-1] and len(s[indi:indj+1]) > len(sub):
                    sub = s[indi:indj+1]
        return sub