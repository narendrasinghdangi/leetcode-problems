class Solution:
    def addDigits(self, num: int) -> int:
        lol=num
        while len(str(num))>1:
            lol=0
            for i in str(num):
                lol=lol+int(i)
            num=lol
        return lol

