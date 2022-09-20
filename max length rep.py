class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        result = 0
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    new_value = dp[i][j]+1
                    dp[i+1][j+1] = new_value
                    result = max(result, new_value)
                    print(result)
                    print(dp)


s = Solution()
s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
