class Solution:
    def isPalindrome(self, s: str) -> bool:
        lol="".join(ch for ch in s if ch.isalnum())
        lol=lol.lower()
        return lol==lol[::-1]