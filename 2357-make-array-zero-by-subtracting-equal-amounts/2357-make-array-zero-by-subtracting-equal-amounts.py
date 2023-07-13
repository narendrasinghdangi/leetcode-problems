class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d=Counter(nums)
        c=0
        for i in d:
            if i!=0:
                c=c+1
        return c