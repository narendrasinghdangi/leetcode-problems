class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while (len(nums)-1)>i:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i+1])
                i=i-1
            i=i+1