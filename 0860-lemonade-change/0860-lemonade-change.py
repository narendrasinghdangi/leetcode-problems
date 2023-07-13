class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c=0
        a=0
        for i in bills:
            if i==5:
                c=c+1
            elif i==10:
                if c==0:
                    return False
                c=c-1
                a=a+1
            else:
                if c==0:
                    return False
                if a==0:
                    if 5*c>=15:
                        c=c-2
                        a=a+1
                    else:
                        return False
                c=c-1
                a=a-1    
        return True