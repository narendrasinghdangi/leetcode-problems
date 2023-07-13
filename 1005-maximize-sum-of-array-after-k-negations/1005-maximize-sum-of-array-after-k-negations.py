class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(k):
            t=True
            for j in range(len(nums)):
                if nums[j]<=0:
                    nums[j]=-nums[j]
                    t=False
                    break
            if t:
                nums[0]=-nums[0]
            nums.sort()
        return sum(nums)