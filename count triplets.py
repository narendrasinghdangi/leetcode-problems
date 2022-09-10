class Solution:
    def countTriplets(self, arr: list[int]):
        res = 0
        for i in range(len(arr)-1):
            xor = 0
            for j in range(i, len(arr)):
                xor = xor ^ arr[j]
                if xor == 0:
                    res = res+j-i
                    print(i, j)
        return res


s = Solution()
s.countTriplets([2, 3, 1, 6, 7])
