class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        m=[]
        for i in range(len(number)):
            if number[i]==digit:
                m.append(int(number[:i]+number[i+1:]))
        return str(max(m))
                
                