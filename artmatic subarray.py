class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        lol = []
        for i in range(len(l)):
            li = []
            li = nums[l[i]:r[i]+1]
            li.sort()
            diff = li[0]-li[1]
            flag = True
            for j in range(1, len(li)-1):
                if diff != li[j]-li[j+1]:
                    flag = False
            lol.append(flag)
        print(lol)


s = Solution()
s.checkArithmeticSubarrays([-12, -9, -3, -12, -6, 15, 20, -
                           25, -20, -15, -10], [0, 1, 6, 4, 8, 7], [4, 4, 9, 7, 9, 10])
