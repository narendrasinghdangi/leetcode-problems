class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while len(nums)>i:
            if nums[i]==val:
                nums.remove(val)
                i=i-1
            i=i+1
        return len(nums)