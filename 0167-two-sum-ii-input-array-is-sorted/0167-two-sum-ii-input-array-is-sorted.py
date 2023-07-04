class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, val in enumerate(nums):
            compl = target - val
            if compl in d:
                return (d[compl]+1, idx+1)
            d[val] = idx