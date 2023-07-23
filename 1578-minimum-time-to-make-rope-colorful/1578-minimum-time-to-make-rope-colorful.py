class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors=list(colors)
        c=0
        i=1
        while len(colors)>i:
            if colors[i]==colors[i-1]:
                if neededTime[i]>neededTime[i-1]:
                    c=c+neededTime.pop(i-1)
                    colors.pop(i-1)
                    i=i-1
                else:
                    c=c+neededTime.pop(i)
                    colors.pop(i)
                    i=i-1
            i=i+1
        return c