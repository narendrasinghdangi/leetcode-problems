class Solution:
    def findTotalSum(self, p: int, c: int, r: int, target: int) -> int:
        count = 0
        for i in range(1, 100):
            for j in range(1, 100):
                for k in range(1, 100):
                    if (i*p+j*c+k*r) == 100 and i+j+k == 100:
                        count = count+1
        print(count)
        return count


s = Solution()
s.findTotalSum(1/5, 1, 10, 100)
