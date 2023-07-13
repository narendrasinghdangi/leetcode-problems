class Solution:
    def fillCups(self, amount: List[int]) -> int:
        c=0
        while set(amount)!={0}:
            m=amount.index(max(amount))
            amount[m]=amount[m]-1
            for i in range(3):
                if amount[i]!=0 and i!=m:
                    amount[i]=amount[i]-1
                    break
            c=c+1
        return c