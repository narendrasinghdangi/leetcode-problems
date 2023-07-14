class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i=0
        j=len(s)
        li=[]
        for k in range(len(s)):
            if s[k]=="I":
                li.append(i)
                i=i+1
            else:
                li.append(j)
                j=j-1
        li.append(j)
        return li