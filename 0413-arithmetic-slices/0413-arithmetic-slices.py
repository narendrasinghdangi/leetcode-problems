class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        c=0
        cur=0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                cur=cur+1
                c=c+cur
            else:
                cur=0
        return c
                        