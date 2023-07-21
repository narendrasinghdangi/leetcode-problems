class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        li=[]
        for i in range(len(nums)):
            if nums[i]==0:
                li.append(i)
        if len(li)==0 or len(li)==1:
            return len(nums)-1
        m=0
        li.insert(0,-1)
        li.append(len(nums))
        for i in range(len(li)-2):
            l=li[i+2]-li[i]-2
            m=max(m,l)
        return m