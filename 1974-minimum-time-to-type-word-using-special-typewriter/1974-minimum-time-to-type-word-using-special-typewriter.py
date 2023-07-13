class Solution:
    def minTimeToType(self, word: str) -> int:
        c=0
        p=97
        for i in word:
            i=ord(i)
            
            if abs(i-p)<=13:
                c=c+abs(i-p)+1
            else:
                c=c+(26-abs(i-p))+1
            p=i
        return c