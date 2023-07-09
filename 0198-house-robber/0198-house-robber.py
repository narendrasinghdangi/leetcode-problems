class Solution:
    def rob(self, nums: List[int]) -> int:
        r1,r2=0,0
        for i in range(len(nums)):
            r1,r2=r2,max(nums[i]+r1,r2)
        return r2