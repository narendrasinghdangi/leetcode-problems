class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d or i-d[nums[i]] > k:
                d[nums[i]] = i
            else:
                return True
        return False