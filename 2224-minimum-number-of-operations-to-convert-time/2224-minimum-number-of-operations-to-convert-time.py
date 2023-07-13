class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current=int(current[:2])*60+int(current[3:])
        correct=int(correct[:2])*60+int(correct[3:])
        c=0
        lol=correct-current
        li=[60,15,5,1]
        while lol!=0:
            for i in li:
                if lol>=i:
                    c=c+1
                    lol=lol-i
                    break
        return c
        