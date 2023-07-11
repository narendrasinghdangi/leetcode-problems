class Solution:
    def tribonacci(self, n: int) -> int:
        li=[0,1,1]
        for i in range(n-2):
            li.append(li[i]+li[i+1]+li[i+2])
        return li[n]