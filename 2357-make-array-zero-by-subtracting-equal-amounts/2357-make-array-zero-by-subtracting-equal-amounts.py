class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            if set(nums)=={0}:
                break
            m=float("inf")
            for j in nums:
                if j<m and j!=0:
                    m=j
            for j in range(len(nums)):
                if nums[j]!=0:
                    nums[j]=nums[j]-m
            c=c+1
        return c