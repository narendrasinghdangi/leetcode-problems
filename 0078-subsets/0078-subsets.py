class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        li=[[]]
        for i in range(len(nums)):
            for j in range(len(li)):
                li.append(li[j]+[nums[i]])
        return li