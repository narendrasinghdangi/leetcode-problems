class Solution:
    def isHappy(self, n: int) -> bool:
        li=[n]
        while n!=1:
            lol=0
            for i in str(n):
                lol=lol+int(i)*int(i)
            n=lol
            if n==1:
                return True
            if n in li:
                return False
            else:
                li.append(n)
        return True
                
            
                