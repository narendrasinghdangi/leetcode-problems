class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<=0:
                nums[i]=-nums[i]
                k=k-1
                if k==0:
                    return sum(nums)
        
        nums.sort()
        if k % 2 == 0:
            return sum(nums)
        nums[0] = -nums[0]
        return sum(nums)