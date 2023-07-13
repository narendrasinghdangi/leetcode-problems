class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        m=0
        number=list(number)
        for i in range(len(number)):
            if number[i]==digit:
                if int("".join(number[:i])+"".join(number[i+1:])) >m:
                    m=int("".join(number[:i])+"".join(number[i+1:]))
        return str(m)
                
                