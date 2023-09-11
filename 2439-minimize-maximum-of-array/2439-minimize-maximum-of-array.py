class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        start, end = 0, max(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.check(nums, mid):
                end = mid
            else:
                start = mid
        if self.check(nums, start):
            return start
        else:
            return end
        
    def check(self, nums, k):
        n = len(nums)
        temp = 0
        for i in range(n - 1, 0, -1):
            if temp + nums[i] > k:
                temp += nums[i] - k
            else:
                temp = 0
        return False if temp + nums[0] > k else True