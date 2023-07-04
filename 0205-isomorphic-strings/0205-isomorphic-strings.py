class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        li1=[]
        li2=[]
        for i in s:
            li1.append(s.index(i))
        for i in t:
            li2.append(t.index(i))
        return li1==li2