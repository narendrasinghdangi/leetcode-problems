class Solution:
    def countOrders(self, n: int) -> int:
        c=1
        for i in range(2,n+1):
            c=c*(2*i-1)*i
        return c%(10**9+7)