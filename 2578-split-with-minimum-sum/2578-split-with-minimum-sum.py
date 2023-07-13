class Solution:
    def splitNum(self, num: int) -> int:
        nums=sorted(str(num))
        num1=""
        num2=""
        for i in range(len(nums)):
            if i%2==0:
                num1=num1+nums[i]
            else:
                num2=num2+nums[i]
        return int(num1)+int(num2)
        