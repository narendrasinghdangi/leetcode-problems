class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        m=0
        for i in range(len(satisfaction)):
            s=0
            for j in range(len(satisfaction)):
                s=s+satisfaction[j]*(j+1)
            m=max(m,s)
            satisfaction.pop(0)
        return m