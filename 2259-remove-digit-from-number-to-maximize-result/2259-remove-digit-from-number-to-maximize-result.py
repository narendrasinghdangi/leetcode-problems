class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        m=[]
        number=list(number)
        for i in range(len(number)):
            if number[i]==digit:
                m.append(int("".join(number[:i])+"".join(number[i+1:])))
        return str(max(m))
                
                