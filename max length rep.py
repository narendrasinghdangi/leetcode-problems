class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        strnum2 = "".join([chr(i) for i in nums2])
        strmax = ""
        ans = 0
        for i in nums1:
            strmax = strmax+chr(i)
            if strmax in strnum2:
                ans = max(ans, len(strmax))
            else:
                strmax = strmax[1:]
            print(strmax)


s = Solution()
s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
