class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=2
        while len(nums)>i:
            if nums[i]==nums[i-1] and nums[i-1]==nums[i-2]:
                nums.remove(nums[i])
                i=i-1
            i=i+1