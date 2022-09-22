class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        l = ""
        for i in s:
            l = l+i[::-1]+" "

        return l[:-1]


s = Solution()
s.reverseWords("lkfijij gigiegm gigeig")
