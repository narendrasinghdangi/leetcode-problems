class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        li=[[]]
        for i in range(len(nums)):
            l=[]
            for j in range(len(li)):
                l.append(li[j]+[nums[i]])
            for j in l:
                li.append(j)
        return li