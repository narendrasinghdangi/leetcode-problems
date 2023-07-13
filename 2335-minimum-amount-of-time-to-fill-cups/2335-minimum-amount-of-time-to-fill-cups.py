class Solution:
    def fillCups(self, amount: List[int]) -> int:
        c=0
        while set(amount)!={0}:
            m=float("inf")
            for i in amount:
                if i<m and i!=0:
                    m=i
            m=amount.index(min(amount))
            if m==0:
                if amount[1]!=0:
                    amount[1]=amount[1]-1
                if amount[2]!=0:
                    amount[2]=amount[2]-1
            elif m==1:
                if amount[0]!=0:
                    amount[0]=amount[0]-1
                if amount[2]!=0:
                    amount[2]=amount[2]-1
            else:
                if amount[0]!=0:
                    amount[0]=amount[0]-1
                if amount[1]!=0:
                    amount[1]=amount[1]-1
            c=c+1
        return c