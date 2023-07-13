class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        m=0
        for i in range(1,len(colors)):
            if colors[0]!=colors[i]:
                    m=i
        for i in range(len(colors)-1):
            if colors[-1]!=colors[i]:
                if len(colors)-i-1>m:
                    m=len(colors)-i-1
        return m