class Solution:
    def climbStairs(self, n: int) -> int:
        li=[1,2]
        for i in range(n-2):
            li.append(li[i]+li[i+1])
        return li[n-1]
        