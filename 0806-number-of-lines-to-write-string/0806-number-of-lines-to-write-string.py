class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        c=0
        ans=0
        for i in s:
            o=ord(i)-97
            o=widths[o]
            if c+o>100:
                ans=ans+1
                c=0
            c=c+o
        return [ans+1,c]