class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums=list(set(nums))
        if k==0:
            return len(nums)
        nums.sort()
        c=0
        mi=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-mi==k:
                c=c+1     
                if i==len(nums)-1:
                    return c
                mi=nums[i+1]
            if nums[i]-mi>k:
                c=c+1
                mi=nums[i]
            
        return c+1