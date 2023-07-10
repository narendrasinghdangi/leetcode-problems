class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        li=[]
        r1,r2=0,0
        lol=nums
        for i in range(len(nums)-1):
            r1,r2=r2,max(nums[i]+r1,r2)
        li.append(r2)
        r1,r2=0,0
        for i in range(1,len(lol)):
            r1,r2=r2,max(nums[i]+r1,r2)
        li.append(r2)
        return max(li)