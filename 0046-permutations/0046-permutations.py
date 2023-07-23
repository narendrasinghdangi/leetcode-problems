class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums=permutations(nums)
        li=[]
        for i in nums:
            li.append(list(i))
        return li