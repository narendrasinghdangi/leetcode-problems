class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n//2
        j = n - 1
        res = 0
        for i in range(mid - 1, -1, -1):
            if nums[i] < nums[j]:
                j -= 1
            else:
                res += 1
        return res + j - mid + 1