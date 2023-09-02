class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        su=0
        for i in range(len(nums)-k+1):
            s=nums[i:i+k]
            if len(set(s))>=m and sum(s)>su:
                su=sum(s)
        return su