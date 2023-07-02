class Solution:
    def canJump(self, nums: List[int]) -> bool:
        s=nums[0]
        i=1
        while s>0 and i!=len(nums):
            if nums[i]>=s:
                s=nums[i]
            else:
                s=s-1
            i=i+1
        if i==len(nums):
            return True
        return False
            