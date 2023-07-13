class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        for i in range(1,len(nums)+1):
            if sum(nums[:i])>sum(nums[i:]):
                return nums[:i]
            
        