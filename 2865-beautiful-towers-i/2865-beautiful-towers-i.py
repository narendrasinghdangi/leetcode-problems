class Solution:
    def maximumSumOfHeights(self, A: List[int]) -> int:
        res = 0
        n = len(A)
        for i in range(n):
            cur = v = A[i]
            for j in range(i - 1, -1, -1):
                v = min(v, A[j])
                cur += v
            v = A[i]
            for j in range(i + 1, n):
                v = min(v, A[j])
                cur += v
            res = max(res, cur)
        return res