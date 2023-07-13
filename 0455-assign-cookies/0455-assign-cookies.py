class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j=0
        c=0
        for i in range(len(s)):
            if j<len(g) and g[j]<=s[i]:
                c+=1
                j+=1
        return c