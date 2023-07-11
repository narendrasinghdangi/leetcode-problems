class Solution:
    def tribonacci(self, n: int) -> int:
        li=[0,1,1]
        for i in range(3,n+1):
            li.append(li[i-1]+li[i-2]+li[i-3])
        return li[n]