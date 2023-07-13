class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current=int(current[:2])*60+int(current[3:])
        correct=int(correct[:2])*60+int(correct[3:])
        lol=correct-current
        a=lol//60
        lol=lol-60*a
        b=lol//15
        lol=lol-15*b
        c=lol//5
        lol=lol-5*c
        return a+b+c+lol
            
     
        