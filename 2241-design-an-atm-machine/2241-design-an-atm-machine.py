class ATM:

    def __init__(self):
        self.li=[0,0,0,0,0]

    def deposit(self, b: List[int]) -> None:
        for i in range(5):
            self.li[i]+=b[i]
        

    def withdraw(self, amount: int) -> List[int]:
        ans=[0,0,0,0,0]
        if(amount%10):return[-1]
        if(amount>=500 and self.li[4]>0):
            ans[4]+=min(self.li[4],(amount//500))
            amount-=(500*ans[4])
        if(amount>=200 and self.li[3]>0):
            ans[3]+=min(self.li[3],(amount//200))
            amount-=(200*ans[3])
        if(amount>=100 and self.li[2]>0):
            ans[2]+=min(self.li[2],(amount//100))
            amount-=(100*ans[2])
        if(amount>=50 and self.li[1]>0):
            ans[1]+=min(self.li[1],(amount//50))
            amount-=(50*ans[1])
        if(amount>=20 and self.li[0]>0):
            ans[0]+=min(self.li[0],(amount//20))
            amount-=(20*ans[0])
        if(amount!=0):return [-1]
        for i in range(5):
            self.li[i]-=ans[i]
        return ans