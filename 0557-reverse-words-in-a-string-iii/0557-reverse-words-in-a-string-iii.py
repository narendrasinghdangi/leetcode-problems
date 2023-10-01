class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        k=""
        for i in s:
            k=k+" "+i[::-1]
        return k[1:]