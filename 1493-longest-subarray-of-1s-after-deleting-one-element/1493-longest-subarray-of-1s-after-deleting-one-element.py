class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if set(nums)=={1}:
            return len(nums)-1
        i=0
        m=0
        t=True
        while len(nums)>i and t:
            c=0
            j=i
            z=0
            while len(nums)>j:
                if j==len(nums)-1:
                    t=False
                if nums[j]==1:
                    c=c+1
                else:
                    z=z+1
                    if z==2:
                        break
                    i=j+1
                j=j+1
            m=max(m,c)
        return m