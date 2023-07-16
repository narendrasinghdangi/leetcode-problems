class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l=[a,b,c]
        l.sort()
        lol=0
        if l[0]+l[1]<=l[2]:
            return l[0]+l[1]
        else:
            lol=l[0]+l[1]-l[2]
            return l[2]+lol//2