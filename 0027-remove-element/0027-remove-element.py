class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]=101
        nums.sort()
        l=0
        for i in range(len(nums)):
            if nums[i]==101:
                break
            l=l+1
        return l