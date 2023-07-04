class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li1=[]
        li2=[]
        s=s.split()
        for i in pattern:
            li1.append(pattern.index(i))
            
        for i in s:
            li2.append(s.index(i))
        return li1==li2