class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        count = Counter()
        res = 0
        for x1, y1 in coordinates:
            for x in range(k + 1):
                res =res+ count[x1 ^ x, y1 ^ (k - x)]
            count[x1, y1] += 1
        return res