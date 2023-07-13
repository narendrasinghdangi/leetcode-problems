class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in num[::-1]:
            if int(i)%2!=0:
                return num
            else:
                num=num[:-1]
        return ""
        