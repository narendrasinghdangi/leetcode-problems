class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        li=[]
        for i in queries:
            for j in range(len(nums)):
                if nums[j]>i:
                    li.append(j)
                    break
                j=j+1
            if i>=nums[-1]:
                li.append(len(nums))
        return li